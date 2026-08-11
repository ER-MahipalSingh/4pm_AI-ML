#include <stdio.h>

int main()
{
    // int marks = 90;

    // if (marks >= 1 && marks <= 100){
    //     if (marks > 80){
    //         printf("Grade A");
    //     }
    //     else if (marks > 60){
    //         printf("Grade B");
    //     }
    //     else if (marks > 45){
    //         printf("Garde C");
    //     }
    //     else if (marks > 33){
    //         printf("Garde D");
    //     }
    //     else{
    //         printf("fail");
    //     }
    // }else{
    //     printf("Invalid marks");
    // }

    // int username = 004;
    // int password = 1234;

    // if(username == 004 && password == 123){
    //     if(password == 1234){
    //         printf("Login Done");
    //     }else{
    //         printf("Login failed");
    //     }
    // }else{
    //     printf("Invalid username");
    // }


    int a = 25;
    int b = 20;
    int c = 30;

    if(a > b){
        if(a > c){
            printf("A is bigger");
        }else{
            printf("C is bigger > first");
        }
    }else{
        if(b > c){
            printf("B is bigger");
        }else{
            printf("C is bigger > second");
        }
    }
}