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
}
int secc(){
	scmp_filter_ctx ctx;
    ctx = seccomp_init(SCMP_ACT_ALLOW);
    int l [2] = {1,59};
    for(int i=0;i<(sizeof(l)/sizeof(int));i++){
        seccomp_rule_add(ctx,SCMP_ACT_KILL,l[i],0);
    }
    return seccomp_load(ctx);
}
int vuln(){
	FILE * fd1;
	FILE * fd2;
	char flag[50];
	char blacklist[50];
	fd1 = fopen("flag.txt","r");
	if(fd1==NULL){
		printf("[!] flag file doesn't exist [!]\n");
		exit(-1);
	}
	fd2 = fopen("blacklist.txt","rw");
	if(fd2==NULL){
		printf("[!] blacklist file doesn't exist [!]\n");
		exit(-1);
	}
	fscanf(fd1,"%s",&flag);
	fscanf(fd2,"%s",&blacklist);
	char buff[64];
	printf("What's the next name in the blacklist ?\n");
	gets(buff);
	return 0;
}
int main(int argc,char * argv[]){
    init();
    vuln(argv[1]);
    secc();
    return 0;
}
