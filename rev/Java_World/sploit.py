from pwn import *

p = process("./run")
p.recvuntil("longkey = ")
longkey = p.recv().rstrip("\n")
log.info("longkey = "+longkey)
log.info("longkey length = "+str(len(longkey)))
data = p.recvuntil("\nBye")
ciphertext = data.strip("\nBye").replace("\n","").split(" ")
ciphertext = ciphertext[:len(ciphertext)-1]
keylength = int(ciphertext[71]) - int(ciphertext[7])
print "key length = ",keylength
ciphertext[71] = str(int(ciphertext[71]) - keylength)

#print ciphertext
c = []
for el in ciphertext:
	c.append(chr(int(el)))
print c

"""ciphertext2 = ""
for i in range(len(ciphertext)):
	if i % 2 == 0:
		ciphertext2 += chr(int(ciphertext[i]))
	else:
"""

lk = ['0','0','0','0','0']
z = 1
f = 0
for j,k in zip(range(1,len(ciphertext)/2,2),range(keylength-1,-1,-1)):
	if z == -1:
		lk[k%4] = chr(int(ciphertext[j]))
	else:
		lk[(j-1)%5] = chr(int(ciphertext[j]))
	z = -z 
	f += 1
	if f == 5:
		break

"""if((j-1)%2 == 0):
	 = chr(int(ciphertext[j]))"""
		
print lk

#print ciphertext2