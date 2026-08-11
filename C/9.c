#include <stdio.h>

int main()
{
    for (int i = 1; i <= 5; i++)
    {
        printf(" i = %d: ", i);
        for (int j = 1; j <= 5; j++)
        {
            printf("j = %d, ", j);
        }
        printf("\n");
    }

    printf("\n*************\n");

    int i = 1;
    while (i <= 5)
    {
        int j = 1;
        while (j <= 5)
        {
            printf("%d ", j);
            j++;
        }
        printf("\n");
        i++;
    }

    printf("\n*************\n");

    int k = 1;
    do
    {
        int j = 1;
        do
        {
            printf("%d ", j);
            j++;
        } while (j <= 5);
        printf("\n");
        k++;
    } while (k <= 5);
}