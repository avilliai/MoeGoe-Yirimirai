
import os
from mirai import  Voice,Image
from mirai import Mirai, WebSocketAdapter, FriendMessage, GroupMessage, At, Plain

from MoeGoe import voiceGenerate

import sys

from plugins.RandomStr.RandomStr import random_str
from plugins.picGet import pic
from readConfig import readConfig
from trans import translate

if __name__ == '__main__':
    bot = Mirai(3093724179, adapter=WebSocketAdapter(
        verify_key='1234567890', host='localhost', port=23456
    ))
    @bot.on(FriendMessage)
    async def yuYinMode(event: FriendMessage):
        if str(event.message_chain).startswith('发送'):
            sa = str(event.message_chain)[2:]
            ranpath = random_str()
            out = sys.argv[0][:-20] + 'PythonPlugins\\plugins\\voices\\' + ranpath + '.wav'
            list1=readConfig()
            aimFriend=list1[0]
            aimGroup = list1[1]
            statusPath = list1[2]
            model = int(list1[3])
            lang = list1[4]

            if int(statusPath)==0:
                if lang=='中文':
                    tex = '[ZH]' + sa + '[ZH]'
                    voiceGenerate(tex, out,model)
                    await bot.send_friend_message(int(aimFriend),Voice(path=out))
                if lang=='日语':
                    tex = '[JA]' + translate(sa) + '[JA]'
                    voiceGenerate(tex, out,model)
                    await bot.send_friend_message(int(aimFriend),Voice(path=out))
            elif int(statusPath)==1:
                if lang=='中文':
                    tex = '[ZH]' + sa + '[ZH]'
                    voiceGenerate(tex, out,model)
                    await bot.send_group_message(int(aimGroup),Voice(path=out))
                if lang=='日语':
                    tex = '[JA]' + translate(sa) + '[JA]'
                    voiceGenerate(tex, out,model)
                    await bot.send_group_message(int(aimGroup),Voice(path=out))
    #图片模块
    @bot.on(GroupMessage)
    async def handle_group_message(event: GroupMessage):
        #if str(event.message_chain) == '/pic':
        if '/pic' in str(event.message_chain):
            picNum=int((str(event.message_chain))[4:])
            if picNum<10 and picNum>-1:
                for i in range(picNum):
                    a = pic()
                    await bot.send(event, Image(path=a))
            elif picNum=='':
                a = pic()
                await bot.send(event, Image(path=a))
            else:
                await bot.send(event,"可以发点正常的数字吗")


    #中文生成
    @bot.on(GroupMessage)
    async def handle_group_message(event: GroupMessage):
        if str(event.message_chain).startswith('#中文'):
            if len(str(event.message_chain)) <280:
                ranpath = random_str()
                out = sys.argv[0][:-20]+'PythonPlugins\\plugins\\voices\\' + ranpath + '.wav'
                #out = 'D:\\Mirai\\Yiris\\PythonPlugins\\plugins\\voices\\01.wav'
                if(os.path.exists(out)):
                    os.remove(out)
                tex= '[ZH]'+((str(event.message_chain))[3:])+'[ZH]'
                with open('ModePath.txt', mode='r', encoding='utf-8') as fa:
                    model = fa.readline()
                    fa.close()
                    print('当前模型' + model)
                voiceGenerate(tex, out,int(model))
                await bot.send(event, Voice(path=out))
            else:
                ranpath = random_str()
                out = sys.argv[0][:-20]+'PythonPlugins\\plugins\\voices\\' + ranpath + '.wav'
                # out = 'D:\\Mirai\\Yiris\\PythonPlugins\\plugins\\voices\\01.wav'
                tex = '[ZH]太常了哦......[ZH]'
                voiceGenerate(tex, out)
                await bot.send(event, Voice(path=out))

    #日语生成
    @bot.on(GroupMessage)
    async def handle_group_message(event: GroupMessage):
        if  str(event.message_chain).startswith('#说'):
            if len(str(event.message_chain)) <280:
                ranpath = random_str()
                out = sys.argv[0][:-20]+'PythonPlugins\\plugins\\voices\\' + ranpath + '.wav'
                tex = '[JA]' + translate((str(event.message_chain))[2:]) + '[JA]'
                #获取当前模型
                with open('ModePath.txt', mode='r', encoding='utf-8') as fa:
                    model = fa.readline()
                    fa.close()
                    print('当前模型' + model)
                voiceGenerate(tex, out,int(model))
                await bot.send(event,Voice(path=out))
            else:
                #以下五行代码可以作为调用文本转语音的示例
                ranpath = random_str()
                out = sys.argv[0][:-20]+'PythonPlugins\\plugins\\voices\\' + ranpath + '.wav'
                tex = '[JA]' + translate('不行,太长了哦.....') + '[JA]'
                voiceGenerate(tex, out)
                await bot.send(event, Voice(path=out))

    #失效
    '''@bot.on(FriendMessage)
    async def handle_group_message(event: FriendMessage):
        if str(event.message_chain).startswith('#说'):
            if len(str(event.message_chain)) < 280:
                ranpath = random_str()
                out = sys.argv[0][:-20] + 'PythonPlugins\\plugins\\voices\\' + ranpath + '.wav'
                tex = '[JA]' + translate((str(event.message_chain))[1:]) + '[JA]'
                voiceGenerate(tex, out)
                await bot.send(event, Voice(path=out))
            else:
                ranpath = random_str()
                out = sys.argv[0][:-20] + 'PythonPlugins\\plugins\\voices\\' + ranpath + '.wav'
                tex = '[JA]' + translate('不行,太长了哦.....') + '[JA]'
                voiceGenerate(tex, out)
                await bot(event, Voice(path=out))'''

    #连接群
    @bot.on(FriendMessage)
    async def on_friend_message(event: FriendMessage):
        if str(event.message_chain).startswith('连接群'):
            sa = str(event.message_chain).split('#')
            configPath='groupPath.txt'
            with open(configPath, mode='w', encoding='utf-8') as ff:
                ff.write(sa[1])
                await bot.send(event,'已载入配置文件')
            statusPath = 'status.txt'
            with open(statusPath, mode='w', encoding='utf-8') as fs:
                fs.write(str(1))
                await bot.send(event, '已切换为群聊'+sa[1])

    #连接人
    @bot.on(FriendMessage)
    async def on_friend_message(event: FriendMessage):
        if str(event.message_chain).startswith('连接对象'):
            sa = str(event.message_chain).split('#')
            configPath = 'friendPath.txt'
            with open(configPath, mode='w', encoding='utf-8') as ff:
                ff.write(sa[1])
                await bot.send(event, '已载入配置文件')

            statusPath = 'status.txt'
            with open(statusPath, mode='w', encoding='utf-8') as fs:
                fs.write(str(0))
                await bot.send(event, '已切换为私聊对象'+sa[1])

    #语言切换
    @bot.on(FriendMessage)
    async def Lanconfig(event: FriendMessage):
        if str(event.message_chain).startswith('切换'):
            sa = str(event.message_chain)[2:]
            langPath = 'langPath.txt'
            with open(langPath, mode='w', encoding='utf-8') as ff:
                if sa=='中文':
                    ff.write(sa)
                    await bot.send(event, '已切换，当前使用语言'+sa)
                elif sa=='日语':
                    ff.write(sa)
                    await bot.send(event, '已切换，当前使用语言' + sa)
                else:
                    await bot.send(event, '数值不合法，语言选择：中文/日语')
    #模型切换
    @bot.on(FriendMessage)
    async def on_friend_message(event: FriendMessage):
        if str(event.message_chain).startswith('M'):
            sa = str(event.message_chain).split('#')
            ModePath = 'ModePath.txt'
            modelList = ['0', '1', '2', '3']
            with open(ModePath, mode='w', encoding='utf-8') as ff:
                if sa[1] in modelList:
                    ff.write(sa[1])
                    await bot.send(event, '已切换，当前使用模型' + sa[1])
                else:
                    await bot.send(event, '数值不合法，模型范围[0-3]')

    bot.run()