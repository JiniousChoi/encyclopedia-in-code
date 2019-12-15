.section .data

.section .text

.globl _start

.globl factorial

_start:

	pushl $5
	call factorial
	addl $4, %esp

	#return %ebx
	movl %eax, %ebx

end_main:
	movl $1, %eax
	int $0x80


.type factorial, @function
factorial:
	pushl %ebp
	movl %esp, %ebp

	movl 8(%ebp), %eax
	cmp $1, %eax
	je end_factorial

	decl %eax
	pushl %eax
	call factorial
	addl $4, %esp

	imull 8(%ebp), %eax

end_factorial:
	movl %ebp, %esp
	popl %ebp

	ret #%eax
