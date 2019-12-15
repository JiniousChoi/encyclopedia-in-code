.section .data

.section .text
.globl _start

_start:
	movl $1, %eax	#this is the linux kernel command
					#number (system call) for exiting a program
	movl $7, %ebx	#status number we will return to the os. Programmer cna define what number to return

	int $0x80		#this wakes up the kernel to run the exit command
