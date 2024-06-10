import speech_recognition as sr

r = sr.Recognizer()

try:
    test = sr.AudioFile('test.wav')
    with test as source:
        print("Recording the audio...")
        audio = r.record(source,duration=4)
        print("Recording complete.")

    try:
        print("Recognizing the audio...")
        text = r.recognize_google(audio)
        print("Google Web Speech thinks you said: " + text)
    except sr.UnknownValueError:
        print("Google Web Speech could not understand the audio.")
    except sr.RequestError as e:
        print("Could not request results from Google Web Speech service; {0}".format(e))

except FileNotFoundError:
    print("The file 'test.wav' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
