# pip install gtts
import os
from gtts import gTTS

txt = "덕영고등학교 소프트웨어학과 2학년 신희준, 자바를 열심히 공부하고 있습니다."
filename = "ttsresult.mp3"

tts = gTTS(text=txt, lang='ko')

tts.save(filename)

os.system(f'start {filename}')
