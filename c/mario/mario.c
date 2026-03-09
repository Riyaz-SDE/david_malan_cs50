#include <stdio.h>

int get_number();
int main(void){
    int x = get_number();
    int y = get_number();
    printf("division %f\n", x / y);
    printf("addition %d\n", x + y);
    return 0;
}

int get_number(void){
    int input;
    do{
        printf("Enter Number:");
        scanf("%d",&input);
    }while(input < 1);
    return input;
}