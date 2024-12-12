import re

sequence = []
subsequence = []
result = []
combined = 0
enable = r'do\(\)'
disable = r'don\'t\(\)'


def create_subsequence(sequence):
    # Join all lines into a single string
    sequence_str = ''.join(sequence)

    # Find all matches for "do()" and "don't()"
    do_position = [match.start() for match in re.finditer(enable, sequence_str)]
    dont_position = [match.start() for match in re.finditer(disable, sequence_str)]
    subsequences = []
    last_position = 0

    # Find the first subsequence between the start and the first "don't()" in the sequence
    if dont_position:
        first_dont = dont_position[0]
        subsequences.append(sequence_str[:first_dont])
        last_position = first_dont

    # Process subsequent "do()" and "don't()" matches
    for do in do_position:
        if do > last_position:
            next_dont = next((pos for pos in dont_position if pos > do), len(sequence_str))
            subsequences.append(sequence_str[do:next_dont])
            last_position = next_dont

    return subsequences


def find_Mull_Occurances(sequence):
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    matches = re.findall(pattern, sequence)

    return [(int(a) * int(b)) for a, b in matches]

# Read the input file
with open('input.txt', 'r') as file:
    for line in file:
        sequence.append(line.strip())  # Strip newline characters

# Create subsequences
subsequences = create_subsequence(sequence)

# Process each subsequence
for line in subsequences:
    result.append(find_Mull_Occurances(line))

# Combine the results
for x in result:
    for y in x:
        combined += y

print(combined)