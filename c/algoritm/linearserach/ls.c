#include <stdio.h>

int main (){
    int number[] = {1,2,3,4,5};

    int serchElement;
    scanf("%d", &serchElement);

    for(int i = 0; i<5; i++){
        if(number[i] == serchElement){
            printf("number is there");
            return 0;
        }
    }
    printf("number not found");
    return 1;
}