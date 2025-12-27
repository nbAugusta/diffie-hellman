# File: clientTest.py
import diffieHellman as DH
import random

# Set up pairs of parties and run Diffie-Hellman exchanges
n1 = random.randint(1,100)
party1 = DH.Party(n1)
n1b = random.randint(1,100)
party1b = DH.Party(n1b)

dh1 = DH.DiffieHellman(97,3,party1,party1b)
dh1.run()


n2 = random.randint(1,100)
party2 = DH.Party(n2)
n2b = random.randint(1,100)
party2b = DH.Party(n2b)

dh2 = DH.DiffieHellman(23,5,party2,party2b)
dh2.run() 


# Test cases for party methods implemented via Diffie-Hellman exchanges      
def test_keyparts():

    assert party1.partkey == (3**n1)%97
    assert party2.partkey == (5**n2)%23
    
    assert party1b.partkey == (3**n1b)%97
    assert party2b.partkey == (5**n2b)%23
    

def test_fullkey():
    
    assert party1.finalkey == (party1b.partkey**n1)%97
    assert party1b.finalkey == (party1.partkey**n1b)%97
    assert party1.finalkey == party1b.finalkey

    assert party2.finalkey == (party2b.partkey**n2)%23
    assert party2b.finalkey == (party2.partkey**n2b)%23
    assert party2.finalkey == party2b.finalkey
