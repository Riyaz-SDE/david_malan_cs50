try:
    x = int(input("Enter the Number: "))
    print("its an integer")
except ValueError:
    print("Not an Integer")
else:
    print("will works when not fail")
finally: 
    print('wil works every time')