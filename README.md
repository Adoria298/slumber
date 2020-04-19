# slumber

Raspberry Pi project used to make the Pi play the famous "Who Disturbs My Slumber?" line from Disnery's 
Aladdin at the push of a button. Line Copyright Disney.

I have set this up with a simple button in a breadboard connected to GPIO pin #2. I use a systemd service 
to automatically run `main.py` at boot (once sound has been loaded).

## Dependencies

`slumber` uses `playsound` (`pip3 install playsound`), which in turn relies on `gstreamer`. Depending on your setup, the following tools may need to be installed for `slumber` to work (given as an all-in-one `apt` command - modify for your own uses).
- `sudo apt install python-gst-1.0 gstreamer1.0-plugins-good gstreamer1.0-plugins-ugly gstreamer1.0-tools python3-gst-1.0`
