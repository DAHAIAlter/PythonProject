# -*- coding=utf-8 -*-

import re
import random
import string
import ConfigParser


def load_cfg():
    return

cfg = ConfigParser.ConfigParser()
cfg.read(r"D:\PycharmProjects\Hellow\venv\cfg.ini")


# 加载ini配置文件
def get_option(key):
    if  cfg.has_option('cfg1',key):
        return cfg.get('cfg1',key)

Img_path = get_option("Img_path")

# 生成随机数string.ascii_letters包含所有字母符号 string.digits包含0-9
# print ''.join(random.sample(string.ascii_letters + string.digits,62))
def get_randomText(num):
    KEY_LEN = num
    randomTxt = ""
    keylist = [random.choice(string.ascii_letters + string.digits) for i in range(KEY_LEN)]
    # for j in range(10):
    #     keylist = [random.choice(string.ascii_letters + string.digits) for i in range(KEY_LEN)]
    #     randomTxt += ''.join(keylist)
    randomTxt += ''.join(keylist)
    return  randomTxt

#在文件末尾插入随机的随机文本
def changFile(filePath):
    fileT = open(filePath,'a')
    fileT.write(get_randomText(100000))
    fileT.close()

changFile(r"D:\PycharmProjects\Hellow\avatar_bg_1.PNG")

text = get_randomText(5)
print text
def fun_fromwork(path):
    rule = r"\(.+\)"
    file_txt = open(path)
    function_list = re.findall(rule,file_txt.read())
    for item in function_list:
        print item


