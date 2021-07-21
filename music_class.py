#mad lib game.
#you add a random word where prompted. A paragraph is then printed out using these random words, can be very funny.
verb = input("verb: ")
verb2 = input("verb: ")
verb3 = input("verb: ")
verb4 = input("verb: ")
verb5 = input("verb: ")
verb6 = input("verb: ")
noun = input("noun: ")
noun2 = input("noun: ")
noun3 = input("noun: ")
noun4 = input("noun: ")
noun5 = input("noun: ")
noun6 = input("noun: ")
adj = input("adjective: ")
adj2 = input("adjective: ")
adj3 = input("adjective: ")
instrument = input("name a musical instrument: ")
instrument2 = input("name a musical instrument: ")
animal = input("name an animal: ")

#using string concatenation the paragraph will be returned with the new inputted words in it.
music_class = f"Make some noise in music class... I like music class because we get to {verb} and {verb2} really loudly.
There are all sorts of {noun} to play, like the {adj} {noun2} and the {noun3}. My instrument is the {adj2} {instrument},
which sounds a lot like a {animal}. We are learning to {verb3} a song by The {noun4} called, I {verb4} to {verb5} with You,
using {instrument2} and {noun5}. When we all {verb6} together, it sounds like a {adj3} group of {noun6}."

print(music_class)