#-*- coding: utf-8 -*-
import requests
import time
import hashlib
import base64
import json
import os

# files_list = os.listdir('/Users/zhouhuchen/Desktop/android/data_test/data/wake1')

URL = "http://openapi.xfyun.cn/v2/aiui"
APPID = ""
API_KEY = ""
AUE = "raw"
SPEEX_SIZE= "300"
AUTH_ID = ""
DATA_TYPE = "audio"
SAMPLE_RATE = "16000"
SCENE = "main"
RESULT_LEVEL = "complete"
LAT = "39.938838"
LNG = "116.368624"
#个性化参数，需转义
PERS_PARAM = "{\\\"auth_id\\\":\\\"2894c985bf8b1111c6728db79d3479ae\\\"}"
FILE_PATH = "/Users/zhouhuchen/Desktop/android/data_test/data/all_1.pcm"
# FILE_PATH = "/Users/zhouhuchen/Desktop/android/data_test/AICloud/audio/spx/1.speex"


def buildHeader():
    curTime = str(int(time.time()))
    param = "{\"result_level\":\""+RESULT_LEVEL+"\",\"auth_id\":\""+AUTH_ID+"\",\"data_type\":\""+DATA_TYPE+"\",\"sample_rate\":\""+SAMPLE_RATE+"\",\"scene\":\""+SCENE+"\",\"lat\":\""+LAT+"\",\"lng\":\""+LNG+"\"}"
    #使用个性化参数时参数格式如下：
    # param = "{\"result_level\":\""+RESULT_LEVEL+"\",\"auth_id\":\""+AUTH_ID+"\",\"data_type\":\""+DATA_TYPE+"\",\"sample_rate\":\""+SAMPLE_RATE+"\",\"scene\":\""+SCENE+"\",\"lat\":\""+LAT+"\",\"lng\":\""+LNG+"\",\"pers_param\":\""+PERS_PARAM+"\"}"
    paramBase64 = base64.b64encode(param)
    m2 = hashlib.md5()
    m2.update(API_KEY + curTime + paramBase64)
    checkSum = m2.hexdigest()

    header = {
        'X-CurTime': curTime,
        'X-Param': paramBase64,
        'X-Appid': APPID,
        'X-CheckSum': checkSum,
    }
    return header

def readFile(filePath):
    binfile = open(filePath, 'rb')
    data = binfile.read()
    return data

# #循环读文件进行语音测试
# i = 1
# files_list = [name for name in os.listdir('/Users/zhouhuchen/Desktop/android/data_test/data/wake6') if name.endswith('.pcm')]
# files_list.sort(key=lambda x:int(x[-7:-4]))
# for filename in files_list:
#     FILE_PATH = "/Users/zhouhuchen/Desktop/android/data_test/data/wake6/" + filename
#     Json_Path = "/Users/zhouhuchen/Desktop/android/data_test/AIUI/data/wake6/" + str(i) + '.json'
#     r = requests.post(URL, headers=buildHeader(), data=readFile(FILE_PATH))
#     result = r.content
#     f2 = open(Json_Path, 'w')
#     f2.write(result)
#     i = i + 1

r = requests.post(URL, headers=buildHeader(), data=readFile(FILE_PATH))
result = r.content

print(result)



