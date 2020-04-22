from gpiozero import Button
from signal import pause
import os

path = os.abspath("./WhoDisturbsMySlumber.wav")
os.system("mplayer " + path)
print("Played sound.")

button = Button(2)

def shutdown():
    """
    Shuts down on button press.
    """
    print("Button pressed. Rebooting.")
    os.system("sudo shutdown now")

button.when_pressed = shutdown

pause()
