import os
from gtts import gTTS
from moviepy.editor import *

# 输入文字
text = input("请输入要生成视频的文字：")

# 生成语音
tts = gTTS(text=text, lang='zh-cn')
tts.save("voice.mp3")

# 自动生成背景图（这里用纯色）
color_clip = ColorClip(size=(1080, 1920), color=(30, 30, 30), duration=10)

# 加载语音
audio = AudioFileClip("voice.mp3")
color_clip = color_clip.set_audio(audio)

# 添加文字
txt_clip = TextClip(text, fontsize=60, color='white', size=(1000, None), method='caption', align='center')
txt_clip = txt_clip.set_duration(audio.duration).set_position('center')

# 合成视频
final = CompositeVideoClip([color_clip, txt_clip])
final.write_videofile("output.mp4", fps=24)

print("✅ 视频已生成：output.mp4")
