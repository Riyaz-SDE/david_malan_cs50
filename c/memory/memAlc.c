#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>

int main(){
    char string1[11] = "sksoakoska";
    printf("%c - end\n",*(string1));
    printf("%c - end\n",*(string1+9));
    printf("%c - Last Null Value\n",*(string1+10));

    // cpoying existing string 
    char input[50];
    scanf("%s",input);
    printf("%s - %d end\n", input, strlen(input));
    // char* clone = *input; this wont work
    char *clone = malloc(strlen(input)+1);
    if(clone == NULL) return 1;
    //coping method

    // for(int i = 0, n = strlen(input); i<=n; i++){
    //     // *(clone + n) = *(input + n); //or
    //     clone[n] = input[n];
    // } // instead of this use strcpy
    strcpy(clone, input);
    printf("%s - end\n",clone);
}