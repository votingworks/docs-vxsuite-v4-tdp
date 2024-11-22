# Password and Credential Policies

On VxSuite machines, there are no passwords for election administrators to use – only smart cards as described above. The smart cards all use 256-bit elliptic-curve digital signatures, which makes them cryptographically strong. In addition, the PINs that gate usage of those cards follow the NIST recommendations for authentication – 6 digits long, randomly generated (as opposed to chosen by the user who might use a birthdate), and never a weak PIN like 000000.
