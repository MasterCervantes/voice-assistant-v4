import requests

class OllamaChecker:
    @staticmethod
    def get_available_models():
        try:
            response = requests.get('http://localhost:11434/api/tags')
            if response.status_code == 200:
                models = response.json().get('models', [])
                return [model['name'] for model in models]
            return ['mistral', 'llama2']
        except:
            return ['mistral', 'llama2']

    @staticmethod
    def is_ollama_running():
        try:
            response = requests.get('http://localhost:11434/api/tags')
            return response.status_code == 200
        except:
            return False