w = open("parsed_cases.csv", "w")
r = open("cases.csv", "r")
r.readline
for line in r:
    if "2025-02-09" in line:
        w.write(line)