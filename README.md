# NoMoeny

------



<div align=center>
    <img alt="Platform" src="https://img.shields.io/badge/platform-windows-blue">
    <img alt="Python Version" src="https://img.shields.io/badge/python-3.8.6-yellow">
    <img alt="GitHub" src="https://img.shields.io/github/license/jorhelp/Ingram">
</div>



## 关于

NoMoney 是一款信息收集的工具，其中集成了fofa，zoomeye(钟馗之眼)，censys，奇安信的鹰图平台，360quake。从这个名字就可以看出，这款工具涉及的范围在以上平台中都是<b>免费</b>的。其中fofa 与zoomeye 是基于网络爬虫获取数据，而其余各大平台都有相对应的免费api，但是有一定的查询限制。



## 各平台介绍



|                       平台                        | 是否有免费API |                           查询限制                           |
| :-----------------------------------------------: | :-----------: | :----------------------------------------------------------: |
|            [fofa](https://fofa.info/)             |       ❌       |  注册用户使用网页<b>每次</b>可以免费查看前 <b>60</b> 条数据  |
|  [zoomeye (钟馗之眼)](https://www.zoomeye.org/)   |       ✔       | 网页浏览<b>每次</b>可以看前<b>400</b>条数据，API <b>每月</b>支持查询<b>10000</b>条数据，且网页与API 互不关联 |
| [qianxin (鹰图平台)](https://hunter.qianxin.com/) |       ✔       | API <b>每日</b>支持查询 <b>500</b> 条数据，但网页查询也会扣除积分 |
| [censys](https://search.censys.io/)              |       ✔       | API<b>每月</b>支持查询<b>250</b>条数据，但网页查询也会扣除积分 |
|  [360uake](https://quake.360.net/quake/#/index)   |       ✔       |       API 每月支持<b>3000</b>条数据，网页查询不扣积分        |

## 项目模块

- fofa：利用pyppeteer浏览器模拟爬虫获取数据，每次最多获取60条。
- zoomeye（钟馗之眼）: 浏览器模拟爬虫获取数据，每次最多获取400条；API 功能暂未完成，敬请期待。
- qianxin（鹰图平台）API获取数据，每日500积分。
- 360quake API 获取数据，每月3000积分，每月会送5次免费查询机会，单次查询最多获取400条数据。
- censys API获取数据，国外网站，速度可能较慢，每月有250积分。



## 安装

  **Windows 平台使用。请确保安装了3.7及以上版本的Python，推荐3.8**

- 克隆该仓库:

```shell
git clone https://github.com/H-Limbus/NoMoney.git
```

- 安装依赖（在中国的话，安装依赖之前切记更换国内镜像源，否则会特别慢）：

```shell
pip3 install -r requirements.txt

在过程中可能pywin32安装不成功，请手动安装 pip3 install pywin32
```

- 安装完毕。



## 运行

- 使用 -h 或者 --help 来查看相关功能

```shell
        ___           ___           ___           ___           ___           ___
       /__/\         /  /\         /__/\         /  /\         /__/\         /  /\          ___
       \  \:\       /  /::\       |  |::\       /  /::\        \  \:\       /  /:/_        /__/|
        \  \:\     /  /:/\:\      |  |:|:\     /  /:/\:\        \  \:\     /  /:/ /\      |  |:|
    _____\__\:\   /  /:/  \:\   __|__|:|\:\   /  /:/  \:\   _____\__\:\   /  /:/ /:/_     |  |:|
   /__/::::::::\ /__/:/ \__\:\ /__/::::| \:\ /__/:/ \__\:\ /__/::::::::\ /__/:/ /:/ /\  __|__|:|
   \  \:\~~\~~\/ \  \:\ /  /:/ \  \:\~~\__\/ \  \:\ /  /:/ \  \:\~~\~~\/ \  \:\/:/ /:/ /__/::::\
    \  \:\  ~~~   \  \:\  /:/   \  \:\        \  \:\  /:/   \  \:\  ~~~   \  \::/ /:/     ~\~~\:\
     \  \:\        \  \:\/:/     \  \:\        \  \:\/:/     \  \:\        \  \:\/:/        \  \:\
      \  \:\        \  \::/       \  \:\        \  \::/       \  \:\        \  \::/          \__\/
       \__\/         \__\/         \__\/         \__\/         \__\/         \__\/

usage: No Money

Because I have no money, I have this script( Part of the API of this script is crawler)

optional arguments:
  -h, --help            show this help message and exit
  -f, --fofa            fofa api
  -z, --zoomeye         zoomeye api
  -c, --Censys          censys api
  -q, --qianxin         yingtu api
  -3, --360-quake       360quake api
  -U, --UpdateCookie    update the cookie
  -r, --rules           the api search rules
  -o OUTPUT, --output OUTPUT
                        Output file
  --format FORMAT       Report format (Available: txt, json, csv), default txt
```

- 在程序运行之前，我们需要配置我们各个平台的账号，需要注册获取：

```python

#                                   """can change"""
# =======================================================================================

# fofa 账号密码
FOFA_USER = ''
FOFA_PASS = ''

# zooyeye（钟馗之眼）账号密码
ZOOMEYE_USER = ''
ZOOMEYE_PASS = ''

# qianxin（奇安信）api-key（登录之后就可以获取）
QIANXIN_API_KEY = ''

# 360_quake 的api（登录之后就可以获取）
QUAKE_API = ''

# censys的api（登录之后就可以获取）
CENSYS_EMAIL = ''
CENSYS_API = ''
CENSYS_SCRECT = ''

# 当前的路径
CURRENT_PATH = os.getcwd()
```

- 我们可以查看不同平台的搜索语法规则：

```shell
python NoMoney.py -fr    或者  -f -r 
```
![图片](https://user-images.githubusercontent.com/85352537/224474391-7e5e5e26-5334-4409-b616-f7ab4e387bd6.png)



- 更新 fofa 和 zoomeye 的cookies ：

```shell
python3 NoMoney.py -fU  或者  -zU
# 网页会自动进行更新，会自动识别所要填的验证码
# fofa 的验证码识别率较高，但是zoomeye 识别率很低，所以在识别错误几次之后会弹出验证码进行手动输入，这确保在无头模式下也可以手动输入
# 当cookies更新之后，使用时就和其他 api 没什么不同了。
```

- 获取数据：

```shell
python NoMoney.py -f 或者 -z 或者 -q 或者 -3 或者 -c 或者 -fzq3c （多平台查询）
```

- 保存数据，可选择三种格式（txt  csv  json ，默认为 txt ）：

```shell
python NoMoney.py -f -o filepath --format=txt
```

- 缺点：由于很多平台会检测防止访问速度过快，速度上可能会稍微比较慢。



## 免责声明

本工具仅供安全测试，严禁用于非法用途，后果与本人无关。



## 鸣谢&应用

thanks to [sml2h3](https://github.com/sml2h3) for ddddocr



## License

<img alt="GitHub" src="https://img.shields.io/github/license/jorhelp/Ingram">

