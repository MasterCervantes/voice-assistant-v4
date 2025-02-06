import win32com.client

class TTSClient:
    def __init__(self):
        self.speaker = win32com.client.Dispatch("SAPI.SpVoice")

    def synthesize(self, text):
        try:
            self.speaker.Speak(text)
        except Exception as e:
            print(f"Failed to synthesize text: {str(e)}")