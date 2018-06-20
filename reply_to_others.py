import requests
def reply_to_others(message):
    
    
    apiUrl = 'http://www.tuling123.com/openapi/api'
    KEY = '输入你的key'
    data = {
        'key'    : KEY,
        'info'   : message,
        'userid' : '随便输入个名字',
    }

    r = requests.post(apiUrl, data=data).json()
    if r.get('code')==100000:
        
        return r.get('text')
    if r.get('code')==200000:
        return str(r.get('url'))
    if r.get('code')==302000:
        l = {}
        for i in range(5):
            x = str(r.get('list')[i].get('article'))
            y = str(r.get('list')[i].get('detailurl'))
            l[x]=y
            
        return str(l)
    if r.get('code')==308000:
        l = {}
        for i in range(5):
            x = str(r.get('list')[i].get('detailurl'))
            l['第%d名'%(i+1)]=x
        return str(l)

