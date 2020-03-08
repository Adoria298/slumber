from playsound import playsound
from gpiozero import Button
from signal import pause

button = Button(2)

def play_line():
    """
    Plays './WhoDisturbsMySlumber.wav'.
    """
    print("Button pressed.")
    playsound("./WhoDisturbsMySlumber.wav")
    print("Played.")

button.when_pressed = play_line

pause()