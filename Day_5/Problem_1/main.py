page_rules = {}
manuals = []
count = 0

with open("input.txt", "r") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        if "|" in line:
            x, y = map(int, line.split("|"))
            if x not in page_rules:
                page_rules[x] = []
            page_rules[x].append(y)

        if "," in line:
            sequence = [int(x) for x in line.split(",")]
            manuals.append(sequence)

for x in range(len(manuals)):
    for y in range(len(manuals[x])):
        if y == 0:
            continue
        cur = manuals[x][y]
        prev = manuals[x][:y]

        for prev in prev:
            if cur in page_rules and prev in page_rules[cur]:
                continue
            else:
                count += 1

print("page rules: ", page_rules)
print("manuals: ", manuals)
print("count: ", count)