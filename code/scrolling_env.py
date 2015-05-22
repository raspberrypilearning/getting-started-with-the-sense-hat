from astro_pi import AstroPi
ap = AstroPi()

while True:
    t = ap.get_temperature()
    p = ap.get_pressure()
    h = ap.get_humidity()

    t = round(t,1)
    p = round(p,1)
    h = round(h,1)

    if t > 18.3 and t< 26.7:
        bg = [0,100,0] #green
    else:
        bg = [100,0,0] #red

    msg = "Temperature = %s, Pressure=%s, Humidity=%s" % (t,p,h)

    ap.show_message(msg,scroll_speed=0.05,backcolour=bg)
