import re

def find_Mull_Occurances(sequence):
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    matches = re.findall(pattern, sequence)

    return matches

