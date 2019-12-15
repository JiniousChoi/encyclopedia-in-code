#include <stdio.h>

int main(int argcount, char **arglist) {
	int i;
	printf("argcount: %d\n", argcount);
	for(i=0; i<argcount; i++) {
		printf("argvalue: %s\n", arglist[i]);
	}
}
