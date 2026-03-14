#include <stdio.h>
void swap(int *a, int *b);
int main(){
    int a;
    int b;
    printf("Type input A in number : ");
    scanf("%d",&a);
    printf("Type input B in number : ");
    scanf("%d",&b);
    printf("value of a is %d and b is %d\n",a,b);
    printf("after variable swapped\n");
    swap(&a,&b);
    printf("value of a is %d and b is %d\n",a,b);
}

void swap(int* a, int* b){
    int temp;
    temp = *a;
    *a = *b;
    printf("%d a\n",*a);
    *b = temp;
    printf("%d b\n",*b);
    printf("%d and %d\n",*a,*b);
}