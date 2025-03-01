lat = open("latitude.csv", "r")
output = open("cordinates.txt","w")

lat.readline()
output.write("var dataPoints = [\n")

for line in lat:
    addend = "{x:"
    parts = line.split(",")
    addend += parts[1] + ", "

    addend += "y:"
    
    countryName = parts[-1]
    countryName = countryName.replace("\n", "")

    pc = open("parsed_cases.csv", "r")
    pc.readline()

    for line2 in pc:
        if countryName in line2:
            xVal = line2.split(",")[-1]
            xVal = xVal.replace("\n", "")
            addend += xVal
            addend += ", name:\"" + countryName
            addend += "\"},\n"
            output.write(addend)
            break
output.write("]")