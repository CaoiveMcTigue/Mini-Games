#mad lib game.
#you add a random word where prompted. A paragraph is then printed out using these random words, can be very funny.

adj1 = input("Adjective: ")
adj2 = input("Adjective: ")
bird = input("type of bird: ")
room = input("room in a house: ")
verb = input("past tense verb: ")
verb2 = input("verb: ")
name = input("name: ")
noun = input("noun: ")
liquid = input("name a liquid: ")
verb3 = input("verb ending in -ing: ")
body-part = input("plural body part: ")
noun2 = input("plural noun: ")
verb4 = input("verb ending in -ing: ")
noun3 = input("noun: ")

#using string concatenation the paragraph will be returned with the new inputted words in it.
madlibs = f"It was a {adj1}, cold November day. I woke up to the {adj2} smell of {bird} roasting in the {room} downstairs.I {verb} down the stairs to see if I could help {verb2} the dinner. My mom said, See if {name} needs a fresh {noun}. 
So I carried a tray of glasses full of {liquid} into the {verb3} room. When I got there, I couldn't believe my {body-part}!
There were {noun2} {verb4} on the {noun3}!"

print(madlibs)
