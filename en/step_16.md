## Detecting movement

The Sense HAT has a set of sensors that can detect movement. It has an IMU (inertial measurement unit) chip which includes:

- A gyroscope (for detecting which way up the board is)
- An accelerometer (for detecting movement)
- A magnetometer (for detecting magnetic fields)

Before you start experimenting with motion sensing, it's important to understand three key terms covered in the [guide](https://github.com/raspberrypilearning/astro-pi-guide/blob/master/sensors/movement.md) and in this [video](https://www.youtube.com/watch?v=pQ24NtnaLl8).

The three axes uses to describe motion are:

- Pitch (like a plane taking off)
- Roll (the plane doing a victory roll)
- Yaw (imagine steering the plane like a car)

![Sense HAT Orientation](images/orientation.png)

The IMU sensor is not yet supported on trinket.io, but will be coming soon!
You can find out the orientation of the Sense HAT using the `sense.get_orientation()` method:

```python
orientation = sense.get_orientation()
pitch = orientation['pitch']
roll = orientation['roll']
yaw = orientation['yaw']
```

This would get the three orientation values (measured in degrees) and store them as the three variables `pitch`, `roll` and `yaw`.

- You can explore these values with a simple program:

```python
from sense_hat import SenseHat

sense = SenseHat()

while True:
    orientation = sense.get_orientation()
    pitch = orientation['pitch']
    roll = orientation['roll']
    yaw = orientation['yaw']
    print("pitch={0}, roll={1}, yaw={}".format(pitch,yaw,roll))
```

- Click **File** -- **Save As**, give your program a name e.g. [`orientation.py`](resources/orientation.py), then press **F5** to run.

    **Note: When using the movement sensors it is important to poll them often in a tight loop. If you poll them too slowly, for example with `time.sleep(0.5)` in your loop, you will see strange results. This is because the code behind needs lots of measurements in order to successfully combine the data coming from the gyroscope, accelerometer and magnetometer.**

- Another way to detect orientation is to use the `sense.get_accelerometer_raw()` method which tells you the amount of g-force acting on each axis. If any axis has ±1g then you know that axis is pointing downwards.

    In this example, the amount of gravitational acceleration for each axis (x, y, and z) is extracted and is then rounded to the nearest whole number:

    ```python
    from sense_hat import SenseHat

    sense = SenseHat()

    while True:
	    acceleration = sense.get_accelerometer_raw()
        x = acceleration['x']
		y = acceleration['y']
		z = acceleration['z']

        x=round(x, 0)
        y=round(y, 0)
        z=round(z, 0)

        print("x={0}, y={1}, z={2}".format(x, y, z))
    ```

- Click **File** -- **Save As**, give your program a name e.g. [`acceleration.py`](resources/acceleration.py), then press **F5** to run.

    As you turn the screen you should see the values for x and y change between -1 and 1. If you place the Pi flat or turn it upside down, the z axis will be 1 and then -1.

- If we know which way round the Raspberry Pi is, then we can use that information to set the orientation of the LED matrix. First you would display something on the matrix, then continually check which way round the board is, and use that to update the orientation of the display.

    ```python
    from sense_hat import SenseHat

    sense = SenseHat()

    sense.show_letter("J")

    while True:
        x = sense.get_accelerometer_raw().['x']
		y = sense.get_accelerometer_raw().['y']
		z = sense.get_accelerometer_raw().['z']

        x = round(x, 0)
        y = round(y, 0)

        if x == -1:
            sense.set_rotation(180)
        elif y == 1:
            sense.set_rotation(90)
        elif y == -1:
            sense.set_rotation(270)
        else:
            sense.set_rotation(0)
    ```

- Click **File** -- **Save As**, give your program a name e.g. [`rotating_letter.py`](resources/rotating_letter.py), then press **F5** to run.

    In this program you are using an `if, elif, else` structure to check which way round the Raspberry Pi is. The `if` and `elif` test three of the orientations, and if the orientation doesn't match any of these then the program assumes it is the "right" way round. By using the `else` statement we also catch all those other situations, like when the board is at 45 degrees or sitting level.

- If the board is only rotated, it will only experience 1g of acceleration in any direction; if we were to shake it, the sensor would experience more than 1g. We could then detect that rapid motion and respond. For this program we will introduce the `abs()` function which is not specific to the Sense HAT library and is part of standard Python. `abs()` gives us the size of a value and ignores whether the value is positive or negative. This is helpful as we don't care which direction the sensor is being shaken, just that it is shaken.

    ```python
    from sense_hat import SenseHat

    sense = SenseHat()

    while True:
	    acceleration = sense.get_accelerometer_raw()
        x = acceleration['x']
		y = acceleration['y']
		z = acceleration['z']
        
        x = abs(x)
        y = abs(y)
        z = abs(z)

        if x > 1 or y > 1 or z > 1:
            sense.show_letter("!", text_colour=[255, 0, 0])
        else:
            sense.clear()
    ```

- Click **File** -- **Save As**, give your program a name e.g. [`shake.py`](resources/shake.py), then press **F5** to run.

    You might find this is quite sensitive, but you could change the value from 1 to a higher number.

### Ideas

  - You could write a program that displays an arrow (or other symbol) on screen; this symbol could be used to point to which way is down. This way the astronauts (in low gravity) always know where the Earth is.
  - You could improve the dice program from earlier in this activity, so that shaking the Pi triggers the dice roll.
  - You could use the accelerometer to sense small movements; this could form part of a game, alarm system or even an earthquake sensor.

