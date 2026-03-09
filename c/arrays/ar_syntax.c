#include<stdio.h>
int main(){
    const int N = 3;
    int scores[N];
    scores[0] = 80;
    scores[1] = 95;
    scores[2] = 100;
    int result = 0;
    for(int i = 0; i<3; i++){
        result += scores[i];
    }
    printf("%f", result / 3.00);
    return 0;
}