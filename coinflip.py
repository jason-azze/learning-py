#coin flip exercise p.85
#jca 06-05-2011

import random

#Init a counter for total number of flips.
flipcount = 0
#Create a place to store our heads and tails counts.
headscount = 0
tailscount = 0
while flipcount < 100:
    #Init a var that will randomly be 0 or 1.
    flipvalue = random.randrange(2)    
    #Evaluate the flips for heady- or tailyness
    if flipvalue == 0:
        headscount += 1
    elif flipvalue == 1:
        tailscount += 1
    flipcount += 1

#When the while loop ends, print our results.
print("There were " , headscount , "heads and " , tailscount , "tails.")

input("\n\nPress enter to continue.")
