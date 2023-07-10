with open("Day6/input.txt", "r") as f:
    data = f.read()

first_marker = 0
for i in range(0, len(data)):
    found_letters = []
    if first_marker== 0:
        for x in range(0,14):
            found_letters.append(data[i+x])
        found_letters = set(found_letters)
        if len(found_letters) == 14:
            first_marker = i+14
    else:
        break

print(first_marker)