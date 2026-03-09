#include <stdio.h>
#include <string.h>
int stringLen(char name [50]);
char getString ();
int main(void) {
    char name[50];
    printf("Name : ");
    scanf("%s", name);
    int strlen = stringLen(name);
    printf("\n%i\n",strlen);
    return 0;
}

int stringLen(char name [50]){
    
    int n = 0;
    while(name[n] != '\0' ){
        if( n > 20) {
            printf("line breaked here inside function \n");
            break;
        };
        printf("line not breaked here inside function %c after increment n is", name[n]);
        n++;
        printf("%i\n ",n);
    }
    return n;
    
}
// char getString (){
//     char name[50] = "hiop";
//     return name;
// };
// char name[50];
// printf("Name : ");
// scanf("%s", name);
// int strlen = stringLen(name);
// printf("\n%i\n",strlen);