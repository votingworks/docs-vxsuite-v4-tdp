#!/usr/bin/env python3
"""Checks the images a pull request adds or changes, and the image rows on
the pages it changes, against the style guide's photo rules.

Fails on any added or changed image that carries location metadata (GPS,
or XMP/IPTC location fields): these repos are public. Warns, without
failing, on a new or changed photo that is larger than 1600 px or 500 KB,
isn't a JPEG, isn't 4:3 or 3:4, or isn't named photo-<...>.jpg, and on an
image row that puts a photo beside a screenshot or mixes photo shapes.

A photo is an image named photo-..., or a JPEG/HEIC/WebP/AVIF that isn't a
gallery screenshot; a screenshot is a gallery ID (vx<app>-....png).

usage: check-images.py <base ref>   (from the repository root, in CI)
       check-images.py --list-photos <base ref> [<head ref>]
         print the photos added or changed since <base ref>, one per line
"""
import json, os, re, subprocess, sys, urllib.parse

ASSETS = ".gitbook/assets/"
RASTER = (".jpg", ".jpeg", ".png", ".heic", ".heif", ".webp", ".avif", ".tif", ".tiff")
PHOTO_EXT = (".jpg", ".jpeg", ".heic", ".heif", ".webp", ".avif")
GALLERY = re.compile(r"^vx(admin|centralscan|mark|markscan|print|scan)-[a-z0-9-]+(\.review)?\.png$")
PHOTO_NAME = re.compile(r"^photo-[a-z0-9]+(-[a-z0-9]+)*\.jpg$")
SHAPES = {"4:3": 4 / 3, "3:4": 3 / 4}
MAX_SIDE, MAX_BYTES = 1600, 500_000
LOCATION_TAGS = ["GPSLatitude", "GPSLongitude", "GPSPosition", "XMP:Location", "XMP:City",
                 "XMP:LocationShownGPSLatitude", "IPTC:City", "IPTC:Sub-location"]


def git(*args):
    return subprocess.run(["git", *args], capture_output=True, text=True, check=True).stdout


def is_photo(name):
    n = name.lower()
    return not GALLERY.match(name) and (n.startswith("photo-") or n.endswith(PHOTO_EXT))


def exif(paths):
    if not paths:
        return {}
    out = subprocess.run(["exiftool", "-json", "-n", "-ImageWidth", "-ImageHeight",
                          *["-" + t for t in LOCATION_TAGS], *paths], capture_output=True, text=True)
    return {r["SourceFile"]: r for r in json.loads(out.stdout or "[]")}


def shape(w, h):
    for name, ratio in SHAPES.items():
        if abs(w / h - ratio) / ratio < 0.02:
            return name
    return f"{w}×{h}"


def warn(msg, path=None):
    print(f"::warning{' file=' + path if path else ''}::{msg}")


def changed_photos(base, head="HEAD"):
    changed = git("diff", "--name-only", "--diff-filter=AM", base, head).splitlines()
    return [p for p in changed if p.startswith(ASSETS) and p.lower().endswith(RASTER)
            and is_photo(os.path.basename(p)) and os.path.exists(p)]


def main(base):
    changed = git("diff", "--name-only", "--diff-filter=AM", f"{base}...HEAD").splitlines()
    # Sources of labeled photos (photos/) are public too: checked for location.
    images = [p for p in changed if (p.startswith(ASSETS) or p.startswith("photos/"))
              and p.lower().endswith(RASTER) and os.path.exists(p)]
    pages = [p for p in changed if p.endswith(".md") and os.path.exists(p)]
    meta = exif(images)
    failed = False
    for p in images:
        m = meta.get(p, {})
        found = [t for t in LOCATION_TAGS if t.split(":")[-1] in m or t in m]
        if found:
            failed = True
            print(f"::error file={p}::{p} carries location metadata ({', '.join(found)}). "
                  "Strip it before merging, e.g. exiftool -all= -tagsfromfile @ -icc_profile <file>.")
        name = os.path.basename(p)
        if not is_photo(name) or p.startswith("photos/"):
            continue
        w, h = m.get("ImageWidth"), m.get("ImageHeight")
        if w and h:
            if max(w, h) > MAX_SIDE:
                warn(f"{name} is {w}×{h}; photos are at most 1600 px on the long side (1600×1200 or 1200×1600).", p)
            if shape(w, h) not in SHAPES:
                warn(f"{name} is {w}×{h}; photos are 4:3 (1600×1200) or 3:4 (1200×1600).", p)
        if os.path.getsize(p) > MAX_BYTES:
            warn(f"{name} is {os.path.getsize(p) // 1000} KB; a 1600 px JPEG is usually 200–400 KB.", p)
        if not name.lower().endswith((".jpg", ".jpeg")):
            warn(f"{name} isn't a JPEG; save photos as JPEG.", p)
        elif not PHOTO_NAME.match(name):
            warn(f"{name}: name photos photo-<device>-<subject>.jpg, in lowercase kebab-case.", p)
    # Rows: a <div> of figures on a changed page.
    for page in pages:
        text = open(page, encoding="utf-8").read()
        for row in re.finditer(r"<div[^>]*>(.*?)</div>", text, re.S):
            names = [urllib.parse.unquote(n) for n in re.findall(r'src="[^"]*\.gitbook/assets/([^"]+)"', row.group(1))]
            if len(names) < 2:
                continue
            line = text.count("\n", 0, row.start()) + 1
            photos = [n for n in names if is_photo(n)]
            shots = [n for n in names if GALLERY.match(n)]
            if photos and shots:
                print(f"::warning file={page},line={line}::A row puts photos ({', '.join(photos)}) beside screenshots "
                      f"({', '.join(shots)}); give photos their own row.")
            dims = exif([ASSETS + n for n in photos if os.path.exists(ASSETS + n)])
            shapes = {shape(d["ImageWidth"], d["ImageHeight"]) for d in dims.values() if d.get("ImageWidth") and d.get("ImageHeight")}
            if len(shapes) > 1:
                print(f"::warning file={page},line={line}::Photos in one row have different shapes ({', '.join(sorted(shapes))}); "
                      "use one shape per row, 4:3 or 3:4.")
    if failed:
        sys.exit(1)
    print(f"Checked {len(images)} changed image(s) and {len(pages)} changed page(s).")


if __name__ == "__main__":
    if sys.argv[1:2] == ["--list-photos"]:
        for photo in changed_photos(*sys.argv[2:4]):
            print(photo)
    else:
        main(sys.argv[1] if len(sys.argv) > 1 else "origin/main")
