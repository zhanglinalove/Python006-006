from datetime import *
import time
import logging
from pathlib import Path


# （此作业需提交至 GitHub）
# 编写一个函数, 当函数被调用时，将调用的时间记录在日志中,
# 日志文件的保存位置建议为：/var/log/python- 当前日期 /xxxx.log


# 生成文件目录及文件，并将其路径返回
def createDirPathReturnName(currDay):
    filePath = "/var/log/python-{0}/{1}.log".format(currDay, currDay)
    print(filePath)
    path = Path(filePath)

    if not path.exists():
        path.parent.mkdir(exist_ok=True)
        path.touch(exist_ok=True)

    return filePath


# 得到当前的日期
def getCurrentTime():
    return time.strftime("%Y%m%d")


# 调用Logging模块，输出调用的时间，及其余的有用信息
def writeLog(filename):
    logging.basicConfig(filename=filename,
                        datefmt="%Y-%m-%d %H:%M:%S",
                        format='%(asctime)s %(name)-8s %(levelname)-8s [line: %(lineno)d] %(message)s')
    logging.debug("debug message!")
    logging.info("info message!")
    logging.error("error message!")
    logging.critical("critical message!")
    logging.warning("warning message!")


# main 进行程序的调用
if __name__ == "__main__":
    writeLog(createDirPathReturnName(getCurrentTime()))
