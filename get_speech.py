import speech_recognition as sr
from glob import glob
import re
import json
from tqdm import tqdm


def speech_to_text(path):
    r = sr.Recognizer()
    with sr.AudioFile(path) as source:
        audio = r.record(source)
        try:
            text = r.recognize_google(audio)
            print(text)
            return text
        except:
            print('Conversion unsuccessful')
            return ""


path_to_audio = './audio-chunks/'
duration = 15  # seconds

# order the files
files = glob(path_to_audio+'*.wav')
files.sort(key=lambda f: int(re.sub('\D', '', f)))
print('Sorted {} files.'.format(len(files)))

i = 0
output = {}
for f in tqdm(files):
    text = speech_to_text(f)
    output[i] = text
    tqdm.write(output[i])
    i += duration


with open('speech.json', 'w') as fp:
    json.dump(output, fp)

