from astro_pi import AstroPi
ap = AstroPi()

while True:
    t = ap.get_temperature()
    p = ap.get_pressure()
    h = ap.get_humidity()

    t = round(t,1)
    p = round(p,1)
    h = round(h,1)

    msg = "Temperature = %s, Pressure=%s, Humidity=%s" % (t,p,h)

    ap.show_message(msg,scroll_speed=0.05)
