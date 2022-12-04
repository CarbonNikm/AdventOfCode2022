their_hands = []
my_hands = []
with open("day2input") as file:
    for line in file:
        their_hands.append(line[0])
        my_hands.append(line[2])
print(their_hands)
print(my_hands)
# A     B     C
# X     Y     Z
#Rock Paper Scissors
static_points = {"X":1, "Y":2, "Z":3, "A":1, "B":2, "C":3}


### begin part 1 ###

def score(their_hand, my_hand):
    their_hand = static_points[their_hand] #convert hand to number
    my_hand = static_points[my_hand] #convert hand to number
    if their_hand == my_hand: #draw
        return my_hand + 3
    if (their_hand - my_hand == -1 or their_hand - my_hand == 2): #win
        return my_hand + 6
    if (their_hand - my_hand == 1 or their_hand - my_hand == -2): #|  ||  ||  |_
        return my_hand

total_score = 0
for i in range(len(their_hands)):
    total_score = total_score +  score(their_hands[i],my_hands[i])
print(total_score)

### end part 1 ###

### begin part 2 ###

def translate_hand_then_get_score(their_hand, outcome):
    their_hand = static_points[their_hand] #convert hand to number
    outcome = static_points[outcome] #convert hand to number
    if outcome == 2: #draw (but said in McRee's voice, this time)
        return their_hand + 3
    if outcome == 1: #we need to lose to decrease suspicion
        if their_hand == 1:
            return 3
        if their_hand == 2:
            return 1
        else:
            return 2
    else: #heh. nice try, kid
        if their_hand == 1:
            return 8
        if their_hand == 2:
            return 9
        if their_hand == 3:
            return 7

total_score = 0
for i in range(len(their_hands)):
    total_score = total_score + translate_hand_then_get_score(their_hands[i], my_hands[i])
print(total_score)

### end part 2 ###