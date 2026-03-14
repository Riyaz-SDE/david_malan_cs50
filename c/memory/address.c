#include<stdio.h>

int main(){
    int number = 50;
    int *numberAddress = &number; // pointer pointing variable number
    printf("This is number : %d\n", number);
    printf("This is pointer of number: %p\n", numberAddress);
    return 0;
}