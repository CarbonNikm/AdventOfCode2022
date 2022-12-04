
### Preparation ###
demo = False # set to true if printing out info for someone else to look at
left_side = []
right_side = []
both_sides_since_part_2_needs_that_now = []
with open("day3input") as file:
    for line in file:
        line = line.strip()
        left_side.append(line[0:int(len(line)/2)]) # get left half of array
        right_side.append(line[int(len(line)/2):]) # get right half of array
        both_sides_since_part_2_needs_that_now.append(line)
print(left_side)
print(right_side)
print(both_sides_since_part_2_needs_that_now)

### Demo and explanation for part 1 and 2 ###
if demo:
    left_set = set(left_side[0]) # convert to set
    right_set = set(right_side[0]) # convert to set
    print(left_set & right_set) # shows the single letter that matches in the sets
    letter_value = ord(list(left_set & right_set)[0]) # extracts the letter of interest, and gives it the unicode value
    print(letter_value) # shows the number
    priority = letter_value - 96 if letter_value > 95 else letter_value - 64 + 26 # converts the unicode value to 1-26 or 27-52, according to the prompt
    print(priority) # shows the priority

### Part 1 ###
sum = 0
for i in range(len(left_side)):
    letter_value = ord(list( set(left_side[i]) & set(right_side[i]) )[0])
    sum += letter_value - 96 if letter_value > 95 else letter_value - 64 + 26
print(sum) # part 1 answer

### Part 2 ###
sum = 0
group_counter = 0
for i in range(int(len(both_sides_since_part_2_needs_that_now)/3)): #iterates through a third of the list since we pull 3 elements each time
    first = set(both_sides_since_part_2_needs_that_now[i * 3])
    second = set(both_sides_since_part_2_needs_that_now[i * 3 + 1])
    third = set(both_sides_since_part_2_needs_that_now[i * 3 + 2])
    letter_value = ord(list(first & second & third)[0])
    sum += letter_value - 96 if letter_value > 95 else letter_value - 64 + 26
print(sum)