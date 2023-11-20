import os
from dotenv import load_dotenv
import elevenlabs
import subprocess
import requests
import pyperclip
import os.path

#  pip install urllib3==1.26.6  

load_dotenv()
api_key = os.getenv("ELEVEN_API_KEY")
elevenlabs.set_api_key(api_key)

# Get content from clipboard
clipboard_content = pyperclip.paste()


audio = elevenlabs.generate(
    text = clipboard_content,
    voice = "Bella"
)
save_path ='/Users/kubansa/project/elevenlabs/voice'

clipboard_content2 = clipboard_content.replace(' ','_')

completeName = os.path.join(save_path, f'{clipboard_content2}.mp3')

elevenlabs.save(audio, completeName)


#Daniel - onwK4e9ZLuTAKqWW03F9
url = 'https://api.elevenlabs.io/v1/text-to-speech/EXAVITQu4vr4xnSDxMaL'
headers = {
    'accept': '*/*',
    'xi-api-key': api_key,
    'Content-Type': 'application/json'
}
data = {
    'text': clipboard_content,
    'voice_settings': {
        'stability': 0.30,
        'similarity_boost': 0.50
    }
}


response = requests.post(url, headers=headers, json=data, stream=True)
response.raise_for_status()
# use subprocess to pipe the audio data to ffplay and play it
ffplay_cmd = ['ffplay', '-autoexit', '-']
ffplay_proc = subprocess.Popen(ffplay_cmd, stdin=subprocess.PIPE)
for chunk in response.iter_content(chunk_size=4096):
    ffplay_proc.stdin.write(chunk)
    print("Downloading...")

# close the ffplay process when finished
ffplay_proc.stdin.close()
ffplay_proc.wait()