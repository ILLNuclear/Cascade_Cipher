import string
from collections import deque

def cascade_encrypt(plaintext):
    KEY = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" #Keyed Initial state
    x_to_n = {c: i + 1 for i, c in enumerate(KEY)}

    deck = deque(KEY)
    ciphertext = []
    
    for ch in plaintext.upper():
        n = x_to_n [ch]
        temp_pile = []
        
        for _ in range(n):
            temp_pile.append(deck.popleft())
        
        deck.extend(reversed(temp_pile))
        ciphertext.append(deck[0])

    return "".join(ciphertext)
plaintext = "" #Input plaintext
ciphertext = cascade_encrypt(plaintext)
print(ciphertext)
