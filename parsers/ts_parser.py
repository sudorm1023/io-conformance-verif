#!/usr/bin/env python3

from ts import LTS
from parsers.tsparsers import parse_ts_type
from constants import TS_TYPE
from parsers.tsparsers import lts_parser
from parsers.tsparsers import iots_parser
from parsers.tsparsers import sts_parser


def ts_parser(file_name: str) -> LTS:
    """
    根据不同迁移系统文件类型，转化为对应的迁移系统对象
    """
    ts_type = parse_ts_type(file_name)

    if ts_type not in TS_TYPE:
        print("\033[31m[!] Error: type is not exist!\033[0m")
        exit(0)

    if ts_type == "LTS":
        return sts_parser(file_name)
    elif ts_type == "IOTS":
        return iots_parser(file_name)
    elif ts_type == "STS":
        return sts_parser(file_name)

    return

