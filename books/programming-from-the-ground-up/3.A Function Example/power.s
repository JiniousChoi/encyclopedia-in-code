#PURPOSE:	Program to illustrate how functions work
#			This program will compute the value of
#			2^3 + 5^2
#
.section .data

.section .text

.globl _start

_start:
#1st FN call
	pushl $3
	pushl $2
	call power
	addl $8, %esp

#store
	#%ebx=2^3
	pushl %eax

#2nd FN call
	pushl $2
	pushl $5
	call power
	addl $8, %esp

#Add ret1 + ret2
	#%eax=5^2
	popl %ebx
	#eax + ebx --> ebx
	addl %eax, %ebx

#end_main
	movl $1, %eax
	int $0x80


.type power, @function
power:
#stack initialize
	pushl %ebp
	movl %esp, %ebp
	subl $4, %esp

#for 1:initialize
	movl 8(%ebp), %ebx
	movl 12(%ebp),%ecx
	movl %ebx, -4(%ebp)

#for 2:condition check
power_loop_start:
	cmpl $1, %ecx
	jle end_power
	movl -4(%ebp), %eax

	imull %ebx, %eax
	movl %eax, -4(%ebp)

#for 3:index update
	decl %ecx
	jmp power_loop_start

end_power:
	#return value
	movl -4(%ebp), %eax

	#restore stack
	movl %ebp, %esp
	popl %ebp
	ret
