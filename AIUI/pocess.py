#-*- coding: utf-8 -*-
import json
import demjson
import matplotlib.pyplot as plt
import numpy as np
from pydub import AudioSegment
import wave



pcm_path = ""
AIUI_Adata_path = ''
json_file = open('', 'r')

def pcm2wav(pcm_path):
    with open(pcm_path, 'rb') as pcmfile:
        pcmdata = pcmfile.read()
    with wave.open(pcm_path + '.wav', 'wb') as wavfile:
        wavfile.setparams((1, 2, 16000, 0, 'NONE', 'NONE'))
        wavfile.writeframes(pcmdata)

#格式化json，并取值
def Pocess_data(file_name):
    f = file_name
    content = f.read()
    # #改到这里
    result = json.loads(content)
    #转换成规范的json
    result = demjson.decode(result)
    text = result["data"][1]["intent"]["text"]
    print(text)

#查看音频波形图
def show_pcm(pcm_path):
    original = np.memmap(pcm_path, dtype='h', mode='r')
    plt.plot(original)
    plt.show()

#切割音频文件
def Pocess_pcm(wav_path,start_time,end_time):
    sound = AudioSegment.from_mp3(wav_path)
    sound_1 = sound[start_time:end_time]
    sound_2 = sound[end_time:]
    sound_1.export(AIUI_Adata_path + '_1.wav')
    sound_2.export(AIUI_Adata_path + '_2.wav')

if __name__ == "__main__":
    show_pcm(pcm_path)
    # pcm2wav(pcm_path)
    # Pocess_pcm(pcm_path + '.wav',0,986780)