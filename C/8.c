#include <stdio.h>

int main(){
    for(int i = 1; i < 1; i++){
        printf("%d ", i);
    }

    printf("\n------\n");

    int i = 1;
    while(i < 1){
        printf("%d ", i);
        i++;
    }

    printf("\n------\n");

    int j = 1;
    do{
        printf("%d ", j);
        j++;
    }while(j < 1);

}