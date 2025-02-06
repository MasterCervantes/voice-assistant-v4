import requests
import winsound

class XTTSClient:
    def __init__(self, url, model='v2.0.2', device='cpu'):
        self.url = url
        self.model = model
        self.device = device

    def synthesize(self, text):
        try:
            response = requests.post(
                f"{self.url}/api/synthesize",
                headers={'Content-Type': 'application/json'},
                json={"text": text, "model": self.model, "device": self.device}
            )
            if response.status_code == 200:
                audio_data = response.content
                output_file = "output.wav"
                with open(output_file, 'wb') as f:
                    f.write(audio_data)
                winsound.PlaySound(output_file, winsound.SND_FILENAME)
            else:
                print(f"Error: {response.status_code} - {response.text}")
        except Exception as e:
            print(f"Failed to synthesize text: {str(e)}")