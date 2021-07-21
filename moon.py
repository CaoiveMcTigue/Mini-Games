#mad lib game.
#you add a random word where prompted. A paragraph is then printed out using these random words, can be very funny.
num = input("enter a number: ")
num2 = input("enter a number: ")
num3 = input("enter a number: ")
num4 = input("enter a number: ")
noun = input("plural noun: ")
noun2 = input("plural noun: ")
noun3 = input("noun: ")
noun4 = input("noun: ")
adj = input("Adjective: ")
adj2 = input("Adjective: ")
adj3 = input("Adjective: ")
place = input("enter a place: ")
first_name = input("enter a first name: ")
first_name2 = input("enter a first name: ")
verb = input("verb ending in -ed: ")
verb2 = input("verb ending in -ed: ")
verb3 = input("verb ending in -ed: ")
verb4 = input("verb ending in -ed: ")
verb5 = input("verb ending in -ed: ")
verb6 = input("verb: ")
verb7 = input("verb: ")
adverb = input("adverb: ")

#using string concatenation the paragraph will be returned with the new inputted words in it.
moon_landing_madlibs = f"The Moon Landing... On July {num} 1969, two american {noun} were the first to {verb6} on the moon.
This {adj} trip took {num2} days to reach the moon from {place}. As {first_name} Armstrong and {first_name2} Aldrin {verb} onto 
the {noun3} of the moon, Armstrong {verb2} the famous words, That's {num3} {adj2} step for man, one {adj3} for mankind.
Soon after, Aldrin {verb3} onto the moon and together, they {verb4} a U.S. {noun4} on the surface. They {verb5} {noun2} from
the moon's surface to {verb7} back to Earth and {adverb} returned home {num4} days later."

print(moon_landing_madlibs)