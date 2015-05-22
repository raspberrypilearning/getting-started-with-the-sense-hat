from astro_pi import AstroPi
ap = AstroPi()
import time

while True:
    pitch,roll,yaw = ap.get_orientation().values()
    print("pitch=%s,roll=%s.yaw=%s" % (pitch,yaw,roll))
    time.sleep(0.5)
