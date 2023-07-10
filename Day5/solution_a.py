with open("Day5/input.txt", "r") as f:
    data = f.readlines()

with open("Day5/instructions.txt") as f:
    instructions = f.readlines()

stacks = []

for i in range(0,9):
    stacks.append([])

i = 0
for line in data:
    if i != len(data)-1:
        stacks[0].append(line[1])
        stacks[1].append(line[5])
        stacks[2].append(line[9])
        stacks[3].append(line[13])
        stacks[4].append(line[17])
        stacks[5].append(line[21])
        stacks[6].append(line[25])
        stacks[7].append(line[29])
        stacks[8].append(line[33])
    i +=1

for i in range(0, len(stacks)):
    
    stacks[i].reverse()
    keep = []
    for item in stacks[i]:
        if item != " ":
            keep.append(item)
    stacks[i] = keep


for line in instructions:
    components = line.replace("\n", "").split(" ")
    amount = int(components[1])
    source = int(components[3])-1
    dest = int(components[5])-1
    
    for i in range(1, amount+1):
        stacks[dest].append(stacks[source][-i])

    stacks[source] = stacks[source][:len(stacks[source]) - amount]

stack_tops = []

for stack in stacks:
    stack_tops.append(stack[-1])

print(stack_tops)