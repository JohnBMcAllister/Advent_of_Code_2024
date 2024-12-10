list1 = {}
list2 = []


#Open the file
file = open("input.txt", "r")

#For each line split the integers and append them to seperate lists
for line in file:
        x = line.split()
        list1[x[0].strip()] = 0
        list2.append(int(x[0].strip()))

file.close()

list2.sort()

print("Length of list 1: ", len(list1))
print("Length of list 2: ", len(list2))


