peoples = [{
    "name" : 'arif',
    "number" : '+91-9176256365'
},{
    "name" : 'riyaz',
    "number" : '+91-176071978'
},{
    "name" : 'cd',
    "number" : '+91-917352353'
}]

name = input("Enter name of person ")
for people in peoples:
    if people["name"] == name:
        print(f'name found and the number is {people["number"]}')
        break
else:
    print('name not found')