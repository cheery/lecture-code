import random
# from 101 BASIC computer games
# in this video I translate it to python:
# https://asciinema.org/a/9480

# by watching how it was created, it can be easier
# to understand why programming constructs if / while 
# are used to control program flow. Thinking about difficult
# things is also itself, quite good exercise.

# structured programming theory goes:
#   every program written in goto soup has a structured
#   equivalent, that is easier to understand.
#   

print("THIS IS A GAME OF >>>>>>>>>>>RUSSIAN ROULETTE")

while 1:
    print("\nHERE IS A REVOLVER")

    victory = False
    while not victory:
        print("HIT ´1´ TO SPIN CHAMBER AND PULL TRIGGER.")
        print("      (HIT ´2´ TO GIVE UP)")
        print("GO") 
        misses = 0
        choice = int(input())
        while choice != 2:
            misses = misses + 1
            # one bullet in one of the six chambers.
            if random.random() > (1.0 - 1.0 / 6): 
                print("     BANG!!!!  YOU´RE DEAD!")
                print("CONDOLENCES WILL BE SENT TO YOUR RELATIVES. ")
                break

            # the chance is 0.83333 to not bite a bullet..
            # 0.83333 to power 10 is the chance to win, therefore.
            # 16% chance to win.
            if misses>10:
                victory = True

            print("- CLICK -\n")
            choice = int(input())

        if choice==2:
            print("      CHICKEN!!!")
        if not victory:
            print("\n\n\n\n...NEXT VICTIM... ")

    print("YOU WIN !!!")
    print("LET SOMEONE ELSE BLOW HIS BRAINS OUT. ")
