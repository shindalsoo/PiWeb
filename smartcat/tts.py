# pip install gTTS
from gtts import gTTS

# pip install playsound
from playsound import playsound

# text = "이제, 점심시간 끝났습니다. 분당경영고 학생분들 신달수선생님 앞으로 모여주세요."
text = "오늘 오후의 수업내용은, 아주 멋진 순서가 준비되어 있습니다. 모두 코로나때문에 지치고 힘들지만, 힘을 냅시다. 화이팅!!"
filename = "helloEn.mp3"
tts = gTTS(text=text, lang='ko') # ko
tts.save("helloEn.mp3")

playsound(filename)