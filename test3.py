#include <stdio.h>

int main(void) {
    int a;

    printf("Введите число: ");
    scanf("%d", &a);

    if (a % 2 == 0) {
        printf("Even\n");
    } else {
        printf("Odd\n");
    }

    return 0;
}
