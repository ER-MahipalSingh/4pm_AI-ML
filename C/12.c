#include <stdio.h>

int main()
{
    // int arr[5] = {10, 20, 30, 40, 50};

    // printf("%d", arr[4]);

    // arr[3] = 500;

    // for (int i = 0; i < 5; i++)
    // {
    //     printf("%d ", arr[i]);
    // }

    int size;

    printf("Enter arr size: ");
    scanf("%d", &size);

    int arr[size];

    for (int i = 0; i < size; i++){
        printf("Enter arr element: ");
        scanf(" %d", &arr[i]);
    }

    for(int i=0; i<size; i++){
        printf("%d ", arr[i]);
    }

    return 0;
}