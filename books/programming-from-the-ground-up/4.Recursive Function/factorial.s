.section .data

.section .text

.globl _start

.globl factorial

_start:

	pushl $4
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

	#$ebx * factorial($ecx)
	#$eax = factorial($ecx)
	movl 8(%ebp), %ecx
	decl %ecx
	cmpl $1, %ecx
	je cond2
	
cond1:
	pushl %ecx
	call factorial
	addl $4, %esp

	movl 8(%ebp), %ebx
	imull %ebx, %eax
	jmp end_factorial

cond2:
	movl 8(%ebp), %ebx
	movl %ebx, %eax
	#jmp end_factorial

end_factorial:
	movl %ebp, %esp
	popl %ebp
	ret
