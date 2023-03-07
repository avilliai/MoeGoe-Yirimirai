# 更新
- 移除不必要的代码和文件。群内可切换音色
- 你可以导入自己的模型，在voiceModel文件夹下新建一个文件夹，把模型和配置文件放进去就好了。(多种语言的模型需要把后缀改成m.pth)
- 群内发送 voice 查看当前模型信息与使用提示
- 设置语音回复，可以参考[wReply](https://mirai.mamoe.net/topic/1842/%E4%BB%8E%E5%A4%96%E9%83%A8%E5%AF%BC%E5%85%A5%E8%AF%8D%E5%BA%93-%E5%8F%AF%E5%9C%A8%E7%BE%A4%E5%86%85%E7%AE%A1%E7%90%86-%E8%87%AA%E5%AE%9A%E4%B9%89%E5%9B%9E%E5%A4%8D)


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

发送 sp 查看当前可用的所有角色

# 导入更多模型(可选)

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
		
# config.json文件的修改

**以碧蓝档案的模型库为例**

*碧蓝档案模型库的模型大都是单角色，它的配置文件是多模型通用的，但为了更方便地使用，我们需要修改config.json*

**在[这个网站](https://www.xgjzx.cn/chinese)把角色的名称转成对应的unicode编码**

![633231ce-c8cf-43bb-8617-4acf44d24e45-image.png](/assets/uploads/files/1678196359711-633231ce-c8cf-43bb-8617-4acf44d24e45-image.png) 

打开config.json文件，把上一步得到的角色名称的unicode码填入speakers项。

**修改前："speakers":["这里是一大堆东西，全删掉"]**

![340501e5-4065-4d78-abfe-e8000dcd321d-image.png](/assets/uploads/files/1678196675709-340501e5-4065-4d78-abfe-e8000dcd321d-image.png) 

**修改后如图**

![71291c49-5ea4-4615-ac7a-4b80890bdfc6-image.png](/assets/uploads/files/1678196514483-71291c49-5ea4-4615-ac7a-4b80890bdfc6-image.png)

**需要注意

如果模型支持中日双语则需要把模型名从XXX.pth改成XXXm.pth**
