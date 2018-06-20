#-*- codind = UTF-8-*-
import itchat
from reply_to_myself import *
from reply_to_others import *
from file2 import *
from voice_translate import *
itchat.auto_login(hotReload=True)
itchat.send("你好，微信机器人启动。。。\
            \n请输入命令：\n1.关机\n2.取消关机\n3.打开WiFi\n4.cap\n5.视频",\
            toUserName='filehelper')




b = []
a = []
@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    
   # global flag
    message =  msg['Text'] 
    fromName =msg['FromUserName'] 
    toName = msg['ToUserName']
    nickname=msg['User']['NickName']
    if toName == "filehelper":
        reply_to_filehelper(message)

    else:
        if read(nickname):
            
            a.append(nickname)
            
            if message=='开机':
                reduce(nickname)
            while a.count(nickname)<2:
                itchat.send('你好，机器人已关闭，回复 开机 可开启',toUserName=fromName)
                break
            
            
            
           
        else:
            if message == '关机':
                add(nickname)
                
            else:
                b.append(nickname)
                while b.count(nickname)<2:
                    itchat.send('你好，机器人处于开启状态，回复 关机 可关闭\n '+
                                '回复 菜名 可获取菜谱\n '+
                                '回复 天气+城市 可获取天气信息\n' +
                                '回复 人名 可获取人物信息\n' +
                                '回复 新闻 可获取新闻\n' +
                                '回复 xx+图片 可获取图片\n '+
                                '另 机器人有聊天功能',

                                toUserName=fromName)
                    break
                
                return reply_to_others(message)
        
        

        
            

'''此模块回复图片'''
@itchat.msg_register(itchat.content.PICTURE)
def print_you(msg):
    msg['Text'](msg['FileName'])
    itchat.send('@%s@%s' %('img' if msg['Type'] ==\
                           'Picture' else 'fil', msg["FileName"]), msg["FromUserName"])
    
@itchat.msg_register(itchat.content.RECORDING)
def talk(msg):
    msg['Text']('voice.mp3')
    flag,result = writing('voice.mp3')
    
    itchat.send("来自<%s>\n内容为<%s>"%(msg['User']['NickName'],result),toUserName='filehelper')
    if flag:
        return reply_to_others(result)
    else:
        return '不好意思，未识别'
    
    
    
    

itchat.run()



