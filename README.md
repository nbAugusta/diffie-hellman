# diffie-hellman
A simple object-oriented implementation of Diffie-Hellman key exchange in Python.

## Basic Usage
* The implementation runs entirely from diffieHellman.py, unit tests are contained within test_difHel.py
* The main() function in diffieHellman.py requires the user enter a prime number corresponding to the order of the finite field used to facilitate the key exchange (ex. 23), in addition to a generator of the multiplicative group over that finite field, before beginning key exchange (ex. for the finite field $$\mathbb{Z}_{23}$$, 5 can be given as a generator). 
* After the key exchange is completed, main() will print out the randomly-generated exponents for each party (a,b), their corresponding key components (g^a (mod p), g^b (mod p)), and the final/full key.

(Not for production use)



