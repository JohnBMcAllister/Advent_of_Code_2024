import re

sequence = []
result = []
combined = 0

def find_Mull_Occurances(sequence):
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    matches = re.findall(pattern, sequence)
    print("Pairs: ", matches)

    return [(int(a) * int(b)) for a, b in matches]

with open('input.txt', 'r') as file:
    for line in file:
        sequence.append(line)

for line in sequence:
    result.append(find_Mull_Occurances(line))

for x in result:
    for y in x:
        combined += y

print (combined)

