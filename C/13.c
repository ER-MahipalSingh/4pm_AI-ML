#include <stdio.h>

int main()
{
    int arr[7][5] = {
        {10, 20, 30, 40},
        {100, 200, 300}
    };

        arr[1][3] = 400;
        arr[2][2] = 2000;
    
    int row = sizeof(arr) / sizeof(arr[0]);
    int col = sizeof(arr[0]) / sizeof(arr[0][0]);
    printf("row = %d",row);
    printf("\ncol = %d",col);

    printf("\n-----------\n");

    for (int i = 0; i < row; i++){
        for (int j = 0; j < col; j++)
        {
            printf("%d ", arr[i][j]);
        }
        printf("\n");
    }

    return 0;
}