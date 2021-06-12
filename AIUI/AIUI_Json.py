#-*- coding: utf-8 -*-
import json
import os
import demjson
import pandas as pd
import numpy as np

csv_path = '/Users/zhouhuchen/Desktop/android/data_test/AIUI/result_6.csv'
df = pd.DataFrame(np.random.randn(100,1))
i = 0
files_list = os.listdir('/Users/zhouhuchen/Desktop/android/data_test/AIUI/data/wake6')
files_list.sort(key=lambda x:int(x[-7:-5]))
for file_name in files_list:
    file_name_t = "/Users/zhouhuchen/Desktop/android/data_test/AIUI/data/wake6/" + file_name
    with open(file_name_t,'r') as f:
        content = f.read()
        result = json.loads(content)
        try:
            text = result["data"][1]["intent"]["text"]
        except BaseException:
            df.iloc[i,0] = 'audio-' + str(i+100) + '没获取到语音信息'
            print('不存在text值')
            i = i + 1
            continue
        df.iloc[i,0] = 'audio-' + str(i+100) + text
        i = i + 1 
        print('audio-' + str(i+99) + text)

df.to_csv(csv_path, index=0)