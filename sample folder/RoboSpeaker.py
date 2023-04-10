import pyttsx3

print("-------------------------------------------RoboSpeaker-----------------------------------------------------------")

engine = pyttsx3.init()

while True:
    x = input("Enter what you want me to speak (or 'q' to quit): ")
    if x == 'q':
        engine.say("Bye!")
        engine.runAndWait()
        break
    
    engine.say(x)
    engine.runAndWait()