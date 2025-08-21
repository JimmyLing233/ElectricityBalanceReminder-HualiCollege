<div align="center">
<h1>ElectricityBalanceReminder-HualiCollege</h1>
适用于广东工业大学华立学院（广州华立学院）的自动电费余额提醒脚本<br><br>
  
[![Licence](https://img.shields.io/badge/LICENSE-MIT-green.svg?style=for-the-badge)](LICENSE)

</div>

## 环境依赖
**Python版本 >= 3.6**

### 通过 pip 安装依赖
```bash
pip install requests
```
## 配置
1. 关注“华立生活”微信公众号
2. 进入“华立电表”并选择类型和校区
3. 在我的信息中绑定电表
4. 返回“用户中心”，在点击“缴费查询”后不要等待加载直接点击右上角三个点复制链接（如果没有此选项请重复此步骤，手速一定要快）
5. 你会得到形如下述的一串链接，请记下memid、openid、operatorcode里（“=”后，“&”前）的参数
```url
https://dbwx.hlsywy.com/web/MWeb/payusereqlist.aspx?type=2&memid=xxx&openid=xxxxxxxxxxxxxxx&operatorcode=XXXX
```
6. 注册server酱服务（推荐）

https://sct.ftqq.com/
选择推送方式并获取apikey
您也可以采用其他的方式推送，但可能需要自行修改代码

7. 修改文件中的参数部分
```python
# 配置参数
# 以下参数填写时请去除<>及其中的内容
config = {
    "openid": "<openid>", # 参考教程中的获取方法
    "memid": "<memid>", # 参考教程中的获取方法
    "operatorcode": "<operatorcode>", # 校区编号？参考教程中的获取方法
    "sct_key": "<key>", # server酱推送key，请事先注册
    "reminder_threshold": 50  # 余额提醒阈值（低于此值将推送提醒）
}
```
## 运行
此脚本支持本地运行和[青龙面板](https://github.com/whyour/qinglong)。
也可以尝试将其部署于云函数等方式运行（请自行测试）

### 本地运行
```bash
python ./ElectricityBalanceReminder.py
```

### 青龙面板
1. 点击左边栏“订阅管理”
2. 点击右上角“创建订阅”
3. 依次将以下内容输入至其中
```text
名称：<自拟>
链接：https://github.com/JimmyLing233/ElectricityBalanceReminder-HualiCollege.git
定时规则：2 2 28 * *
白名单：ElectricityBalanceReminder
文件后缀：py
```
4. 点击“确定”后点击“运行”等待拉取，拉取成功后请点击右侧三个点并选择“禁用”避免后续自动拉取导致的配置清空。
5. 点击左边栏“定时任务”找到刚才拉取的项目
6. 点击“命令/脚本”栏目下的链接跳转至文件编辑界面按照上述修改文件中的参数部分。
7. 您可以返回“定时任务”中测试并调整定时运行配置

## 免责声明
**本工具仅供学习和研究使用，使用本工具所产生的任何后果由使用者自行承担。<br>
本工具僅供學習和研究使用，使用本工具所產生的任何後果由使用者自行承擔。<br>
This tool is only for learning and research purposes, and any consequences arising from the use of this tool are borne by the user.**

## 许可证
[MIT License](LICENSE)
