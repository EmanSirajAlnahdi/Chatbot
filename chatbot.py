from openai import OpenAI
from dotenv import load_dotenv
from os import getenv
from RealtimeTTS import TextToAudioStream
from RealtimeSTT import AudioToTextRecorder
from RealtimeTTS.engines.system_engine import SystemEngine


load_dotenv()

client = OpenAI(api_key=getenv("API_KEY"), base_url="https://api.deepseek.com")
engine = SystemEngine()
stream = TextToAudioStream(engine)



def process_text(text):
    print(text)

if __name__ == '__main__':
    print("Wait until it says 'speak now'")

    while True:
        # Record audio and convert it to text
        recorder = AudioToTextRecorder()
        transcript = recorder.text(process_text)
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[{"role": "user", "content": str(transcript)},],
            stream=False
            )
        stream.feed(response.choices[0].message.content)
        stream.play_async()
        