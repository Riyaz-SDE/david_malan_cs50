#include <stdio.h>

void meow(int n); // this is called as protyping
int get_positive_number(void);
int main(){
    printf("code working\n");
    int times = get_positive_number();
    meow(times);
    return 0;
}

int get_positive_number(){
    int input;
    do{
        printf("Enter Positive Number:");
        scanf("%d",&input);
    }while (input < 1);
    return input;
}
void meow(int n){
    for(int i = 0; i < n; i++){
        printf("%d meow\n",i);
    }
}
