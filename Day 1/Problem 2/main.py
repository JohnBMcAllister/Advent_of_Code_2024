list1 = {}
list2 = []
similarityScore = 0



#For each line split the integers and append them to seperate lists
with open("input.txt", "r") as file:
        for line in file:
                x = line.split()
                list1[int(x[0].strip())] = 0
                list2.append(int(x[1].strip()))

for i in range(len(list2)):
        if list2[i] in list1:
                list1[list2[i]] += 1

for i in list1.keys():
        similarityScore += i * list1[i]

print(list1)
print(similarityScore)




