# LTS进行一致性检测

## 1. 程序目录描述

* `core/`: 对LTS的三个组件状态、迁移系统、动作进行分别编程描述
    * `action.py`: 描述动作
    * `state.py`: 描述状态
    * `transition.py`: 描述迁移关系
  
* `ts/`: 该目录下保存不同的迁移系统
    * `lts.py`: 该文件描述标记迁移系统
    * `iots.py`: 该文件描述输入输出迁移系统
    * `sts.py`: 该文件描述安全迁移系统
    * `testcase.py`: 增加一致性种的测试用例系统
  
* `conf/`: 该目录保存一致性测试的步骤
  * `testcase_generate.py`: 测试用例生成
  * `testcase_run.py`: 测试用例执行
  * `conf_relation.py`: 判断实现是否满足一致性关系
  
* `confgraph`: 该目录用来讲迁移系统表示为图
  * `ts_graph.py`: 各种迁移系统的图表示的图的抽象定义
  * `ts_to_tsgraph.py`: 将各种迁移系统转换为TsGraph对象
  
* `constants`: 该目录用来保存各种常量
  * `constant.py`: 保存常量的文件
  
* `parsers`: 该目录下的文件用来存放解析的文件
  * `tsparsers`: 该目录下存放对应不同文件迁移系统的解析文件
  * `ts_parser.py`: 通用的解析文件