# NoMoeny

------



<div align=center>
    <img alt="Platform" src="https://img.shields.io/badge/platform-windows-blue">
    <img alt="Platform" src="https://img.shields.io/badge/platform-Linux-blue">
    <img alt="Python Version" src="https://img.shields.io/badge/python-3.8.6-yellow">
    <img alt="GitHub" src="https://img.shields.io/github/license/jorhelp/Ingram">
</div>



## About

NoMoney is an information collection tool that integrates Fofa, <del>Zoomeye (Zhong Kui's Eye), Centsys,</del> Qi'anxin's Yingtu platform, and 360quake. From this name, it can be seen that the scope of this tool is free on all platforms mentioned above. Among them, fofa <del>and  zoomeye</del> are based on web crawler to obtain data, while other major platforms have corresponding free apis, but there are certain query restrictions.



##  Introduction to various platforms 



|                     Platform                     | Is there a free API available |                      Query Restrictions                      |
|:------------------------------------------------:| :---------------------------: | :----------------------------------------------------------: |
|            [fofa](https://fofa.info/)            |               ❌               | Registered users can view the first <b>60</b> data items for free every time they use the webpage |
| <del> [Zoomeye (钟馗之眼)](https://www.zoomeye.org/) |         <del>      ✔               | <del>Web browsing <b>allows you to view the first <b>400</b> pieces of data each time</b>. The API <b>supports querying <b>10000</b>pieces of data per month</b>, and the web page is not associated with the API |
|  [qianxin (鹰图平台)](https://hunter.qianxin.com/)   |               ✔               | API supports querying <b>500</b> data items daily, but website queries also deduct points |
|   <del>    [Censys](https://search.censys.io/)        |    <del>           ✔               | <del>API supports querying <b>250</b> data items per month, but website queries also deduct points |
|  [360quake](https://quake.360.net/quake/#/index)  |               ✔               | API supports <b>3000</b> data points per month, and no points will be deducted for webpage queries |

## Module

- fofa: Simulate crawling to obtain data using the playwright browser, with a maximum of 60 entries obtained at a time.
- <del>Zoomeye（钟馗之眼）:The browser simulates crawling to obtain data, with a maximum of 400 entries per session; The API functionality is currently incomplete, please stay tuned.
- qianxin（鹰图平台）: API data acquisition, 500 points per day.
- 360quake: API obtains data with 3000 points per month, and offers 5 free query opportunities per month. A single query can obtain up to 400 pieces of data.
- <del>Censys: API to obtain data, foreign websites, may be slower, with 250 points per month.



## Install

  **Windows/Linux platform. Please ensure that Python version 3.7 and above is installed, recommended version 3.8**

- clone the depository:

```shell
git clone https://github.com/H-Limbus/NoMoney.git
```

- Installation dependency (in China, please remember to replace the domestic image source before installing dependency, otherwise it will be particularly slow)：

```shell
pip3 install -r requirements.txt
```

- After the dependency installation is complete, use `python NoMoney.py -fU`, and if the following error occurs, use the `playwright install` command to install it:
![img](https://cdn.jsdelivr.net/gh/H-Limbus/myBlogImage/img/202409170250442.png)

- Installation completed.



## Run

- use -h or --help for viewing help

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
  -q, --qianxin         yingtu api
  -3, --360-quake       360quake api
  -U, --UpdateCookie    update the cookie
  -r, --rules           the api search rules
  -o OUTPUT, --output OUTPUT
                        Output file
  --format FORMAT       Report format (Available: txt, json, csv), default txt
```

- Before running the program, we need to configure the accounts of our various platforms and register to obtain：

```python

#                                   """can change"""
# =======================================================================================

# fofa account and password 
FOFA_USER = ''
FOFA_PASS = ''

# qianxin（奇安信）api-key（After logging in, you can obtain）
QIANXIN_API_KEY = ''

# 360_quake 的api（After logging in, you can obtain）
QUAKE_API = ''

# PlayWright 的启动配置
browserHeadless = False
```

- We can view the search syntax rules of different platforms：

```shell
python NoMoney.py -fr  or  -f -r 
```
![image-20240917025424436](https://cdn.jsdelivr.net/gh/H-Limbus/myBlogImage/img/202409170254971.png)



- update cookies for fofa <del>and zoomeye</del> ：

```shell
python3 NoMoney.py -fU
# The webpage will be automatically updated and the verification code to be filled in will be automatically recognized.

# After the cookies are updated, they are no different from other APIs when used.
```

- get data：

```shell
python NoMoney.py -f or -q or -3 or -fq3 (Multi platform query)
```

- Save data in three formats (txt CSV JSON, default to txt)：

```shell
python NoMoney.py -f -o filepath --format=txt
```

- Disadvantage: Due to many platforms detecting and preventing access speed from being too fast, the speed may be slightly slower.



## Disclaimers

This tool is for safety testing only and is strictly prohibited from being used for illegal purposes. The consequences are not my responsibility.



## Acknowledgement&Application

thanks to [sml2h3](https://github.com/sml2h3) for ddddocr



## License

<img alt="GitHub" src="https://img.shields.io/github/license/jorhelp/Ingram">

