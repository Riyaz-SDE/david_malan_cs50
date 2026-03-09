#include <stdio.h>
#include <string.h>

int main(){
    char string[50];

    scanf("%s", string);
    printf("input %s \n", string);
    printf("output : ");
    for(int i = 0,n = strlen(string); i < n; i++){
        if(string[i] >= 'a' && string[i] <= 'z'){
            string[i] = string[i] - 32;
        }
        printf("%c - %i ", string[i],string[i]);
    }
    printf("\n");
}