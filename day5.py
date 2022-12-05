### Preparation ###
number_of_stacks = 9 # hardcoded, sorry not sorry
stacks = [[] for i in range(number_of_stacks)] #list of n empty lists
stacks_part2 = [[] for i in range(number_of_stacks)] #list of n empty lists
position_generator = lambda x : x * 4 + 1 #used to get the stack index in the input
instructions = []
with open("day5input") as file:
    for line in file:
        line = line.replace("\n","").replace("\r","")
        if "move" not in line and "1" not in line:
            while len(line) < number_of_stacks * 4 - 1:
                line += " " #make all lines the same length
            for i in range(number_of_stacks):
                item = line[position_generator(i)]
                if item != " ":
                    stacks[i].append(item)
                    stacks_part2[i].append(item)
        elif "move" in line:
            instructions.append(line.replace("move ","").replace("from ","").replace("to ","").split(" "))

for instruction in instructions:
    count = int(instruction[0])
    from_stack = int(instruction[1]) - 1  # convert to 0 based index
    to_stack = int(instruction[2]) - 1  # convert to 0 based index
    for i in range(count):
        stacks[to_stack].insert(0, stacks[from_stack].pop(0))  # yes, my stacks are upside down. too bad. at least im making comments, Jelly >.>
for stack in stacks:
    print(stack[0], end="")
print()

for instruction in instructions:
    count = int(instruction[0])
    from_stack = int(instruction[1]) - 1  # convert to 0 based index
    to_stack = int(instruction[2]) - 1  # convert to 0 based index
    temp_stack = []
    for i in range(count):
        temp_stack.append(stacks_part2[from_stack].pop(0))
    for i in range(len(temp_stack)):
        stacks_part2[to_stack].insert(0,temp_stack.pop())

for stack in stacks_part2:
    print(stack[0], end="")

