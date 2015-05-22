from astro_pi import AstroPi
ap = AstroPi()
import time

ap.show_letter("J")

while True:
  x,y,z = ap.get_accelerometer_raw().values()

  x=round(x,0)
  y=round(y,0)

  if x == -1:
      ap.set_rotation(180)
  elif y == 1:
      ap.set_rotation(90)
  elif y == -1:
      ap.set_rotation(270)
  else:
      ap.set_rotation(0)

  time.sleep(0.1)
