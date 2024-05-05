import speech_recognition as sr

# Recognizer
rec = sr.Recognizer()
# Microfone
#print(sr.Microphone().list_microphone_names())
with sr.Microphone(1) as mic:
    rec.adjust_for_ambient_noise(mic)
    print('fala que eu te escuto ...')
    audio = rec.listen(mic)
    texto = rec.recognize_google(audio, language='pt-BR')
    print(texto)