from playsound import playsound
from gpiozero import Button
from signal import pause

playsound("./WhoDisturbsMySlumber.wav")

button = Button(2)

def shutdown():
    """
    Pretends to shut down.
    """
    print("Button pressed.")

button.when_pressed = shutdown

pause()