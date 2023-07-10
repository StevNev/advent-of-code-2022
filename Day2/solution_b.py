with open("Day2/input.txt", "r") as f:
    data = f.readlines()

opponent = {
    "A": {
        "Z": "paper",
        "Y": "rock",
        "X": "scissors"
    },
    "B": {
        "Z": "scissors",
        "Y": "paper",
        "X": "rock"
    },
    "C": {
        "Z": "rock",
        "Y": "scissors",
        "X": "paper"
    }
}

own_play = {
    "rock": 1,
    "paper": 2,
    "scissors": 3
}

conclusions = {
    "X": 0,
    "Y": 3,
    "Z": 6
}

points = 0
for item in data:
    plays = item.replace("\n", "").split(" ")
    points += conclusions.get(plays[1])
    # print(own_play.get(opponent.get(plays[0]).get(plays[1])))
    points += own_play.get(opponent.get(plays[0]).get(plays[1]))




print(points)
        