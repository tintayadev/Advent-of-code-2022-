#   Day 2: paper, rocks, scissors

with open("./input/day2_input.txt") as file:
    turns = [i for i in file.read().strip().split('\n')]

# ---------------------------------------------
# LEFT VS RIGHT | OUT | RIGHT + RESULT = TOTAL
# ---------------------------------------------
# A vs X = DRAW = (1 + 3) = 4
# A vs Y = WIN  = (2 + 6) = 8
# A vs Z = LOSS = (3 + 0) = 3
# B vs X = LOSS = (1 + 0) = 1
# B vs Y = DRAW = (2 + 3) = 5
# B vs Z = WIN  = (3 + 6) = 9
# C vs X = WIN  = (1 + 6) = 7
# C vs Y = LOSS = (2 + 0) = 2
# C vs Z = DRAW = (3 + 3) = 6

results = {
    "A X":4, "A Y":8, "A Z":3, 
    "B X":1, "B Y":5, "B Z":9, 
    "C X":7, "C Y":2, "C Z":6 
}

total_score = 0
for turn in turns:
    total_score += results[turn]

# Respuesta parte 1
print(total_score)

wanted_results = {
    "A X":3, "A Y":4, "A Z":8, 
    "B X":1, "B Y":5, "B Z":9, 
    "C X":2, "C Y":6, "C Z":7 
}

total_score = 0
for turn in turns:
    total_score += wanted_results[turn]

# Respuesta parte 2
print(total_score)