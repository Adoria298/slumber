# slumber

Raspberry Pi project used to make the Pi play the famous "Who Disturbs My Slumber?" line from Disnery's Aladdin at the push of a button. Line Copyright Disney.

I have set this up with a simple button in a breadboard connected to GPIO pin #2. `cron` then runs `main.py` at boot, piping output into `main.py.log`.