from cs50 import get_string

inputx = get_string("what is your name ")
print(f'hi {inputx}')

def printf(input,endline,sep):
    print(input,end = endline,sep = sep)
printf('riyaz', '----\t --- \n','*')

def add2numm():
    x = int(input("type : x")) 
    y = int(input("type : y"))
    print(x + y)
    printf("sum of two num is", '\t finished ','*')
add2numm()