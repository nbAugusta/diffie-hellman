# File: diffieHellman.py
import random

def main():
    
    p = input("prime order: p = ")          # Prime order of finite field
    g = input("generator: g = ")            # Generator of multiplicative group Z_p*
    
    a = random.randint(0,100)               # Secret exponents for both parties
    b = random.randint(0,100)   
    
    party1 = Party(a)                       # Exchange occurs between these two parties
    party2 = Party(b)
    
    dh = DiffieHellman(p,g,party1,party2)   # Run exchange 
    dh.run()
    
    # Print results
    print("a = " + str(party1.n) + ", b = " + str(party2.n))
    print("g^a = " + str(party1.partkey))
    print("g^b = " + str(party2.partkey))
    print("full key: " + str(party1.finalkey))


# Party involved in Diffie-Hellman key exchange
class Party():
    
    def __init__(self,n):
        self.n = n                          # Secret exponent
        self.partkey = None                 
        self.finalkey = None                
        
    def keypart(self,p,g):                  # g^a to send to other party to compute full key g^ab
        self.partkey = (g**self.n)%p
        
    def fullkey(self,key_b,p):              # Compute full key g^ab using received key part key_b = g^b
        self.finalkey = (key_b**self.n)%p
        

# Facilitates Diffie-Hellman key exchange between two parties
class DiffieHellman():

    def __init__(self,p,g,clienta,clientb):
        self.partya = clienta               # Two parties involved in exchange (a and b)
        self.partyb = clientb
        self.p = int(p)                     # Prime order of finite field
        self.g = int(g)                     # Generator of multiplicative group Z_p*
        
    def setkeyparts(self):                  # Compute key parts g^a and g^b
        self.partya.keypart(self.p,self.g)
        self.partyb.keypart(self.p,self.g)
        

    def exchange(self):                     # Exchange key parts and compute full keys for both parties
        self.partya.fullkey(self.partyb.partkey,self.p)
        self.partyb.fullkey(self.partya.partkey,self.p)
        
    
    def run(self):                          # Run the full Diffie-Hellman exchange 
        self.setkeyparts()
        self.exchange()
    

if __name__ == '__main__':
    main()
