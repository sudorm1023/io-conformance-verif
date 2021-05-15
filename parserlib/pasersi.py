"""
该模块中函数用来获取*.si文件中自动机表示
"""

import os.path


def read_si(file_name: str) -> str:
    if not os.path.exists(file_name):
        print("[!] Error: {} is not exist!".format(os.path.abspath(file_name)))
        exit(0)

    with open(file_name, mode='r') as f:
        return f.read()
