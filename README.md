# slumber

Raspberry Pi project used to make the Pi play the famous "Who Disturbs My Slumber?" line from Disnery's 
Aladdin when it boots. Line Copyright Disney. Also creates a shutdown button.

I have set this up with a simple button in a breadboard connected to GPIO pin #2 and the GND pin. I use a systemd service to automatically run `main.py` at boot (once sound has been loaded).

## Dependencies

`slumber` uses `mplayer` to play sound, which can be installed with `sudo apt install mplayer`. See `man mplayer` for its documentation. `slumber` must be run on a Linux system - it is designed for the 
Raspberry Pi, and has been tested on the Pi 3B.
