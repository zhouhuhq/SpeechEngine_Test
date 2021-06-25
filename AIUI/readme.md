# 这是AIUI的测试代码
APPID 和 API_KEY 还有AUTH_ID需要去AIUI官网上获取。  
网址：https://aiui.xfyun.cn
# 文件结构
AIUI.py为主要请求代码；<br>
pocess.py文件为音频分割文件，和音频处理文件(可不用)<br>
AIUI_Json.py文件为返回json格式处理文件
数据集使用的是.pcm文件
# 环境需求
AIUI.py -- python2.x 
AIUI_Json.py -- python3.x
# 如何使用
```python
python AIUI.py
```
会返回结果的json，存储在目标路径下，使用AIUI_Json.py解析即可。

