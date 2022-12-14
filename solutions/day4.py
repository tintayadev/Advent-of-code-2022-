# <<< Day 4: Camp Cleanup >>>

#   Obteniendo la data
with open('./input/day4_input.txt') as file:
    data = [i for i in file.read().strip().split("\n")]

sum = 0

for elem in data:
    
    first, second = map(str, elem.split(",")) 

    first = [int(i) for i in first.split("-")]
    second = [int(i) for i in second.split("-")] 
    print(first, second)

    if first[0] <= second[0] and first[1] >= second[1]:
        sum += 1
    elif second[0] <= first[0] and second[1] >= first[1]:
        sum += 1

#Respuesta parte 1
print(sum)

sum = 0
for elem in data:
    
    first, second = map(str, elem.split(",")) 

    first = [int(i) for i in first.split("-")]
    second = [int(i) for i in second.split("-")] 

    if first[0] in range(second[0], second[1]+1) or first[1] is range(second[0], second[1]+1):
        sum += 1
    elif second[0] in range(first[0], first[1]+1) or second[1] is range(first[0], first[1]+1):
        sum += 1
# Respuesta parte 2
print(sum)

