#!/usr/bin/python3
#-*- coding: UTF-8 -*- 
#@Author:

import json
from mailrest.logs import *

CONFNAME = r"/app/sendermail/conf/cfg.json"

#读取配置文件，并以字典形式返回
def read_cof():
    log = LogtoLog().getlog()
    try:
        ofs = open(CONFNAME, encoding='utf-8')
    except IOError as err:
        log.error("文件不存在，或者权限不足!!! " + str(err))
    cnfdata = json.load(ofs)
    return cnfdata