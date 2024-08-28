import logger
import json
import requests
import time
from login import get_cookies

# 签到接口
sign_url = "https://tieba.baidu.com/sign/add"


# 单个贴吧签到
# tieba_name:贴吧名 tieba_url:贴吧链接
def tieba_sign_up(tieba_name, tieba_url):
    referer = tieba_url
    BDUSS, STOKEN = get_cookies()
    payload = {
        "ie": "utf-8",
        "kw": tieba_name,
    }
    Cookies = {
        "BDUSS": BDUSS,
        "STOKEN": STOKEN,
    }
    resp = requests.post(
        sign_url, cookies=Cookies, headers={"Referer": referer}, data=payload
    )
    # 1101表示重复签到
    if resp.json()["no"] == 0 or resp.json()["no"] == 1101:
        logger.debug("签到成功：" + tieba_name + "吧")
        return True
    else:
        logger.error("签到失败：" + tieba_name + "吧")
        logger.error("失败原因：" + resp.json()["error"])
    return False


def sign_up():
    logger.info("开始签到")
    with open("tieba_dict.json", "r", encoding="utf-8") as f:
        tieba_dict = json.load(f)
    sign_sum = 0
    faliure_sum = 0
    for tieba_name, tieba_url in tieba_dict.items():
        time.sleep(1)
        if tieba_sign_up(tieba_name, tieba_url) == False:
            faliure_sum += 1
        sign_sum += 1
    logger.info("共计" + str(sign_sum) + "个贴吧")
    logger.info("成功" + str(sign_sum - faliure_sum) + "个")
    logger.info("失败" + str(faliure_sum) + "个")


if __name__ == "__main__":
    tieba_name = "net"
    tieba_url = "https://tieba.baidu.com/f?kw=net"
    logger.set_logger("debug")
    tieba_sign_up(tieba_name, tieba_url)
