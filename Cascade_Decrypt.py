import string

def cascade_decrypt(plaintext):
    A_Z = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" #Initial state
    n_to_x = {i + 1: c for i, c in enumerate(A_Z)}

    deck = list(A_Z)
    plaintext = []
    
    for ch in ciphertext.upper():
        temp_pile = []
        count = 0
        
        while deck[0] != ch:
            temp_pile.append(deck.pop(0))
            count += 1
        
        plaintext.append(n_to_x[count])
        temp_pile.reverse()
        deck.extend(temp_pile)

    return "".join(plaintext)
ciphertext = "" #Input ciphertext
plaintext = cascade_decrypt(ciphertext)
print(plaintext)
