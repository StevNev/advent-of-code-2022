with open("Day3/input.txt", "r") as f:
    data = f.readlines()

split_lists = []

for item in data:
    split_lists.append([item[:int(len(item)/2)], item[int(len(item)/2):]])


priority_total = 0
for item in split_lists:
    common = list(set(item[0]).intersection(item[1]))[0]
    print(common, ord(common))
    if common.isupper():
        priority_total += (ord(common) - 38)
    else:
        priority_total += (ord(common) - 96)

print(priority_total)