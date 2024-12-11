reports = []
safetyList = []
safeReports = 0

with open("input.txt", "r") as file:
    for line in file:
        reports.append([int(x) for x in line.split()])

# Iterate through the list of reports
for i in range(len(reports)):

    # Check If report is increasing or decreasing or neither
    if reports[i] == sorted(reports[i]):
        # Assume the report is safe
        safe = True

        # Check if the difference between two consecutive indexes
        for j in range(len(reports[i]) - 1):
            # If difference is out of range, mark report as unsafe break loop
            if not (1 <= (reports[i][j + 1] - reports[i][j]) <= 3):
                safe = False
                break

        # Append "Safe" or "Unsafe" based on eval
        if safe:
            safetyList.append("Safe")
        else:
            safetyList.append("Unsafe")

    # Check if current report is descending
    elif reports[i] == sorted(reports[i], reverse=True):
        # Same process as above
        safe = True

        for j in range(len(reports[i]) - 1):
            if not (1 <= (reports[i][j] - reports[i][j + 1]) <= 3):
                safe = False
                break

        if safe:
            safetyList.append("Safe")
        else:
            safetyList.append("Unsafe")

    # If report is neither ascending or descending, mark it unsafe
    else:
        safetyList.append("Unsafe")


# Count the number of safe reports
safeReports = safetyList.count("Safe")

# Output the total number of safe reports
print(safeReports)
