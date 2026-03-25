#include <stdio.h>
#include "triangle.h"

int main(void) {
    double a,b,c;
    printf("Введите а: ");
    scanf("%lf", &a);
    printf("Введите b: ");
    scanf("%lf", &b);
    printf("Введите c: ");
    scanf("%lf", &c);
    if (a>0 && b>0 && c>0 && a+b>c && a+c>b && b+c>a) {
        printf("Периметр =  %lf \n", triangle_per(a,b,c));
        printf("Площадь = %lf", triangle_area(a,b,c));
    } else {
        printf("Стороны не подходят");
    }
    return 0;
}
