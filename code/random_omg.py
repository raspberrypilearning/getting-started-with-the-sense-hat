from astro_pi import AstroPi
import time
import random

ap = AstroPi()

r = random.randint(0,255)
ap.show_letter("O",text_colour=[r,0,0])
time.sleep(1)

r = random.randint(0,255)
ap.show_letter("M",text_colour=[0,0,r])
time.sleep(1)

r = random.randint(0,255)
ap.show_letter("G",text_colour=[0,r,0])
time.sleep(1)

ap.show_letter("!",text_colour=[0,0,0],back_colour=[255,255,255])
time.sleep(1)
ap.clear()
