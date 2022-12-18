# <<< Day 6: Tunning trouble >>>

with open('./input/day6_input.txt') as file:
    input = file.read()


for i in range(4, len(input)):
    cad = input[(i-4) : i]
    string = set(cad)
    if len(string) == 4:
        # Answer part 1
        print(string, i)
        break


for i in range(14, len(input)):
    cad = input[(i-14) : i]
    string = set(cad)
    if len(string) == 14:
        # Answer part 2
        print(string, i)
        break
