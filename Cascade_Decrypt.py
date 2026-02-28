import string
from collections import deque

def cascade_decrypt(ciphertext):
    KEY = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" #Keyed Initial state
    n_to_x = {i + 1: c for i, c in enumerate(KEY)}

    deck = deque(KEY)
    plaintext = []

    for ch in ciphertext.upper():
        temp_pile = []
        count = 0
    
        while deck[0] != ch:
            temp_pile.append(deck.popleft())
            count += 1
    
        plaintext.append(n_to_x[count])
        deck.extend(reversed(temp_pile))

    return "".join(plaintext)
ciphertext = ""  #Input ciphertext
plaintext = cascade_decrypt(ciphertext)
print(plaintext)
