import speech_recognition as sr

# Initialize the recognizer
r = sr.Recognizer()

# Load the audio file
test = sr.AudioFile('noise.wav')
with test as source:
    # Adjust for ambient noise and record the audio
    r.adjust_for_ambient_noise(source, duration=0.5)
    audio = r.record(source)

# Recognize the speech in the audio
try:
    text = r.recognize_google(audio)
    print("Recognized text: " + text)
except sr.UnknownValueError:
    print("Google Web Speech could not understand the audio.")
except sr.RequestError as e:
    print("Could not request results from Google Web Speech service; {0}".format(e))
