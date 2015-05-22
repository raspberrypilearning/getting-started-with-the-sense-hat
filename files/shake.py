from astro_pi import AstroPi
ap = AstroPi()
import time

while True:
  x,y,z = ap.get_accelerometer_raw().values()

  x=abs(x)
  y=abs(y)
  z=abs(z)

  if x > 1 or y > 1 or z>1:
      ap.show_letter("!",text_colour=[255,0,0])
  else:
      ap.clear()
  time.sleep(0.1
