#include <stdio.h>
// implement structure
// funtion like push pop size
#define MAX_SIZE 5
typedef struct
{
    int items[MAX_SIZE];
    int top
} stack;

void intStact(stack *s){
    s -> top = -1;
}
int isEmpty(stack *s){
    if(s->top == -1) return 0;
}
int main(){

}