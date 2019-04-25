import pyttsx3


class SpeechSynthesizer:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('voice', 'com.apple.speech.synthesis.voice.samantha')
        self.engine.setProperty('rate', self.engine.getProperty('rate') - 10)

    def talk(self, text):
        self.engine.say(text)
        self.engine.runAndWait()