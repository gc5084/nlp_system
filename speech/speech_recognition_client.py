import speech_recognition as sr


class SpeechRecognizer:

    def __init__(self):
        self.recognizer = sr.Recognizer()

    def _get_recognized_audio(self, audio):
        try:
            recognized_text = self.recognizer.recognize_google(audio)
            print("Google Speech Recognition thinks you said: " + recognized_text)
        except sr.UnknownValueError as e:
            print("Google Speech Recognition could not understand audio {0}".format(e))
            return None
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
            return None
        return recognized_text

    def listen(self):
        with sr.Microphone() as source:
            print("Say something!")
            audio = self.recognizer.listen(source)
            return self._get_recognized_audio(audio)
