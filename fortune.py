#exercise 1 on page 85.
#fortune cookies
#jca 06-05-2011

import random

print("I'm cracking open your fortune cookie and reading what's inside.\n")
print("Your fortune is . . . ")
keepgoing = "y"
while keepgoing == "y":
    #Generate our random number from 1 to 5. Moved this inside while loop.
    fortune_index = random.randint(1, 5)
    if fortune_index == 1:
        print("\n\tMany Bothan spies died to bring you this fortune.")
    elif fortune_index == 2:
        print("\n\tConfucious say, \"Delicious hotdog not always so delicious.\"")
    elif fortune_index == 3:
        print("\n\tPants on the ground.")
    elif fortune_index == 4:
        print("\n\tThere's a jellybean in your future.")
    elif fortune_index == 5:
        print("\n\tLatin is like a cheeseburger.")
    else:
        print("This condition can never happen. How are you seeing this?")
    keepgoing = input("\nIf you want me to open another, type y. ")

#input("Press enter to continue.")
