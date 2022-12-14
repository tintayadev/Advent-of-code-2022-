# <<< Day 3: Rucksack Reorganization >>>

from string import ascii_letters
#   Obteniendo la data
with open('./input/day3_input.txt') as file:
    data = [i for i in file.read().strip().split("\n")]


#   Iterando en el archivo
total_sum = 0
for rucksack in data:

    half = len(rucksack)//2

    left = set(rucksack[:half])
    right = set(rucksack[half:])

    for priority, char in enumerate(ascii_letters):
        if char in left and char in right:
            total_sum += priority + 1

#  Respuesta parte 1
print(total_sum)

j = 3
total_sum = 0
for i in range(0, len(data), 3):
    rucksacks = data[i:j]
    j += 3

    # print(rucksacks)

    for priority, char in enumerate(ascii_letters):
        if char in rucksacks[0] and char in rucksacks[1] and char in rucksacks[2]:
            total_sum += priority + 1
# Respuesta parte 2
print(total_sum)