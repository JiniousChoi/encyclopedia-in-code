#include<stdio.h>
#include<string.h>
#include<stdlib.h>

int main(int argc, char** argv){
	char* buffer = (char *) malloc(100);
	char* datafile = (char *) malloc(20);
	strcpy(datafile, "/var/notes");
	
	strcpy(buffer, argv[1]);
	
	printf("[DEBUG] buffer	@ %p: \'%s\'\n", buffer, buffer);	
	printf("[DEBUG] datafile@ %p: \'%s\'\n", datafile, datafile);	

	free(buffer);
	free(datafile);
}
