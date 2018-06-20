from aip import AipSpeech
def speech(message):
    APP_ID = ''
    API_KEY = ''
    SECRECT_KEY = ' '
    client = AipSpeech(APP_ID,API_KEY,SECRECT_KEY)
    result = client.synthesis(message,'zh',1,{'vol':5,'per':4})
    if not isinstance(result, dict):
        with open('auido.mp3', 'wb') as f:
            f.write(result)
        return True
    else:
        return False
def writing(voice):
    APP_ID = ''
    API_KEY = ''
    SECRECT_KEY = ' '
    client = AipSpeech(APP_ID,API_KEY,SECRECT_KEY)
    def get_file_content(filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()
    result = client.asr(get_file_content(voice), 'pcm', 16000, {'dev_pid':1536,})
    try:
        return True,result['result']
    except:
        return False,'未识别'


    
