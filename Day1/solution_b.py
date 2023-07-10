with open("Day1/input.txt", "r") as f:
    data = f.read()

list = data.split("\n")


total = 0
totals_list = []
for item in list:
    if item != "":
        total += int(item)
    else:
        totals_list.append(total)
        total = 0

totals_list.sort(reverse=True)

print(totals_list[0] + totals_list[1] + totals_list[2])