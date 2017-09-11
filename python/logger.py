# encoding: utf-8

import logging
# see https://docs.python.org/3/library/logging.html#logging.Formatter

logging.basicConfig(level=logging.DEBUG,
        format='%(asctime)s [%(filename)s:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='myapp.log',
                    filemode='a')

#################################################################################################
#定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象#
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
formatter = logging.Formatter(fmt='%(asctime)s [%(filename)s:%(funcName)s:%(lineno)d] %(levelname)s %(message)s',
                            datefmt = '%a, %d %b %Y %H:%M:%S')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)
#################################################################################################
logger = logging.getLogger()
logger.debug('This is debug message')
logger.info('This is info message')
logger.warning('This is warning message')

