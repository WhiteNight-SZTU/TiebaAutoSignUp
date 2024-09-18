import logger
import json
import requests
import time
from login import get_cookies
import random
import hashlib

# PC端签到接口
# sign_url = "https://tieba.baidu.com/sign/add"

# 移动端签到接口
sign_url = "https://c.tieba.baidu.com/c/c/forum/sign"


# 单个贴吧签到
# tieba_name:贴吧名 tieba_url:贴吧链接
def tieba_sign_in(tieba_name, tieba_url, tbs, BDUSS):
    referer = tieba_url
    sign_str = f"kw={tieba_name}tbs={tbs}tiebaclient!!!"
    sign = hashlib.md5(sign_str.encode("utf-8")).hexdigest()
    payload = {
        "kw": tieba_name,
        "tbs": tbs,
        "sign": sign,
    }
    Cookies = {
        "BDUSS": BDUSS,
    }
    resp = requests.post(
        sign_url,
        cookies=Cookies,
        data=payload,
    )

    if "user_info" in resp.json():
        logger.debug("签到成功：" + tieba_name + "吧")
        return True
    elif resp.json()["error_code"] == "160002":
        logger.error("签到失败：" + tieba_name + "吧")
        logger.error("失败原因：" + resp.json()["error_msg"])
    else:
        logger.error("签到失败：" + tieba_name + "吧")
        logger.debug(str(resp.json()))
        logger.error("失败原因：" + resp.json()["error_msg"])
    return False


def sign_in():
    logger.info("开始签到")
    with open("tieba_dict.json", "r", encoding="utf-8") as f:
        tieba_dict = json.load(f)
    sign_sum, faliure_sum = 0, 0
    tbs, BDUSS, _ = get_cookies()
    for tieba_name, tieba_url in tieba_dict.items():
        if tieba_sign_in(tieba_name, tieba_url, tbs, BDUSS) == False:
            faliure_sum += 1
        sign_sum += 1
        logger.info("共计" + str(sign_sum) + "个吧")
        logger.info("当前已签到成功" + str(sign_sum - faliure_sum) + "个吧")
        time.sleep(random.randint(1, 5))

    logger.info("共计" + str(sign_sum) + "个贴吧")
    logger.info("成功" + str(sign_sum - faliure_sum) + "个")
    logger.info("失败" + str(faliure_sum) + "个")


if __name__ == "__main__":
    tieba_name = "余额宝"
    tieba_url = "https://tieba.baidu.com/f?kw=%D3%E0%B6%EE%B1%A6"
    logger.set_logger("debug")
    tieba_sign_in(tieba_name, tieba_url)
