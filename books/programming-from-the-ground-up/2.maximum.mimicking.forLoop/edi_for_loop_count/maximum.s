.section .data
data_items:
	.long 17, 66, 32, 132, 247, 132, 42, 34, 23, 125, 22, 123, 23, 0, 188, 25
.section .text

.globl _start

#for(i=0; data_items[i] != 0; i++){ ... }
_start:
	movl $0, %edi
	movl data_items(,%edi,4), %eax
	movl %eax, %ebx

loop_condition:
	cmpl $15, %edi
	je _exit_loop

#_loopbody:
	cmpl %ebx, %eax
	jle _index_update
	movl %eax, %ebx

_index_update:
	incl %edi
	movl data_items(,%edi,4), %eax
	jmp loop_condition 
	
_exit_loop:
	movl $1, %eax
	int $0x80
