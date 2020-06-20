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

c = []
for el in ciphertext:
	c.append(chr(int(el)))
print c

lk = []
s = [1,13,5,17,9]

for el in s:
	lk.append(chr(int(ciphertext[el])))

print "extracted lk = ",lk

z = 1
tab = []
for j,i in zip(range(len(ciphertext)),range((keylength*2)-1,-1,-1)):
	if z == 1:
		if (i/2) % 4 != 0:
			tab.append(chr(int(ciphertext[j]) + 100 - ord(lk[(i/2)%4])))
		else:
			tab.append(chr(int(ciphertext[j]) ^ ord(lk[(j/2)%5])))
	z = -z

for i in range(18,36,1):
	tab[i] = chr(ord(tab[i]) ^ 4)
for i in range(17,-1,-1):
	tab[i] = chr(ord(tab[i]) ^ 40)
password = ''.join([tab[i] for i in range(36)])
print password