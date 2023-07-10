with open("Day2/input.txt", "r") as f:
    data = f.readlines()

opponent = {
    "A": ["Y", "rock"],
    "B": ["Z", "paper"],
    "C": ["X", "scissors"]
}

own_play = {
    "X": [1, "rock"],
    "Y": [2, "paper"],
    "Z": [3, "scissors"]
}

conclusions = {
    "win": 6,
    "draw": 3,
    "lose": 0
}

points = 0
for item in data:
    plays = item.replace("\n", "").split(" ")
    points += own_play.get(plays[1])[0]

    if plays[1] == opponent.get(plays[0])[0]:
        points += conclusions.get("win")

    elif own_play.get(plays[1])[1] == opponent.get(plays[0])[1]:
        points += conclusions.get("draw")

    else:
        points += conclusions.get("lose")

print(points)
        