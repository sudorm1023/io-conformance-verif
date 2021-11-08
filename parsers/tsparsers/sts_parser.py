#!/usr/bin/env python3

"""
该模块中的函数用来将，以如下文本文件表示的迁移系统：

module-sts euler_rate_to_ang_vel_AC_AttitudeControl:
initial : s0
output sinf : {s0 -> s1}
output cosf : {s1 -> s2}
output cosf : {s2 -> s3}
output sinf : {s3 -> s4}
endmodule-sts

转换为标记迁移系统STS实例
"""

from ts import STS


def sts_parser(file_name: str) -> STS:
    """
    根据*.ts文件中描述的输入输出迁移系统，生成对应的STS对象
    :param file_name: .ts结尾的文件
    :return: STS对象
    """

    """
    还需要补充代码块
    """
    return
