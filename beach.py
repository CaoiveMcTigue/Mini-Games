#mad lib game.
#you add a random word where prompted. A paragraph is then printed out using these random words, can be very funny.
adj = input("Adjective: ")
adj2 = input("Adjective: ")
adj3 = input("Adjective: ")
noun = input("noun: ")
noun1 = input("noun: ")
noun2 = input("plural noun: ")
verb = input("verb: ")

#using string concatenation the paragraph will be returned with the new inputted words in it.
beach_madlibs = f"A day at the beach... Yesterday, I went to the beach. I had such a fun time! When I arrived to the beach
I could not help but notice the {adj} sand. My friend loved my {adj2} bathing suit I was wearing. I looked at the ocean 
and could not believe my eyes! I saw {noun3} swimming around! I wanted to go swimming with them but I was afraid they
were going to {verb} me! Instead I decided to build a {noun} castle. I used a shovel, spade, and {noun2} to help me build it.
The sun started to set,and it was time to go home. I had the {adj3} time at the beach!"

print(beach_madlibs)