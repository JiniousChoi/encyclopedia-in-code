#include <stdio.h>
#include <stdlib.h>

int main() {
    system("ps -ef; sleep 10;");

    printf("Sleeping after system ends.\n");
    sleep(10);

    printf("Done.\n");
    exit(0);
}

