# 功能介绍：

Make Run Once是超级斜杠开发的，一款能够帮助大家方便触发Make自动化工作流运行的小工具。大家平时是否会觉得搭建好的Make自动化工作流，想要让其按需运行时，每次都要进入到Make后台点击Run Once，这种方式太麻烦了，使用Make Run Once小工具仅能解决这个问题！

# 运行原理：
Make Run Once的原理是调用Make的官方API接口，触发特定的工作流运行，因此，你的Make账号需要是付费套餐才可以使用，此外，你还需要按照下方的使用教程，完成按钮的配置。
![image001](https://github.com/superslash-rico/MakeRunOnce/blob/main/readme/001.png)


# 小工具地址：

https://me.superslash.cn
（建议将其保存为浏览器书签，或者添加到浏览器收藏栏，方便使用)

# 使用教程：
1.进入小工具，点击右下角的“+”号，添加按钮，需要对按钮进行配置：区域 URL *、API Token *、Scenario ID *、Data (可选，JSON 格式)、按钮名称 *、按钮备注、按钮图标、按钮颜色。
![image002](https://github.com/superslash-rico/MakeRunOnce/blob/main/readme/002.gif)

- 区域 URL *：选择你的make账号的基础域名URL，登录你的Make账号，在浏览器地址栏就能看到，不同人的账号的域名URL是不一样的，请根据自己的填写，如下图我的是：us2.make.com，我就选择对应的区域URL。
![image0031](https://github.com/superslash-rico/MakeRunOnce/blob/main/readme/0031.png)
![image003](https://github.com/superslash-rico/MakeRunOnce/blob/main/readme/003.png)

- API Token *：指的是API key，登录make，依次点击“右上角头像—Profile—API access—Add Token”，新建一个token，选择全部权限，然后点击Add，创建好的Token只会出现一次，请妥善保存，并且不要分享给其他人。
![image004](https://github.com/superslash-rico/MakeRunOnce/blob/main/readme/004.png)
![image0041](https://github.com/superslash-rico/MakeRunOnce/blob/main/readme/0041.png)
![image0051](https://github.com/superslash-rico/MakeRunOnce/blob/main/readme/0051.png)
![image005](https://github.com/superslash-rico/MakeRunOnce/blob/main/readme/005.png)

- Scenario ID *：即要运行的工作流的专属ID，进入要运行的工作流，在浏览器地址栏中可以看到这个ID，如下图所示：
![image0061](https://github.com/superslash-rico/MakeRunOnce/blob/main/readme/0061.png)
![image006](https://github.com/superslash-rico/MakeRunOnce/blob/main/readme/006.png)

- Data (可选，JSON 格式)：你的工作流是否设置了输入参数？如果没有设置，则不需要填写，如果设置了，则必须根据输入参数的数据结构进行填写！
![image007](https://github.com/superslash-rico/MakeRunOnce/blob/main/readme/007.png)
![image008](https://github.com/superslash-rico/MakeRunOnce/blob/main/readme/008.png)
![image009](https://github.com/superslash-rico/MakeRunOnce/blob/main/readme/009.png)
![image010](https://github.com/superslash-rico/MakeRunOnce/blob/main/readme/010.png)

- 按钮名称 *、按钮备注、按钮图标、按钮颜色：设置其他按钮选项，方便识别。
![image011](https://github.com/superslash-rico/MakeRunOnce/blob/main/readme/011.gif)

添加好的按钮如下，可以重复上述操作添加多个按钮。
![image012](https://github.com/superslash-rico/MakeRunOnce/blob/main/readme/012.gif)










