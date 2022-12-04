stdin = [0]
with open("day1input") as file:
    for line in file:
        print(line)
        if line == "\n":#newline means next index
            stdin.append(0)
            continue
        stdin[-1] += (int(line.strip()))
print(stdin)
print(sorted(stdin)[-1]) #answer 1
print(sum(sorted(stdin)[-3:])) #answer 2