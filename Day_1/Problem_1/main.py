
# Initialize the variable
list1 = []
list2 = []
total_distance = 0

#Open the file
file = open("input.txt", "r")

#For each line split the integers and append them to seperate lists
for line in file:
        x = line.split()
        list1.append(int(x[0]))
        list2.append(int(x[1]))

file.close()

#Sort the lists
list1.sort()
list2.sort()

for i in range(len(list1)):
    total_distance += abs(list1[i] - list2[i])

print(f"Total distance is: {total_distance}")


