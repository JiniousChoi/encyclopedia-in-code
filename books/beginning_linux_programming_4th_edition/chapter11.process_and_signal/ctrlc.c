#include <signal.h>
#include <stdio.h>
#include <unistd.h>

typedef void (*sighandler_t)(int);

void oops(int sig) {
    printf("OOPS! by %d\n", sig);
}

void ouch(int sig) {
    printf("OUCH! - I got signal %d\n", sig);
    (void) signal(SIGINT, SIG_DFL);
}

int main() {
    sighandler_t old_handler1, old_handler2;

    old_handler1 = signal(SIGINT, oops);
    // Segmentation fault (core dumped) due to calling SIG_DFL directly in userland
    // old_handler1(2); 

    old_handler2 = signal(SIGINT, ouch);
    old_handler2(2);

    while(1) {
        printf("Hello World!\n");
        sleep(1);
    }
}
