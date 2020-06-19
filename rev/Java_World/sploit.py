from pwn import *


p = process("./run")
p.recvuntil("longkey = ")
longkey = p.recv()
log.info("longkey = "+longkey)
print len(longkey)
"""p.recvline()
ciphertext = p.recvline()
print ciphertext," --",len(ciphertext)
leak = ""
for i in range(len(ciphertext)-1):
	if i % 2 == 0:
		leak += ciphertext[i]
print leak
"""
