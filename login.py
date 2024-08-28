import requests
import re
import json
import os
import logger

prefix = "https://tieba.baidu.com"
url = "https://tieba.baidu.com/f/like/mylike"


def get_cookies():
    BDUSS, STOKEN = "", ""
    if os.path.exists("test_account.json"):
        with open("test_account.json", "r", encoding="utf-8") as f:
            account = json.load(f)
            BDUSS = account["BDUSS"]
            STOKEN = account["STOKEN"]
    elif os.path.exists("account.json"):
        with open("account.json", "r", encoding="utf-8") as f:
            account = json.load(f)
            BDUSS = account["BDUSS"]
            STOKEN = account["STOKEN"]
    else:
        raise Exception("未找到BDUSS或STOKEN")
    logger.debug("获取BDUSS和STOKEN成功")
    return BDUSS, STOKEN


# 从百度贴吧获取关注的贴吧列表
# 结果保存到tieba_dict.json文件中
def get_tieba_dict():
    tieba_dict = {}
    BDUSS, STOKEN = get_cookies()
    Cookies = {
        "BDUSS": BDUSS,
        "STOKEN": STOKEN,
    }
    page = 1
    tieba_sum = 0
    while True:
        mylike_url = "https://tieba.baidu.com/f/like/mylike?&pn=" + str(page)
        try:
            response = requests.get(mylike_url, cookies=Cookies)
        except Exception as e:
            raise Exception("请求失败：" + str(e))
        data = extract_data(response.text)
        if data == []:
            break
        for i in data:
            tieba_name = re.search(r"<a.*?>(.*?)</a>", i).group(1)
            tieba_url = prefix + re.search(r"href=\"(.*?)\"", i).group(1)
            if tieba_name is not None:
                tieba_sum += 1
            tieba_dict[tieba_name] = tieba_url
        page += 1
    with open("tieba_dict.json", "w", encoding="utf-8") as f:
        json.dump(tieba_dict, f, ensure_ascii=False)
    logger.info("获取贴吧列表成功")
    logger.info("共获取到" + str(tieba_sum) + "个贴吧")


def extract_data(html_content: str):
    rows = re.findall(r"<tr>(.*?)</tr>", html_content, re.DOTALL)
    data = []
    for row in rows:
        first_td = re.search(r"<td>(.*?)</td>", row, re.DOTALL)
        if first_td:
            data.append(first_td.group(1))
    return data


if __name__ == "__main__":
    logger.set_logger("debug")
    get_tieba_dict()
