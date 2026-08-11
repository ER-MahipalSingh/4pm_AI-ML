#include <stdio.h>

int main()
{
    char a = 'g';
    char b[] = "Paython Developer";
    char str[5] = {'a', 'g', 'l', 'B', '\0'};

    // printf("%c", a);
    // printf("\n%s", b);
    // printf("\n%s ", str);

    // for(int i=0; str[i] != '0'; i++){
    //     printf("%c ",str[i]);
    // }


    // char tech[100];

    // printf("Enter tech stack: ");
    // scanf("%s", &tech);
    // fgets(tech, 100, stdin);

    // printf("%s", tech);
    // puts(tech);

    for(char i='A'; i<='Z'; i++){
        printf("%c ", i);
    }

    return 0;
}