#include <stdio.h>
#include <math.h>
int main(void) {
    int n;
    while (n != 0) {
        double a,b,c;
        double x1,x2,d;
        d = pow(b, 2) - 4*a*c;
        printf("Введите а: ");
        scanf("%lf", &a);
        printf("Введите b: ", b);
        scanf("%lf", &b);
        printf("Введите c: ", c);
        scanf("%lf", &c);
        if (d<0){
            printf("корней нет");
        } else{
            x1 = (-b + pow(d, 1/2)) / (2*a);
            x2 = (-b - pow(d, 1/2)) / (2*a);
        }
        printf("x1 %lf\n",x1);
        printf("x2 %lf\n",x2);
        printf("продолжнить программу? 1-да , 0-нет: ");
        scanf("%d", &n);
        
        
    }
    return 0;
}
