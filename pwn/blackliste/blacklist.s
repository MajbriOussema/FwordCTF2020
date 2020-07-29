	.file	"blacklist.c"
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
	subq	$96, %rsp
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
	movl	$1, -96(%rbp)
	movl	$2, -92(%rbp)
	movl	$18, -88(%rbp)
	movl	$20, -84(%rbp)
	movl	$56, -80(%rbp)
	movl	$57, -76(%rbp)
	movl	$58, -72(%rbp)
	movl	$59, -68(%rbp)
	movl	$62, -64(%rbp)
	movl	$101, -60(%rbp)
	movl	$200, -56(%rbp)
	movl	$275, -52(%rbp)
	movl	$296, -48(%rbp)
	movl	$304, -44(%rbp)
	movl	$309, -40(%rbp)
	movl	$322, -36(%rbp)
	movl	$328, -32(%rbp)
	movl	$0, -4(%rbp)
	jmp	.L2
	popq	%r9
	ret
.L3:
	movl	-4(%rbp), %eax
	cltq
	movl	-96(%rbp,%rax,4), %edx
	movq	-16(%rbp), %rax
	movl	$0, %ecx
	movl	$0, %esi
	movq	%rax, %rdi
	movl	$0, %eax
	call	seccomp_rule_add@PLT
	addl	$1, -4(%rbp)
.L2:
	movl	-4(%rbp), %eax
	cmpl	$16, %eax
	jbe	.L3
	movq	-16(%rbp), %rax
	movq	%rax, %rdi
	call	seccomp_load@PLT
	leave
	.cfi_def_cfa 7, 8
	ret
	popq	%r8
	ret
	popq	%r10
	ret
	.cfi_endproc
.LFE6:
	.size	init, .-init
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
	subq	$64, %rsp
	leaq	-64(%rbp), %rax
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
