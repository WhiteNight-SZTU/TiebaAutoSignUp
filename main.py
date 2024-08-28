import argparse
import logger
import os
from login import get_tieba_dict
from sign import sign_up


def parser():
    parser = argparse.ArgumentParser(description="自动签到")
    parser.add_argument(
        "-r",
        "--refresh",
        type=bool,
        help="是否刷新需要签到的贴吧，默认false。第一次运行时会自动将需要签到的贴吧保存到tieba_dict.json文件中。",
        default=False,
    )
    parser.add_argument(
        "--log", help="日志级别，默认INFO。可选info/debug", default="info"
    )
    return parser.parse_args()


def main():
    args = parser()
    logger.set_logger(args.log)
    if args.refresh == True:
        get_tieba_dict()
    if os.path.exists("tieba_dict.json"):
        sign_up()
    else:
        get_tieba_dict()
        sign_up()


if __name__ == "__main__":
    main()
