#include <stdio.h>
// #include <f
/**
 * CRUD
 * fopen - opening file
 * fclose - close
 */

 int main(){
    FILE *fileName = fopen("abc.csv","a");
    // work on logic if file doesnt exist exit
    if( fileName == NULL) return 1;
    char inputString[50];
    printf("Type Input String : ");
    scanf("%s",inputString);
    int inputNumber;
    printf("Type Input Numbe : ");
    scanf("%d", inputNumber);
    fprintf(fileName,"name : %s, Number : %d\n",inputString,inputNumber);
    fclose(fileName);
 }