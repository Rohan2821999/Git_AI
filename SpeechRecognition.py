import speech_recognition as sound

r = sound.Recognizer()
while (True):
    with sound.Microphone()as source:
        audio = r.listen(source)
    try:
        print(r.recognize_google(audio))
    except sound.UnknownValueError:
        pass
