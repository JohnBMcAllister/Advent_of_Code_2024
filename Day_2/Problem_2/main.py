reports = []
safetyList = []
safeReports = 0

def is_safe(row):
    inc = [row[i + 1] - row[i] for i in range(len(row) - 1)]
    if set(inc) <= {1, 2, 3} or set(inc) <= {-1, -2, -3}:
        return True
    return False

with open("input.txt", "r") as file:
    for line in file:
        reports.append([int(x) for x in line.split()])

# Iterate through the list of reports
for i in range(len(reports)):
    safe = False
    # First check if the report is safe as it is
    if is_safe(reports[i]):
        safe = True
    else:
        # Then, try removing one element at a time to see if the sequence becomes safe
        for j in range(len(reports[i])):
            modified_report = reports[i][:j] + reports[i][j + 1:]
            if is_safe(modified_report):
                safe = True
                break

    # Append result based on safety check
    safetyList.append("Safe" if safe else "Unsafe")

# Count the number of safe reports
safeReports = safetyList.count("Safe")

# Output the total number of safe reports
print(safeReports)