page_rules = {}
manuals = []

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

print(page_rules)