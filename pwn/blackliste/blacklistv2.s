	.file	"blacklistv2.c"
	.text
	.globl	init
	.type	init, @function
init:
.LFB6:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	subq	$48, %rsp
	movq	stdout(%rip), %rax
	movl	$0, %ecx
	movl	$2, %edx
	movl	$0, %esi
	movq	%rax, %rdi
	call	setvbuf@PLT
	movq	stdin(%rip), %rax
	movl	$0, %ecx
	movl	$2, %edx
	movl	$0, %esi
	movq	%rax, %rdi
	call	setvbuf@PLT
	movq	stderr(%rip), %rax
	movl	$0, %ecx
	movl	$2, %edx
	movl	$0, %esi
	movq	%rax, %rdi
	call	setvbuf@PLT
	movl	$2147418112, %edi
	call	seccomp_init@PLT
	movq	%rax, -16(%rbp)
	movl	$56, -48(%rbp)
	movl	$57, -44(%rbp)
	movl	$58, -40(%rbp)
	movl	$59, -36(%rbp)
	movl	$62, -32(%rbp)
	movl	$101, -28(%rbp)
	movl	$200, -24(%rbp)
	movl	$322, -20(%rbp)
	movl	$0, -4(%rbp)
	jmp	.L2
.L3:
	movl	-4(%rbp), %eax
	cltq
	movl	-48(%rbp,%rax,4), %edx
	movq	-16(%rbp), %rax
	movl	$0, %ecx
	movl	$0, %esi
	movq	%rax, %rdi
	movl	$0, %eax
	call	seccomp_rule_add@PLT
	addl	$1, -4(%rbp)
.L2:
	movl	-4(%rbp), %eax
	cmpl	$7, %eax
	jbe	.L3
	movq	-16(%rbp), %rax
	movq	%rax, %rdi
	call	seccomp_load@PLT
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE6:
	.size	init, .-init
	.section	.rodata
.LC0:
	.string	"r"
.LC1:
	.string	"flag.txt"
	.align 8
.LC2:
	.string	"[!] flag file doesn't exist [!]"
	.align 8
.LC3:
	.string	"What's the next name in the blacklist ?"
	.text
	.globl	vuln
	.type	vuln, @function
vuln:
.LFB7:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	subq	$80, %rsp
	leaq	.LC0(%rip), %rsi
	leaq	.LC1(%rip), %rdi
	call	fopen@PLT
	movq	%rax, -8(%rbp)
	cmpq	$0, -8(%rbp)
	je	.L6
	leaq	.LC2(%rip), %rdi
	call	puts@PLT
.L6:
	leaq	.LC3(%rip), %rdi
	call	puts@PLT
	leaq	-80(%rbp), %rax
	movq	%rax, %rdi
	movl	$0, %eax
	call	gets@PLT
	movl	$0, %eax
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE7:
	.size	vuln, .-vuln
	.globl	main
	.type	main, @function
main:
.LFB8:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	subq	$16, %rsp
	movl	%edi, -4(%rbp)
	movq	%rsi, -16(%rbp)
	movl	$0, %eax
	call	init
	movq	-16(%rbp), %rax
	addq	$8, %rax
	movq	(%rax), %rax
	movq	%rax, %rdi
	movl	$0, %eax
	call	vuln
	movl	$0, %eax
	leave
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE8:
	.size	main, .-main
	.ident	"GCC: (Debian 9.3.0-14) 9.3.0"
	.section	.note.GNU-stack,"",@progbits
