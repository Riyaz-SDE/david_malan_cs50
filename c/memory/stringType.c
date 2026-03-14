#include <stdio.h>

typedef char* string;
int main(){

    string name = "HI I AM RIYAZ";
    // scanf("%s", name); 
    printf("%s\n", name);
    printf("%c\n", *name);
    printf("%c\n", *(name+1));
}