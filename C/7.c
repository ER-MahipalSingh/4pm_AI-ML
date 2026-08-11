#include <stdio.h>

int main(){
    // int num = 11;
    // (num % 2 == 0) ? printf("Even Number") : printf("Odd Number");

    // int a = 100, b = 200, c = 30;
    // int res = (a > b) ? (a > c ? a : b) : (b > c ? b : c);
    // printf("Bigger value is: %d", res);


    int a, b;
    char op;

    printf("Enter first number: ");
    scanf("%d", &a);

    printf("Enter second number: ");
    scanf("%d", &b);

    printf("Enter operator (+,/,-,*): ");
    scanf(" %c", &op);

    switch(op){
        case '+':
            printf("a + b is: %d", a + b);
            break;
        case '-':
            printf("\na - b is: %d", a - b);
            break;
        case '*':
            printf("\na * b is: %d", a * b);
            break;
        case '/':
            printf("\na / b is: %d", a / b);
            break;
        default:
            printf("\nInvalid operator");
            break;
    }
}