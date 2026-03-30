
def compare_number(a,b):
    if a == b:
        return "number are same"
    elif a > b:
        return f'number {a} must be greater than {b}'
    else:
        return f'number {b} must be greater than {a}'
def agree(option,flag=False):
    if flag:
        option = input('type valid input like yes or no ')
    
    option = option.lower()

    if option not in ['y','yes','n','no']:
        return agree(None,True)
    
    if option in ["y","yes"]:
        print('d1')
        return True
    elif option in ["n", "no"]:
        print('d2')
        return False
    print('d3')

x = int(input("enter number x: "))
y = int(input("enter number y: "))
result = compare_number(x,y)
print(result)
z = input("type your ans ")
print(agree(z))
