#include <fcntl.h>
#include <unistd.h>
#include <stddef.h>
#include <errno.h>
#include <sys/prctl.h>
#include <linux/audit.h>
#include <linux/seccomp.h>
#include <linux/filter.h>
#include <linux/unistd.h>
#include <stdlib.h>
#include <stdio.h>

static int seccomp_configuration(int nr,int arch,int error){
    struct sock_filter filter[] = {
        BPF_STMT(BPF_LD + BPF_W + BPF_ABS, (offsetof(struct seccomp_data, arch))),
        BPF_JUMP(BPF_JMP + BPF_JEQ + BPF_K, arch, 0, 3),
        BPF_STMT(BPF_LD + BPF_W + BPF_ABS, (offsetof(struct seccomp_data, nr))),
        BPF_JUMP(BPF_JMP + BPF_JEQ + BPF_K, nr, 0, 1),
        BPF_STMT(BPF_RET + BPF_K, SECCOMP_RET_ERRNO | (error & SECCOMP_RET_DATA)),
        BPF_STMT(BPF_RET + BPF_K, SECCOMP_RET_ALLOW),
    };
    struct sock_fprog prog = {
       .len = (unsigned short)(sizeof(filter) / sizeof (filter[0])),
       .filter = filter,
    };
    if (prctl(PR_SET_NO_NEW_PRIVS, 1, 0, 0, 0)) {
        perror("prctl(NO_NEW_PRIVS)");
        return 1;
    }
    if (prctl(PR_SET_SECCOMP, 2, &prog)) {
        perror("prctl(PR_SET_SECCOMP)");
        return 1;
    }
}
int main(){
    
    char buff[60];
    gets(buff);
    seccomp_configuration(__NR_execve, AUDIT_ARCH_X86_64, EPERM);
    seccomp_configuration(__NR_fork, AUDIT_ARCH_X86_64, EPERM);
    //execve("/bin/sh",0,0);
}