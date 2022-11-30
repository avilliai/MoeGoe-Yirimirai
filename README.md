# 更新
- 移除不必要的代码和文件。群内可切换语音模型


# Links
- 项目最核心的部分是CjangCjengh佬的[MoeGoe](https://github.com/CjangCjengh/MoeGoe)
- 基于[Yiri-mirai](https://github.com/YiriMiraiProject/YiriMirai)实现
- python版本推荐3.9  不推荐python3.10
- 下载模型并放在voiceModel文件夹下[Pretrained models](https://sjtueducn-my.sharepoint.com/personal/cjang_cjengh_sjtu_edu_cn/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fcjang%5Fcjengh%5Fsjtu%5Fedu%5Fcn%2FDocuments%2Fvits%5Fmodels%2Fnene%2Bnanami%2Brong%2Btang%2F1374%5Fepochs%2Epth&parent=%2Fpersonal%2Fcjang%5Fcjengh%5Fsjtu%5Fedu%5Fcn%2FDocuments%2Fvits%5Fmodels%2Fnene%2Bnanami%2Brong%2Btang&ga=1)
- 请确保已安装[mirai-api-http](https://github.com/project-mirai/mirai-api-http)
- 使用release的话就不用再下载模型了


# 可能的问题

    1
    
      FileNotFoundError[Errno 2]: No such............ 
      
      解决：out = sys.argv[0][:-20] + 'PythonPlugins\\plugins\\voices\\' + ranpath + '.wav'
      
            替换成
            
           out='绝对路径\\PythonPlugins\\plugins\\voices\\' + ranpath + '.wav'
           
    2
    
      ModuleNotFoundError: no module named 'XXX'
      
      解决：缺包，执行如下命令 
      
      pip install XXX
      
    3
    
      TyreError: run() got an unexpected keyword argument 'debug'
      
      解决：python版本不对，推荐换3.9
      
    4
    
      ConnectionRefusedError: [WinError 1225] 远程网络计算机拒绝连接
      
      解决：bot.py的port,key,botqq与mirai-api-http配置不一致，修改对应即可
    5
      AttributeError:........
      推测是和现有的包有冲突，不知道。换个解释器试试。实在不行用venv文件夹里的玩意替换本地的。
      
# How to use
下载Release或
克隆仓库到本地(克隆记得去下载模型)

    根目录是PythonPlugins

    不是的话就修改成这样

    PythonPlugins\\bot.py

打开cmd运行如下命令

   pip install -r requirements.txt

修改并运行bot.py(修改QQ为你bot的QQ,port、key与你的mirai-api-http需要保持一致)



发送语音指令如下：
-


向指定目标发送命令（私聊窗口用，先连接群或好友才能发送）

      发送×××

中文生成（群内可用）

      中文
日语生成（群内可用，改触发命令可以从bot.py改）

      说

向群聊发送（私聊用群号为示例）

       连接群#699455559
向个人发送（由于腾讯更新私聊语音加密，不能用了）

        连接对象#1840094972

语言切换

         切换中文
         切换日语
 
模型切换

          M#0
          M#1
          M#2
          M#3
附加小功能

         /pic数字
 
