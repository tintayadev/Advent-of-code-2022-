# <<< Day 5: Supply stacks >>>

with open('./input/day5_input.txt') as file:
    stacks_data, steps = (i.splitlines() for i in file.read().strip("\n").split("\n\n"))

stacks = {int(n): [] for n in stacks_data[-1].replace(" ", "")}
indexes = [n for n, elem in enumerate(stacks_data[-1]) if elem != " "]
# print(stacks)


def displayStacks():
    print("\n\nStacks:\n")
    for stack in stacks:
        print(stack, stacks[stack])
    print("\n")

displayStacks()

def loadStacks():
    for elem in stacks_data[:-1]:
        stack_num = 1
        for n in indexes:
            if elem[n] != " ":
                stacks[stack_num].insert(0, elem[n])
            stack_num += 1

def emptyStacks():
    for stack_num in stacks:
        stacks[stack_num].clear()

def getStackEnds():
    answer = ""
    for stack in stacks:
        answer += stacks[stack][-1]
    return(answer)

loadStacks()
displayStacks()

for step in steps:
    step = step.replace("move", "").replace("from ", "").replace("to ", "").strip().split(" ")
    step = [int(i) for i in step]
    print(step)

    crates = step[0]
    from_stack = step[1]
    to_stack = step[2]

    for crate in range(crates):
        crate_removed = stacks[from_stack].pop()
        stacks[to_stack].append(crate_removed)

displayStacks()

# Answer part 1
print(getStackEnds())
print("===================================")

emptyStacks()
loadStacks()
displayStacks()



for step in steps:
    step = step.replace("move", "").replace("from ", "").replace("to ", "").strip().split(" ")
    step = [int(i) for i in step]

    crates = step[0]
    from_stack = step[1]
    to_stack = step[2]

    crates_to_remove = stacks[from_stack][-crates:]
    # Deleting crates
    stacks[from_stack] = stacks[from_stack][:-crates]

    # To add crates to another stack
    for crate in crates_to_remove:
        stacks[to_stack].append(crate)


displayStacks()
#Answer part 2
print(getStackEnds())