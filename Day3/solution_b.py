with open("Day3/input.txt", "r") as f:
    data = f.readlines()

split_lists = []

for i in range(0, len(data), 3):
    split_lists.append([
        data[i].replace("\n", ""), 
        data[i+1].replace("\n", ""), 
        data[i+2].replace("\n", "")
    ])

priority_total = 0
for item in split_lists:
    common = list(set(item[0]).intersection(item[1]).intersection(item[2]))[0]
    if common.isupper():
        priority_total += (ord(common) - 38)
    else:
        priority_total += (ord(common) - 96)

print(priority_total)