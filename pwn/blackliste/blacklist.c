#include <fcntl.h>
#include <stddef.h>
#include <seccomp.h>
#include <stdlib.h>
#include <stdio.h>
/* 
	gcc -S blacklist.c -o blacklist.s
	gcc -c blacklist.s // adding (popq %r8,ret;popq %r9,ret;popq %r10,ret)
	gcc blacklist.o -o blacklist -static -fno-stack-protector -no-pie -s -lseccomp

*/
int init(){
	setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
    scmp_filter_ctx ctx;
    ctx = seccomp_init(SCMP_ACT_ALLOW);
    int l [17] = {1,2,18,20,56,57,58,59,62,101,200,275,296,304,309,322,328};
    for(int i=0;i<(sizeof(l)/sizeof(int));i++){
        seccomp_rule_add(ctx,SCMP_ACT_KILL,l[i],0);
    }
    return seccomp_load(ctx);
}
int vuln(){
	char buff[64];
	gets(buff);
	return 0;
}
int main(int argc,char * argv[]){
    init();
    vuln();
    return 0;
}
