"""
Author: Night-stars-1 19710015@qq.com
Date: 2024-08-20 22:17:31
LastEditors: Night-stars-1 19710015@qq.com
LastEditTime: 2025-03-28 16:00:51
"""

import platform
from urllib.request import getproxies
from datetime import datetime  # 新增导入

from utils.logger import log


def print_info():
    """打印系统信息"""
    current_date = datetime.now().strftime("%Y-%m-%d")  # 获取当前日期并格式化
    log.info(current_date)  # 替换为日期
    log.info("---------- 系统信息 -------------")
    system_info()
    log.info("---------- 运行日志 -------------")


def system_info():
    """系统信息"""
    log.info(show_info("系统平台", platform.platform()))
    log.info(
        show_info(
            "Python 版本",
            str(platform.python_version()),
        )
    )
    if getproxies():
        log.info(show_info("系统代理", getproxies()))


def show_info(tip: str, info: str):
    """格式化输出"""
    return f"{tip}: {info}"
