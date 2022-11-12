
import random
import os

import mirai.models.events

import asyncio
import datetime
from mirai import Mirai, WebSocketAdapter, Startup, Shutdown
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

from mirai import Image, Voice
from mirai import Mirai, WebSocketAdapter, FriendMessage, GroupMessage, At, Plain

from MoeGoe import voiceGenerate

import sys

from plugins.RandomStr.RandomStr import random_str
from plugins.moyu import moyu
from plugins.newsEveryday import news
from plugins.picGet import pic
from readConfig import readConfig
from trans import translate

if __name__ == '__main__':
    bot = Mirai(3093724179, adapter=WebSocketAdapter(
        verify_key='1234567890', host='localhost', port=23456
    ))
    #私聊内容
    @bot.on(FriendMessage)
    async def on_friend_message(event: FriendMessage):
        if str(event.message_chain) == '你好':
            await bot.send(event, 'Hello World!')

    #监听群聊消息
    @bot.on(GroupMessage)
    async def handle_group_message(event: GroupMessage):
        if str(event.message_chain) == 'test':
            await bot.send_group_message(699455559, 'yucca测试版YIRIS启动成功！')

            # print(str(event.message_chain))  # 打印消息内容

    @bot.on(mirai.models.events.NudgeEvent)
    async def handle_nudge_message(event: mirai.models.events.NudgeEvent):
       await bot.send_nudge(target=1840094972,subject=3093724179,kind='Friend')

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


    # 摸鱼
    @bot.on(GroupMessage)
    async def handle_group_message(event: GroupMessage):
        if str(event.message_chain)=='摸鱼':
             moyus=moyu()
             await bot.send(event, Image(path=moyus))

    #读取配置的测试
    '''@bot.on(GroupMessage)
    async def handle_group_message(event: GroupMessage):
        if str(event.message_chain) == 'test111':
            txt=r"Config\moyu\groups.txt"
            groupList = readConfig(txt)
            for i in  groupList:
                intTrans=int(i)
                await bot.send_group_message(intTrans, Voice(path='D:\\Mirai\\Yiris\\PythonPlugins\\plugins\\voices\\$mfd9t.wav'))'''


    #定时摸鱼,可以在Config//moyu//中添加群
    scheduler = AsyncIOScheduler()
    @bot.on(Startup)
    def start_scheduler(_):
        scheduler.start()  # 启动定时器
        print('当前路径' + sys.argv[0])
        Path=sys.argv[0][:-20]
    @bot.on(Shutdown)
    def stop_scheduler(_):
        scheduler.shutdown(True)  # 结束定时器
    #摸鱼人日历
    @scheduler.scheduled_job(CronTrigger(hour=16, minute=48))
    async def timer():
        moyuPic=moyu()
        txt = r"Config\moyu\groups.txt"
        groupList = readConfig(txt)
        for i in groupList:
            intTrans = int(i)
        await bot.send_group_message(intTrans, Image(path=moyuPic))

    @scheduler.scheduled_job(CronTrigger(hour=16, minute=49))
    async def timer():
        txt = r"Config\moyu\groups.txt"
        groupList = readConfig(txt)
        for i in groupList:
            intTrans = int(i)
            index = random.randint(1, 4)
            if index == 1:
                ranpath = random_str()
                out = sys.argv[0][:-20]+'PythonPlugins\\plugins\\voices\\' + ranpath + '.wav'
                tex = '[JA]' + translate('啊......好累呢，该下班了') + '[JA]'
                voiceGenerate(tex, out)
                await bot.send_group_message(intTrans, Voice(path=out))
            if index == 2:
                ranpath = random_str()
                out = sys.argv[0][:-20]+'PythonPlugins\\plugins\\voices\\' + ranpath + '.wav'
                tex = '[ZH]辛苦了，要注意休息哦~[ZH]'
                voiceGenerate(tex, out)
                await bot.send_group_message(intTrans, Voice(path=out))
            if index == 3:
                ranpath = random_str()
                out = sys.argv[0][:-20]+'PythonPlugins\\plugins\\voices\\' + ranpath + '.wav'
                tex = '[JA]' + translate('辛苦了，要注意休息哦~') + '[JA]'
                voiceGenerate(tex, out)
                await bot.send_group_message(intTrans, Voice(path=out))

    #早八新闻自动推送
    @scheduler.scheduled_job(CronTrigger(hour=7, minute=40))
    async def timer():
        newsPic = news()
        txt = r"Config\moyu\groups.txt"
        groupList = readConfig(txt)
        for i in groupList:
            intTrans = int(i)
            await bot.send_group_message(intTrans, Image(path=newsPic))
            ranpath = random_str()
            out = sys.argv[0][:-20] + 'PythonPlugins\\plugins\\voices\\' + ranpath + '.wav'
            tex = '[JA]' + translate('早上好~........已经为您整理好了今天的新闻！.......有什么有趣的事情吗?') + '[JA]'
            voiceGenerate(tex, out)
            await bot.send_group_message(intTrans, Voice(path=out))

    #早八问候
    @scheduler.scheduled_job(CronTrigger(hour=9, minute=34))
    async def timer():
        txt = r"Config\moyu\groups.txt"
        groupList = readConfig(txt)
        for i in groupList:
            intTrans = int(i)
            index = random.randint(1, 4)
            if index == 1:
                ranpath = random_str()
                out = sys.argv[0][:-20]+'PythonPlugins\\plugins\\voices\\' + ranpath + '.wav'
                tex = '[JA]' + translate('早上好......记得吃早饭~......今天也请好好加油~！') + '[JA]'
                voiceGenerate(tex, out)
                await bot.send_group_message(intTrans, Voice(path=out))
            if index == 2:
                ranpath = random_str()
                out = 'D:\\Mirai\\Yiris\\PythonPlugins\\plugins\\voices\\' + ranpath + '.wav'
                tex = '[JA]' + translate('唔......早上好呀!') + '[JA]'
                voiceGenerate(tex, out)
                await bot.send_group_message(intTrans, Voice(path=out))
            if index == 3:
                ranpath = random_str()
                out = 'D:\\Mirai\\Yiris\\PythonPlugins\\plugins\\voices\\' + ranpath + '.wav'
                tex = '[JA]' + translate('起床啦~!.......现在还没起床的话可不行') + '[JA]'
                voiceGenerate(tex, out)
                await bot.send_group_message(intTrans, Voice(path=out))

    #早八新闻
    @bot.on(GroupMessage)
    async def handle_group_message(event: GroupMessage):
        if str(event.message_chain) == '新闻':
            newPic = news()
            await bot.send(event, Image(path=newPic))
            ranpath = random_str()
            out = sys.argv[0][:-20]+'PythonPlugins\\plugins\\voices\\' + ranpath + '.wav'
            tex = '[JA]' + translate('这是今天的新闻！') + '[JA]'
            voiceGenerate(tex, out)
            await bot.send(event, Voice(path=out))

    #天气查询模块
    import re
    import plugins.weatherQuery
    @bot.on(GroupMessage)
    async def weather_query(event: GroupMessage):
        # 从消息链中取出文本
        msg = "".join(map(str, event.message_chain[Plain]))
        # 匹配指令
        m = re.match(r'^查询\s*(\w+)\s*$', msg.strip())
        if m:
            # 取出指令中的地名
            city = m.group(1)
            await bot.send(event, '查询中……')
            # 发送天气消息
            await bot.send(event, await plugins.weatherQuery.querys(city))


    # 对早的回复
    @bot.on(GroupMessage)
    def on_group_message(event: GroupMessage):
        if  str(event.message_chain).startswith('早') :
            if len(str(event.message_chain))<6:
                index = random.randint(1, 4)
                if index == 1:
                    ranpath = random_str()
                    out = sys.argv[0][:-20]+'PythonPlugins\\plugins\\voices\\' + ranpath + '.wav'
                    tex = '[JA]' + translate('早上好') + '[JA]'
                    voiceGenerate(tex, out)
                    return bot.send(event, Voice(path=out))
                if index == 2:
                    ranpath = random_str()
                    out = sys.argv[0][:-20]+'PythonPlugins\\plugins\\voices\\' + ranpath + '.wav'
                    tex = '[ZH]早安，天气很好呢[ZH]'
                    voiceGenerate(tex, out)
                    return bot.send(event, Voice(path=out))
                if index == 3:
                    ranpath = random_str()
                    out = sys.argv[0][:-20]+'PythonPlugins\\plugins\\voices\\' + ranpath + '.wav'
                    tex = '[JA]' + translate('今天也要加油') + '[JA]'
                    voiceGenerate(tex, out)
                    return bot.send(event, Voice(path=out))
                if index >3:
                    ranpath = random_str()
                    out = sys.argv[0][:-20]+'PythonPlugins\\plugins\\voices\\' + ranpath + '.wav'
                    tex = '[JA]' + translate('早上好~！，想出去走走吗？~') + '[JA]'
                    voiceGenerate(tex, out)
                    return bot.send(event, Voice(path=out))


    # 对艾特的回复
    @bot.on(GroupMessage)
    def on_group_message(event: GroupMessage):
        if At(bot.qq) in event.message_chain:
            index=random.randint(1,4)
            if index==1:
                return bot.send(event, [At(event.sender.id), ' 你在叫我吗？'])
            if index==2:
                return bot.send(event, [At(event.sender.id), ' 唉，怎么了。我做了什么奇怪的事情吗'])
            if index==3:
                return bot.send(event, [At(event.sender.id), ' 做什么呢'])


    @bot.on(GroupMessage)
    async def on_group_message(event: GroupMessage):
        if str(event.message_chain).endswith('亲亲') :
            index = random.randint(1, 4)
            if index==1:
                ranpath = random_str()
                out = sys.argv[0][:-20] + 'PythonPlugins\\plugins\\voices\\' + ranpath + '.wav'
                tex = '[JA]' + translate('不准亲......快走开，变态！~') + '[JA]'
                await bot.send(event,'不准亲，走开')
                await bot.send(event,Image(path=sys.argv[0][:-20] + 'PythonPlugins\\plugins\\PICTURE\\p2\\6.jpg'))
                voiceGenerate(tex, out)
                return bot.send(event, Voice(path=out))
            if index==2:
                ranpath = random_str()
                out = sys.argv[0][:-20] + 'PythonPlugins\\plugins\\voices\\' + ranpath + '.wav'
                tex = '[JA]' + translate('你是看到谁都想亲吗.....真是奇怪的人呢~') + '[JA]'
                await bot.send(event,'你是看到谁都想亲吗.....')
                await bot.send(event,Image(path=sys.argv[0][:-20] + 'PythonPlugins\\plugins\\PICTURE\\p2\\5.jpg'))
                voiceGenerate(tex, out)
                return bot.send(event, Voice(path=out))
            if index==3:
                ranpath = random_str()
                out = sys.argv[0][:-20] + 'PythonPlugins\\plugins\\voices\\' + ranpath + '.wav'
                tex = '[JA]' + translate('一块钱亲一口~，怎么样!?.......很划算吧') + '[JA]'
                await bot.send(event,Image(path=sys.argv[0][:-20] + 'PythonPlugins\\plugins\\PICTURE\\p2\\13.jpg'))
                voiceGenerate(tex, out)
                return bot.send(event, Voice(path=out))

        else:
            return


    @bot.on(GroupMessage)
    async def on_group_message(event: GroupMessage):
        if '对不对' in str(event.message_chain) :#or (('我是' in str(event.message_chain)) and str(event.message_chain).endswith('吗')):
            index = random.randint(1, 5)
            if index == 1:
                ranpath = random_str()
                out = sys.argv[0][:-20] + 'PythonPlugins\\plugins\\voices\\' + ranpath + '.wav'
                tex = '[JA]' + translate('当然是了！......笨蛋！.......这还用问吗~？') + '[JA]'
                #await bot.send(event, '')
                #await bot.send(event, Image(path=sys.argv[0][:-20] + 'PythonPlugins\\plugins\\PICTURE\\p2\\6.jpg'))
                voiceGenerate(tex, out)
                return bot.send(event, Voice(path=out))
            if index == 2:
                ranpath = random_str()
                out = sys.argv[0][:-20] + 'PythonPlugins\\plugins\\voices\\' + ranpath + '.wav'
                tex = '[JA]' + translate('不知道呢.......或许吧....') + '[JA]'
                #await bot.send(event, '你是看到谁都想亲吗.....')
                #await bot.send(event, Image(path=sys.argv[0][:-20] + 'PythonPlugins\\plugins\\PICTURE\\p2\\5.jpg'))
                voiceGenerate(tex, out)
                return bot.send(event, Voice(path=out))
            if index == 3:
                ranpath = random_str()
                out = sys.argv[0][:-20] + 'PythonPlugins\\plugins\\voices\\' + ranpath + '.wav'
                tex = '[JA]' + translate('应该是吧.....我感觉是的.....') + '[JA]'
                #await bot.send(event, Image(path=sys.argv[0][:-20] + 'PythonPlugins\\plugins\\PICTURE\\p2\\13.jpg'))
                voiceGenerate(tex, out)
                return bot.send(event, Voice(path=out))
            if index == 3:
                ranpath = random_str()
                out = sys.argv[0][:-20] + 'PythonPlugins\\plugins\\voices\\' + ranpath + '.wav'
                tex = '[JA]' + translate('绝对不是.....这样绝对很奇怪啊！.....') + '[JA]'
                #await bot.send(event, Image(path=sys.argv[0][:-20] + 'PythonPlugins\\plugins\\PICTURE\\p2\\13.jpg'))
                voiceGenerate(tex, out)
                return bot.send(event, Voice(path=out))

        else:
            return


    # 对日日的回复
    @bot.on(GroupMessage)
    async def on_group_message(event: GroupMessage):
        if str(event.message_chain)=='日日':
            index = random.randint(1, 11)
            if index == 1:
                await bot.send(event, [At(event.sender.id), ' 又开始了，又开始了......'])
                return bot.send(event,Image(path=sys.argv[0][:-20]+'PythonPlugins\\plugins\\PICTURE\\haiXiu\\11.jpg'))

            if index == 2:
                await bot.send(event, [At(event.sender.id), ' 唉，那个.....不行的吧！绝对不行的吧！'])
                return bot.send(event, Image(path=sys.argv[0][:-20]+'PythonPlugins\\plugins\\PICTURE\\haiXiu\\20.jpg'))
            if index == 3:
                ranpath = random_str()
                out = sys.argv[0][:-20]+'PythonPlugins\\plugins\\voices\\' + ranpath + '.wav'
                tex = '[JA]' + translate('你在想什么呢？') + '[JA]'
                voiceGenerate(tex, out)
                await bot.send(event, Image(path=sys.argv[0][:-20]+'PythonPlugins\\plugins\\PICTURE\\haiXiu\\12.jpg'))
                return bot.send(event, Voice(path=out))
            if index ==4:
                ranpath = random_str()
                out = sys.argv[0][:-20]+'PythonPlugins\\plugins\\voices\\' + ranpath + '.wav'
                tex = '[ZH]……哈~……哈~……嗯~……嗯啊~……不……不要~……咦咦咦啊啊啊啊啊啊~……[ZH]'
                voiceGenerate(tex, out)
                await bot.send(event, Image(path=sys.argv[0][:-20]+'PythonPlugins\\plugins\\PICTURE\\p2\\10.jpg'))
                return bot.send(event, Voice(path=out))
            if index ==5:
                await bot.send(event, Image(path=sys.argv[0][:-20]+'PythonPlugins\\plugins\\PICTURE\\haiXiu\\9.jpg'))
                return bot.send(event, [At(event.sender.id), ' 标记了一个变态:' + str(event.sender.id)] )
            if index ==6:
                ranpath = random_str()
                out = sys.argv[0][:-20]+'PythonPlugins\\plugins\\voices\\' + ranpath + '.wav'
                tex = '[JA]' + translate('这样很有趣呢！') + '[JA]'
                voiceGenerate(tex, out)
                await bot.send(event, Image(path=sys.argv[0][:-20]+'PythonPlugins\\plugins\\PICTURE\\haiXiu\\18.jpg'))
                return bot.send(event, Voice(path=out))
            if index ==7:
                ranpath = random_str()
                out = sys.argv[0][:-20]+'PythonPlugins\\plugins\\voices\\' + ranpath + '.wav'
                tex = '[JA]' + translate('不是很明白，这是什么意思呢？') + '[JA]'
                await bot.send(event, Image(path=sys.argv[0][:-20]+'PythonPlugins\\plugins\\PICTURE\\haiXiu\\4.jpg'))
                voiceGenerate(tex, out)
                return bot.send(event, Voice(path=out))
            if index ==8:
                ranpath = random_str()
                out = sys.argv[0][:-20]+'PythonPlugins\\plugins\\voices\\' + ranpath + '.wav'
                tex = '[JA]' + translate('你想说什么呢，我在听.....') + '[JA]'
                voiceGenerate(tex, out)
                await bot.send(event, Image(path=sys.argv[0][:-20]+'PythonPlugins\\plugins\\PICTURE\\haiXiu\\6.jpg'))
                return bot.send(event, Voice(path=out))
            if index ==9:
                await bot.send(event, Image(path=sys.argv[0][:-20]+'PythonPlugins\\plugins\\PICTURE\\haiXiu\\2.jpg'))
                return bot.send(event, '不懂了.....这到底是什么呢')
            if index==10:
                ranpath = random_str()
                out = sys.argv[0][:-20] + 'PythonPlugins\\plugins\\voices\\' + ranpath + '.wav'
                tex = '[JA]' + translate('笨蛋，变态，烦死了') + '[JA]'
                await bot.send(event, Image(path=sys.argv[0][:-20] + 'PythonPlugins\\plugins\\PICTURE\\p2\\9.jpg'))
                voiceGenerate(tex, out)
            if index>10:
                s=random.randint(1,20)
                si=str(s)
                return bot.send(event,Image(path=sys.argv[0][:-20]+'PythonPlugins\\plugins\\PICTURE\\haiXiu\\'+si+'.jpg'))


    #中文生成
    @bot.on(GroupMessage)
    async def handle_group_message(event: GroupMessage):
        if str(event.message_chain).startswith('中文'):
            if len(str(event.message_chain)) <280:
                ranpath = random_str()
                out = sys.argv[0][:-20]+'PythonPlugins\\plugins\\voices\\' + ranpath + '.wav'
                #out = 'D:\\Mirai\\Yiris\\PythonPlugins\\plugins\\voices\\01.wav'
                if(os.path.exists(out)):
                    os.remove(out)
                tex= '[ZH]'+((str(event.message_chain))[2:])+'[ZH]'
                voiceGenerate(tex,out)
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
        if  str(event.message_chain).startswith('说'):
            if len(str(event.message_chain)) <280:
                ranpath = random_str()
                out = sys.argv[0][:-20]+'PythonPlugins\\plugins\\voices\\' + ranpath + '.wav'
                tex = '[JA]' + translate((str(event.message_chain))[1:]) + '[JA]'
                voiceGenerate(tex, out)
                await bot.send(event,Voice(path=out))
            else:
                ranpath = random_str()
                out = sys.argv[0][:-20]+'PythonPlugins\\plugins\\voices\\' + ranpath + '.wav'
                tex = '[JA]' + translate('不行,太长了哦.....') + '[JA]'
                voiceGenerate(tex, out)
                await bot.send(event, Voice(path=out))

    bot.run()

