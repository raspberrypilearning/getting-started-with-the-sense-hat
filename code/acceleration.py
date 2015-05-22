from astro_pi import AstroPi
ap = AstroPi()
import time

while True:
  x,y,z = ap.get_accelerometer_raw().values()

  x=round(x,0)
  y=round(y,0)
  z=round(z,0)

  print("x=%s,y=%s.z=%s" % (x,y,z))
  time.sleep(0.1)
