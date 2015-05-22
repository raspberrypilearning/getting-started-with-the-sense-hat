# Software installation

Connect your Astro Pi HAT and boot up the Pi.

## Astro Pi driver installation

Ensure your Pi is connected to the internet, then run the following command (from the command prompt or a Terminal window) to download and start the Astro Pi installation script:

```bash
wget -O - http://www.raspberrypi.org/files/astro-pi/astro-pi-install.sh --no-check-certificate | bash
```

This will take about 5 minutes on a Pi 2 and about 15 to 20 minutes on a Pi 1.

When it's finished you'll see the following message:

```
You must reboot to complete the Astro Pi installation
Type:
sudo reboot
and press Enter when ready
```

Reboot the Pi to complete the installation:

```bash
sudo reboot
```

The rainbow pattern on the LED matrix should now turn off during boot up.
