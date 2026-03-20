#include <stdio.h>
int main(void) {
    double matrix[3][3];
    int a=0,b=0;
    printf("Введите значения матрицы 3х3:");
    for(int i=0;i<3;i++){
        for(int j=0;j<3;j++){
            scanf("%lf", &matrix[i][j]);
    }
        }
    for (int i = 0; i<3; i++){
        a += matrix[i][i];
        b += matrix[i][2-i];
    }
    printf("Сумма главной диагонали %d\n", a);
    printf("Сумма поб диагонали %d\n", b);
    int matrix1[2][2];
    int a1=0,b1=0,c;
    printf("Введите значения матрицы 2x2:");
    for(int i1 = 0; i1<2; i1++){
        for(int j1=0;j1<2;j1++){
            scanf("%d", &matrix1[i1][j1]);
        }
    }
    for (int i2 = 0; i2<2; i2++){
        a1 += matrix1[i2][i2];
        b1 += matrix1[i2][1-i2];
    }
    c = pow((a1+b1),2);
        
    printf("квадрат матрицы 2х2: %d \n", c);
    return 0;
}
