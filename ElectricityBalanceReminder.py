import requests

def get_balance_info(openid, memid, operatorcode):
    base_url = "https://dbwx.hlsywy.com/web/MWeb/payusereqlist.aspx" # 电费接口
    query_params = {
        "_r": "show", # 开启格式化json输出
        "type": "1",
        "memid": memid,
        "openid": openid,
        "operatorcode": operatorcode
    }
    url = f"{base_url}?{requests.compat.urlencode(query_params)}"

    try:
        response = requests.get(url)
        if response.status_code == 200: # 检查请求是否成功
            data = response.json()
            if data.get("RtnCode") == 9999: # 检查接口是否返回9999
                user_data_body = data.get("UserDataBody") # 提取用户数据
                if user_data_body: # 检查数据
                    meter_data_body = user_data_body[0].get("MeterDataBody")
                    if meter_data_body:
                        remnant = meter_data_body[0].get("Remnant") # 提取剩余电费（Remnant字段）
                        return remnant if remnant is not None else "未找到电费余额信息" # 返回余额或未找到信息的提示
                    return "未找到电表相关信息" # 电表数据为空
                return "用户信息不存在，请检查户号" # 用户数据为空
            return f"获得用户信息失败: {data.get('RtnMsg', '未知错误原因')}" # 接口返回错误
        return f"请求失败，状态码：{response.status_code}" # 接口调用错误
    except requests.exceptions.RequestException as e: # 网络错误
        return f"请求发生异常: {e}"


def send_balance_reminder(message, sct_key):
    # 此处调用server酱服务https://sct.ftqq.com/。您也可以改为使用serverChan3，https://sc3.ft07.com/。
    chanurl = f'https://sctapi.ftqq.com/{sct_key}.send'
    params = {'title': '电费余额提醒', 'desp': message}
    return requests.get(chanurl, params=params).text


# 配置参数
# 以下参数填写时请去除<>及其中的内容
config = {
    "openid": "<openid>",
    "memid": "<memid>", # 参考教程中的获取方法
    "operatorcode": "<operatorcode>", # 校区编号？参考教程中的获取方法
    "sct_key": "<key>", # server酱推送key，请事先注册
    "reminder_threshold": 50  # 余额提醒阈值（低于此值将推送提醒）
}

balance_info = get_balance_info(
    config["openid"],
    config["memid"],
    config["operatorcode"]
)

if isinstance(balance_info, (int, float)):
    if balance_info < config["reminder_threshold"]:
        send_response = send_balance_reminder(
            f"用户电费余额为: {balance_info} 元",
            config["sct_key"]
        )
        print(f"当前电费余额 {balance_info} 元，提醒已发送: {send_response}")
    else:
        print(f"当前电费余额 {balance_info} 元，无需提醒。")
else:
    error_message = f"无法获取电费余额数据: {balance_info}"
    send_response = send_balance_reminder(error_message, config["sct_key"])
    print(f"出错提醒已发送: {send_response}")
