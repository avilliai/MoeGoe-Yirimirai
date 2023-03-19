# 不 要 克 隆 仓 库
- 克隆仓库用不了,几个月没push过。用右上角release。
# 更新
- 支持导入模型，XX说
- 设置语音回复，可以参考[wReply](https://github.com/avilliai/wReply)

# Links
- 项目最核心的部分是CjangCjengh佬的[MoeGoe](https://github.com/CjangCjengh/MoeGoe)
- 基于[Yiri-mirai](https://github.com/YiriMiraiProject/YiriMirai)实现
- python版本推荐3.9  不推荐python3.10
- 请确保已安装[mirai-api-http](https://github.com/project-mirai/mirai-api-http)


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
 - 下载Release,不要克隆仓库
 
 - 解压，安装压缩包里的python

 - 进入bot.py所在目录，打开cmd运行如下命令

   	pip install -r requirements.txt

 - 修改config.json并运行bot.py(修改port、key与你的mirai-api-http需要保持一致)

	发送 voice 查看帮助菜单

	发送 sp 查看当前可用的所有角色

# 导入更多模型(可选)

在voiceModel文件夹下新建文件夹，把.pth(模型文件)和config.json(配置文件)放进去

下载模型
        
下载模型
        
[碧蓝档案主题模型](https://www.bilibili.com/video/BV1wG4y1M7SL/?spm_id_from=333.999.0.0)
            
[CjangCjengh的模型仓库](https://github.com/CjangCjengh/TTSModels)

[**已修改配置文件的模型仓库**](https://pan.baidu.com/s/1bEbDMv0Ysj0cRmwHi6WAyA?pwd=9rmj),下载后放在项目对应文件夹下即可。
            

	模型命名规则(重要)：
		多语种模型：后缀名前面加一个m,如yuuka.pth支持中日双语，则改成yuukam.pth
		单语种模型：不用改名

	配置文件修改：
		模型来自saya佬：打开config.json修改speakers，把一大串speakers修改为一个(名称随意) | 中文名的speaker需要转unicode | https://www.xgjzx.cn/chinese
		模型来自CjangCjengh：直接用
		
# 模型名称与config.json文件的修改(导入模型的详解)

**以碧蓝档案的模型库为例**

*碧蓝档案模型库的模型大都是单角色，它的配置文件是多模型通用的，但为了更方便地使用，我们需要修改config.json*

**在[这个网站](https://www.xgjzx.cn/chinese)把角色的名称转成对应的unicode编码**

![image](https://user-images.githubusercontent.com/99066610/223444528-6095f225-f9f6-4154-af3b-ecfd120fd563.png)


打开config.json文件，把上一步得到的角色名称的unicode码填入speakers项。

**修改前："speakers":["这里是一大堆东西，全删掉"]**

![image](https://user-images.githubusercontent.com/99066610/223444630-8c5e2a02-df4d-488a-954d-a68c92d3e491.png)


**修改后："speakers": ["\u963f\u55b5\u55b5"]**

![image](https://user-images.githubusercontent.com/99066610/223444725-4a6fe6f6-9225-4cd4-aa1b-7277b92d89f9.png)


**需要注意**

如果模型支持中日双语则需要把模型名从XXX.pth改成XXXm.pth
