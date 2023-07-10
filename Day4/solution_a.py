with open("Day4/input.txt", "r") as f:
    data = f.readlines()

assignments = []
for item in data:
    elf1, elf2 = item.replace("\n", "").split(",")
    elf1 = elf1.split("-")
    elf2 = elf2.split("-")
    assignments.append([elf1, elf2])


total = 0
for pairing in assignments:
    elf1 = []
    elf2 = []

    for i in range(int(pairing[0][0]), int(pairing[0][1])+1):
        elf1.append(i)

    for i in range(int(pairing[1][0]), int(pairing[1][1])+1):
        elf2.append(i)

    elf1 = set(elf1)
    elf2 = set(elf2)

    common = elf1.intersection(elf2)
    if common == elf1 or common == elf2:
        total += 1

print(total)