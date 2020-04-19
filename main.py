from playsound import playsound
from gpiozero import Button
from signal import pause
import os

playsound("./WhoDisturbsMySlumber.wav")
print("Played sound.")

button = Button(2)

def shutdown():
    """
    Reboots on button press.
    """
    print("Button pressed.")
    os.system("sudo shutdown -r now")

button.when_pressed = shutdown

pause()