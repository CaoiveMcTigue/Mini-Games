#selects a madlib from the four different ones I've created at random
from madlibs import madlibs.py, beach.py, moon.py, music_class.py
import random

if __name__ == "__main__":
    m = random.choice([madlibs.py, beach.py, moon.py, music_class.py])
    m.madlibs()