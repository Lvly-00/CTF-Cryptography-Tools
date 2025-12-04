# Python program for decryption of the given ciphertext.

import string

# Initializing variables for ciphertext and the complete English alphabet.
x = 'OFNYADSOPN'   #Changable
alpha = string.ascii_uppercase

# Running a loop on x to decrypt each letter with the decryption equation.
# Decryption equation: x = (y - 24) / 17 (mod 26)
result = []
for i in x:
    # Finding the index of each letter in the English alphabet.
    index = alpha.index(i)
    
    # With the index as the value of y, plugging it in to the decryption equation.
    # Modular arithmetic property: (a*b) mod n = [(a mod n) * (b mod n)] mod n.
    a = pow(17, -1, 26) * pow(index - 24, 1, 26)
    a = pow(a, 1, 26)
    result.append(alpha[a])

result = ''.join(result)
print(result)
