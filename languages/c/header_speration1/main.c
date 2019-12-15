#include <stdio.h>

extern int MUL(int, int);

int main(char **argv, int argc) {
    int x=3,y=4;
    int z= MUL(x,y);
    printf("%d*%d=%d\n", x,y,z);
    return 0;
}
