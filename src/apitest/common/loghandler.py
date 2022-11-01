# import logging

import logging
from src.apitest.common.yaml_handler import yaml_data
class LoggerHandler(logging.Logger):
    # 继承Logger类
    def __init__(self,
                 name='root',
                 level='DEBUG',
                 file=None,
                 format=None
                 ):
        # 设置收集器
        super().__init__(name)
        # 设置收集器级别
        self.setLevel(level)
        # 设置日志格式
        fmt = logging.Formatter(format)
        # 如果存在文件，就设置文件处理器，日志输出到文件
        if file:
            file_handler = logging.FileHandler(file,encoding='utf-8')
            file_handler.setLevel(level)
            file_handler.setFormatter(fmt)
            self.addHandler(file_handler)
        # 设置StreamHandler,输出日志到控制台
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(level)
        stream_handler.setFormatter(fmt)
        self.addHandler(stream_handler)
# 从yaml配置文件中读取logging相关配置
logger = LoggerHandler(name=yaml_data['logger']['name'],
                       level=yaml_data['logger']['level'],
                       file='../log/mylog.txt',
                       format=yaml_data['logger']['format'])
#
# # 定义一个日志收集器
# logger = logging.getLogger('ITester')
#
# # 设置收集器的级别，不设定的话，默认收集warning及以上级别的日志
# logger.setLevel('DEBUG')
#
# # 设置日志格式
# fmt =logging.Formatter('%(filename)s-%(lineno)d-%(asctime)s-%(levelname)s-%(message)s')
#
# # 设置日志处理器-输出到文件
# file_handler = logging.FileHandler('../log/mylog.txt')
#
# # 设置日志处理器级别
# file_handler.setLevel("DEBUG")
#
# # 处理器按指定格式输出日志
# file_handler.setFormatter(fmt)
#
# # 输出到控制台
# ch = logging.StreamHandler()
# # 设置日志处理器级别
# ch.setLevel("DEBUG")
# # 处理器按指定格式输出日志
# ch.setFormatter(fmt)
#
# # 收集器和处理器对接，指定输出渠道
# # 日志输出到文件
# logger.addHandler(file_handler)
# # 日志输出到控制台
# logger.addHandler(ch)

# 调试代码
if __name__ == '__main__':
    logger.debug('自定义的debug日志')
    logger.info('运行成功')
    logger.warning('自定义的warning日志')
    logger.error('自定义的error日志')
    logger.critical('自定义的critical日志')