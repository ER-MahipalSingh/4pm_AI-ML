#include <stdio.h>

void greet(){
    printf("Welcome");
};

void sum(int x, int y){
    printf("sum of x + y: %d", x + y);
};

int num(){
    return 10;
};

int multi(int a, int b){
    return a * b;
};

int fact(int n){
    if(n==1) return 1;
    return n * fact(n - 1);
}

int main(){
    // greet();
    // sum(10, 5);
    // int a = num();
    // printf("%d",a);

    // int res = multi(10,5);
    // printf("%d",res);

    int res = fact(5);
    printf("%d", res);
    return 0;
}