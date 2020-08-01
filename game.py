
locations = {0: "You are sitting in front of a computer learning Python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are inside a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}

exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},
         2: {"N": 5, "Q": 0},
         3: {"W": 1, "Q": 0},
         4: {"N": 1, "W": 2, "Q": 0},
         5: {"W": 2, "S": 1, "Q": 0}}

named_exits = {1: {"2": 2, "3": 3, "4": 4, "5": 5},
               2: {"5": 5},
               3: {"1": 1},
               4: {"1": 1, "2": 2},
               5: {"2": 2, "1": 1}}
wordsUsed = {"WEST": "W",
             "EAST": "E",
             "NORTH": "N",
             "SOUTH": "S",
             "QUIT": "Q",
             "ROAD": "1",
             "HILL": "2",
             "BUILDING": "3",
             "VALLEY": "4",
             "FOREST": "5"}
# print(locations[0].split())
# print(locations[3].split(","))
# print(' '.join(locations[0].split()))
loc = 1
while True:
    availableExits = ", ".join(exits[loc].keys())
    # print(availableExits)
    print(locations[loc])

    if loc == 0:
        break
    else:
        allExits = exits[loc].copy()
        allExits.update(named_exits[loc])

    direction = input("Available exits are " + availableExits + ": ").upper()
    print()
    # Parse user input using wordsUsed dict
    if len(direction) > 1:
        words = direction.split()
        for word in words:
            if word in wordsUsed:
                direction = wordsUsed[word]
                break
        # for word in wordsUsed:
        #     if word in direction:
        #         direction = wordsUsed[word]

    if direction in allExits:
        loc = allExits[direction]
    else:
        print("You cannot go in that direction")
