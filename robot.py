# video of creation of this script at: https://asciinema.org/a/9479
# the goal was to write a script with nice theme,
# while being simple enough for a beginner to understand.

# video reveals that the design was refined all the time
# while working on the program.


has_head  = False
has_hands = False
has_legs  = False

head  = "        r   "
torso = "       ooo  "
groin = "        o   "
legs  = "       o o  "
hands = "      / o | "

def robot():
    if has_head:
        print(head)
    print(torso)
    if has_hands:
        print(hands)
    else:
        print(groin)
    if has_legs:
        print(legs)

print("Build a robot!")
print("In this game, you are an robot engineer.\n")

complete = False
while not complete:
    print("This is your robot:\n")
    robot()

    print("""
    Build:""")
    if not has_head:
        print("    1. head")
    if not has_hands:
        print("    2. hands")
    if not has_legs:
        print("    3. legs")

    part = input("? ")
    if not has_head and part == "1" or part.startswith("he"):
        print("\nYou build a head\n")
        has_head = True
    if not has_hands and part == "2" or part.startswith("ha"):
        print("\nYou build pair of hands\n")
        has_hands = True
    if not has_legs and part == "3" or part.startswith("l"):
        print("\nYou build pair of legs\n")
        has_legs = True

    complete = has_head and has_hands and has_legs

print("This is your robot:\n")
robot()
print("\nrobot: BEE BOOB, I AM A ROBOT!")
