import csv

with open("favorites.csv","r") as file:
    reader = csv.DictReader(file)
    next(reader) # it skips the row
    # scratch, c, python = 0, 0, 0
    count = {}
    for row in reader:
        favorites = row["language"]
        if favorites in count:
            count[favorites] += 1
        else:
            count[favorites] = 1
        # if favorite == "Scratch":
        #     scratch += 1
        # elif favorite == "Python":
        #     python +=1
        # elif favorite == "C":
        #     c += 1
# print(scratch,python,c)
for favorite in sorted(count,key = count.get, reverse=True):
    print(f'{favorite} : {count[favorite]}')
print(count)