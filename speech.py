
def text():
    import speech_recognition as sr
    r = sr.Recognizer()
    dest = ""
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=4)
        audio = r.listen(source)
        try:
            dest = r.recognize_google(audio)
            str1+=" "
            str1+=dest
            print(str1)
        except:
            print('Data Unable To Read')
    return dest

text()