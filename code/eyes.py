from astro_pi import AstroPi
import time
ap = AstroPi()

w = [150,150,150]
b = [0,0,255]
e = [0,0,0]

image = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
w,w,w,e,e,w,w,w,
w,w,b,e,e,w,w,b,
w,w,w,e,e,w,w,w,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e
]

ap.set_pixels(image)

while True:
    time.sleep(1)
    ap.flip_h()
