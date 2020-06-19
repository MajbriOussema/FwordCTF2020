from pwn import *


p = process("./run")
p.recvuntil("longkey = ")
longkey = p.recv()
log.info("longkey = "+longkey)
log.info("longkey length = "+longkey)
data = p.recvuntil("\nBye")
ciphertext = data.strip("\nBye").replace("\n","").split(" ")
ciphertext = ciphertext[:len(ciphertext)-1]
keylength = int(ciphertext[71]) - int(ciphertext[7])
print "key length = ",keylength
print ciphertext

lk = [0,0,0,0,0]
for j,i in zip(range(0,len(ciphertext),2),range(len(ciphertext)-1,-1,-2)):
	if j % 2 == 0:
		lk[j%5] = int(ciphertext[j+1],10)
	