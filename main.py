from gpiozero import Button
from signal import pause
import os

os.system("mplayer WhoDisturbsMySlumber.wav")
print("Played sound.")

button = Button(2)

def shutdown():
    """
    Reboots on button press.
    """
    print("Button pressed. Rebooting.")
    os.system("sudo shutdown -r now")

button.when_pressed = shutdown

pause()