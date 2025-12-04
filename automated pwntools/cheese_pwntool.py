# Automated Python program with pwntools.

from pwn import *
import string

# Initializing variables.
alphabet = list(string.ascii_uppercase)

# Initializing host and port of the server.
HOST = 'verbal-sleep.picoctf.net'
PORT = 51043

# Connecting to the server.
s = remote(HOST, PORT)

# Getting response after connection is established.
res = s.recvuntil(b'would you like to do?').decode()
print(res)

# Extracting ciphertext to decrypt.
ciphertext_begin = res.find('it:')
ciphertext_end = res.find('Hint:')
ciphertext = res[ciphertext_begin+5:ciphertext_end-1]
print()
print("The ciphertext is:", ciphertext)

# Entering input "e" to begin encrypting "cheddar" to get the 2 equations.
print("\nSending 'e' to encrypt 'cheddar'")
s.sendline(b'e')

# Getting response after sending "e".
res = s.recvuntil(b'encrypt?').decode()
print(res)

# Entering "cheddar".
print("\nSending 'cheddar'...\n")
s.sendline(b'cheddar')

# Getting response after sending "cheddar".
res = s.recvuntil(b'would you like to do?').decode()
print(res)

# Extracting the ciphertext for "cheddar".
cheddar_cipher_begin = res.find(':')
cheddar_cipher_end = res.find('Not sure why')
cheddar_cipher = res[cheddar_cipher_begin+3:cheddar_cipher_end-1]
print()
print("The ciphertext for 'cheddar' is:", cheddar_cipher)

# Constructing the 2 equations.
# Linear equation form: y = mx + b (mod 26).
C_ind = alphabet.index('C')
c_ind_1 = alphabet.index(cheddar_cipher[0])
H_ind = alphabet.index('H')
c_ind_2 = alphabet.index(cheddar_cipher[1])

eq_1 = [C_ind, 1, c_ind_1]
eq_2 = [H_ind, 1, c_ind_2]

# Solving the system of equations to calculate m.
m_1 = -eq_1[0] + eq_2[0]
m_2 = -eq_1[2] + eq_2[2]

if m_2 % m_1 != 0:
    m_3 = pow(m_1, -1, 26)
    m = pow(m_2 * m_3, 1, 26)
else:
    m = pow(m_2 // m_1, 1, 26)

print("\nm =", m)

# Solving the system of equations to calculate b.
b = pow(eq_1[2] - eq_1[0] * m, 1, 26)
print("b =", b)
print()

# Printing the full equation in y = mx + b (mod 26) format (encryption equation).
print("The equation is: y = " + str(m) + "x + " + str(b) + " (mod 26)")

# Printing the inverse of this equation (decryption equation).
print("The inverse equation is: x = (y - " + str(b) + ") / " + str(m) + " (mod 26)")

# Running a loop on ciphertext to decrypt each letter with the decryption equation.
decrypted = []
for i in ciphertext:
    index = alphabet.index(i)
    a = pow(m, -1, 26) * pow(index - b, 1, 26)
    a = pow(a, 1, 26)
    decrypted.append(alphabet[a])

decrypted = ''.join(decrypted)
print("\nThe decrypted text:", decrypted)

# Entering the decrypted text to get the flag.
s.sendline(b'g')

res = s.recvuntil(b'my cheese?').decode()
print(res)

s.sendline(decrypted.encode())

# If running on Webshell. Comment out if running on jupyter notebook.
s.interactive()

# If running on jupyter notebook environment. Comment out if running on Webshell.
try:
    res = s.recvuntil(b'}').decode()
    print(res)
except Exception:
    res = s.recvuntil(b'!').decode()
    print(res)
    pass