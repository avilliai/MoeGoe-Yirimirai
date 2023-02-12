# 更新
- 移除不必要的代码和文件。群内可切换音色
- 你可以导入自己的模型，在voiceModel文件夹下新建一个文件夹，把模型和配置文件放进去就好了。(多种语言的模型需要把后缀改成m.pth)
- 群内发送 voice 查看当前模型信息与使用提示


# Links
- 项目最核心的部分是CjangCjengh佬的[MoeGoe](https://github.com/CjangCjengh/MoeGoe)
- 基于[Yiri-mirai](https://github.com/YiriMiraiProject/YiriMirai)实现
- python版本推荐3.9  不推荐python3.10
- 1374模型来自[Pretrained models](https://sjtueducn-my.sharepoint.com/personal/cjang_cjengh_sjtu_edu_cn/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fcjang%5Fcjengh%5Fsjtu%5Fedu%5Fcn%2FDocuments%2Fvits%5Fmodels%2Fnene%2Bnanami%2Brong%2Btang%2F1374%5Fepochs%2Epth&parent=%2Fpersonal%2Fcjang%5Fcjengh%5Fsjtu%5Fedu%5Fcn%2FDocuments%2Fvits%5Fmodels%2Fnene%2Bnanami%2Brong%2Btang&ga=1)
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
      推测是和现有的包有冲突，不知道。换个解释器试试。实在不行下载site-package并解压替换本地的site-package。
      
# How to use
下载Release,不要克隆仓库

打开cmd运行如下命令

   pip install -r requirements.txt

修改并运行bot.py(修改port、key与你的mirai-api-http需要保持一致)

发送 voice 查看帮助菜单

# 导入模型

在voiceModel文件夹下新建文件夹，把.pth(模型文件)和config.json(配置文件)放进去

下载模型
        
[碧蓝档案主题](https://www.bilibili.com/video/BV1wG4y1M7SL/?spm_id_from=333.999.0.0)
            
[CjangCjengh的模型仓库](https://github.com/CjangCjengh/TTSModels)
            

	模型命名规则(重要)：
		多语种模型：后缀名前面加一个m,如yuuka.pth支持中日双语，则改成yuukam.pth
		单语种模型：不用改名

	配置文件修改：
		模型来自saya佬：打开config.json修改speakers，把一大串speakers修改为一个(名称随意) | 中文名的speaker需要转unicode | https://www.xgjzx.cn/chinese
		模型来自CjangCjengh：直接用
		
