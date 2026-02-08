import speech_recognition as sr

class SpeechRecognizer:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def recognize_from_microphone(self):
        with sr.Microphone() as source:
            print("Adjusting for ambient noise... Please wait.")
            self.recognizer.adjust_for_ambient_noise(source)
            print("Listening...")
            audio = self.recognizer.listen(source)
            try:
                print("Recognizing...")
                return self.recognizer.recognize_google(audio)
            except sr.RequestError:
                return "Could not request results from Google Speech Recognition service."
            except sr.UnknownValueError:
                return "Google Speech Recognition could not understand audio."

    def recognize_from_file(self, file_path):
        with sr.AudioFile(file_path) as source:
            audio = self.recognizer.record(source)
            try:
                return self.recognizer.recognize_google(audio)
            except sr.RequestError:
                return "Could not request results from Google Speech Recognition service."
            except sr.UnknownValueError:
                return "Google Speech Recognition could not understand audio."

    def recognize_continuously(self):
        with sr.Microphone() as source:
            print("Adjusting for ambient noise... Please wait.")
            self.recognizer.adjust_for_ambient_noise(source)
            print("Listening for continuous input...")
            try:
                for audio in sr.Microphone.listen(source, phrase_time_limit=5):
                    print("Recognizing...")
                    text = self.recognizer.recognize_google(audio)
                    print(text)
            except Exception as e:
                return str(e)

# Example usage:
if __name__ == '__main__':
    recognizer = SpeechRecognizer()
    print(recognizer.recognize_from_microphone())