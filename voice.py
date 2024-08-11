import speech_recognition as sr

# Initialize the speech recognizer
recognizer = sr.Recognizer()
mic = sr.Microphone()

def listen_for_command():
    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening for command...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio).lower()
            print("Recognized command:", command)
            return command
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return None
        except sr.RequestError:
            print("Could not request results; check your network connection.")
            return None

# Main loop to continuously listen for voice commands
while True:
    command = listen_for_command()
    if command == 'stop':
        print("Stopping the voice recognition model.")
        break
