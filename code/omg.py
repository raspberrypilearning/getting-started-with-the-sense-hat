from astro_pi import AstroPi
import time

ap = AstroPi()

ap.show_letter("O",text_colour=[255,0,0])
time.sleep(1)
ap.show_letter("M",text_colour=[0,0,255])
time.sleep(1)
ap.show_letter("G",text_colour=[0,255,0])
time.sleep(1)
ap.show_letter("!",text_colour=[0,0,0],back_colour=[255,255,255])
time.sleep(1)
ap.clear()
