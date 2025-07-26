# Install an external module and use it to perform an operation of your interest

import pyttsx3 as pt
engine = pt.init()
engine.say('''Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.''')
engine.runAndWait()