#include <stdio.h>

int main()
{
    // for (int i = 1; i <= 5; i++)
    // {
    //     printf("i = %d: ", i);
    //     for (int j = i; j <= 5; j++)
    //     {
    //         printf("%d ", j);
    //     }
    //     printf("\n");
    // }

    // for (int i = 1; i <= 5; i++){
    //     printf("i = %d: ", i);
    //     for (int j = 1; j <= i; j++)
    //     {
    //         printf("%d ", j);
    //     }
    //     printf("\n");
    // }

    // for (int i = 2 - 1; i <= 5 + 1; i++){
    //     for (int j = i + 1; j <= 5 + 1; j++)
    //     {
    //         printf("%d ", j);
    //     }
    //     printf("\n");
    // }

    for(int i = 1; i <= 10; i++){
        // printf("%d ", i);
        if(i == 8){
            continue;
        }
        printf("%d ", i);
    }
}