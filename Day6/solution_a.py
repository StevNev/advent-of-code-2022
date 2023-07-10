with open("Day6/input.txt", "r") as f:
    data = f.read()

first_marker = 0
for i in range(0, len(data)):
    found_letters = []
    if first_marker== 0:
        found_letters.append(data[i])
        found_letters.append(data[i+1])
        found_letters.append(data[i+2])
        found_letters.append(data[i+3])
        found_letters = set(found_letters)
        if len(found_letters) == 4:
            first_marker = i+4
    else:
        break

print(first_marker)