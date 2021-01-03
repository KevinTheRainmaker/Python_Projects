import pyttsx3
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("좋은 아침이에요")
    elif hour>=12 and hour<18:
        speak("즐거운 오후에요")
    else:
        speak("오늘 하루는 어떠셨나요?")

    speak("저는 당신의 비서, 자비스입니다. 무엇을 도와드릴까요?")

if __name__ == "__main__":
    wishMe()