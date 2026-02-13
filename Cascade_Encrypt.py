import string

def cascade_encrypt(plaintext):
    A_Z = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" #Initial state
    x_to_n = {c: i + 1 for i, c in enumerate(A_Z)}

    deck = list(A_Z)
    ciphertext = []
    
    for ch in plaintext.upper():
        n = x_to_n [ch]
        temp_pile = []
        
        for _ in range(n):
            temp_pile.append(deck.pop(0))
        
        temp_pile.reverse()
        deck.extend(temp_pile)
        ciphertext.append(deck[0])

    return "".join(ciphertext)
plaintext = "" #Input plaintext
ciphertext = cascade_encrypt(plaintext)
print(ciphertext)
