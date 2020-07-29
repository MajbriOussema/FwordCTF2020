from pwn import *

p = process("./run.sh")
data = p.recvuntil("\n-!-")
ciphertext = data.strip("\n-!-").replace("\n","").split(" ")
ciphertext = ciphertext[:len(ciphertext)-1]
keylength = int(ciphertext[71]) - int(ciphertext[7])
print "key length = ",keylength
ciphertext[71] = str(int(ciphertext[71]) - keylength)


lk = []
s = [1,13,5,17,9]

for el in s:
	lk.append(chr(int(ciphertext[el])))

print "extracted longkey = ",lk

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
log.warn("password = "+password)