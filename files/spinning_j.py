from astro_pi import AstroPi
import time

ap = AstroPi()

ap.show_letter("J")

for r in (0,90,180,270,0,90,180,270):
    ap.set_rotation(r)
    time.sleep(0.5)
