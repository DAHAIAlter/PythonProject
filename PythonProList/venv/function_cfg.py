# -*- coding:utf-8 -*-
# 该脚本注重于对应.cfg文件的修改以及管理

import ConfigParser
import random
import string
import os


# 重写ConfigParser,使其保存时能保证大小写
class MyConfigParser(ConfigParser.ConfigParser):
    def __init__(self, defaults=None):
        ConfigParser.ConfigParser.__init__(self, defaults=defaults)

    def optionxform(self, optionstr):
        return optionstr


fname_list = MyConfigParser()
fname_list.read(r"D:\PycharmProjects\Hellow\venv\FunctionName.cfg")

use_list = MyConfigParser()
use_list.read(r"D:\PycharmProjects\Hellow\venv\UseCfg.cfg")


def clean_all():
    with open(r"D:\PycharmProjects\Hellow\venv\FunctionName.cfg","w+") as fun_fil:
        fun_fil.truncate()
        fun_fil.close()
    with open(r"D:\PycharmProjects\Hellow\venv\UseCfg.cfg","w+") as use_fil:
        use_fil.truncate()
        use_fil.close()



# 传入数字,返回对应数量的随机字母
def get_random_text(num):
    if num <= 0: return
    ran_list = [random.choice(string.ascii_letters) for i in range(num)]
    ran_txt = ''.join(ran_list)
    return ran_txt


# 该文件对应的是对应类名捕获对应的函数名,其中path为对应类的路径
def add_Fname_CFG(section, option):
    if not fname_list.has_section(section):
        fname_list.add_section(section)
    if not fname_list.has_option(section, option):
        fname_list.set(section, option, get_random_text(5))
    fname_list.write(open(r"D:\PycharmProjects\Hellow\venv\FunctionName.cfg", 'w'))


# 更新对应脚本的路径
def init_cs_path(section, path):
    if fname_list.has_section(section):
        if fname_list.has_option(section, "path"):
            if os.path.exists(fname_list.get(section, "path")):
                return
            else:
                if os.path.exists(path):
                    fname_list.set(section, "path", path)
        else:
            if os.path.exists(path):
                fname_list.set(section, "path", path)
    else:
        if os.path.exists(path):
            fname_list.add_section(section)
            fname_list.set(section, "path", path)
    fname_list.write(open(r"D:\PycharmProjects\Hellow\venv\FunctionName.cfg", 'w+'))


# 该文件是对各脚本中实例调用的路径
def add_Use_CFG(section, option, value):
    if not use_list.has_section(section):
        use_list.add_section(section)
    if not use_list.has_option(section, option):
        use_list.set(section, option, value)
    use_list.write(open(r"D:\PycharmProjects\Hellow\venv\UseCfg.cfg", 'w'))


def get_all_invok():
    invok_list = []
    invok_sections = use_list.sections()
    for curr_sec in invok_sections:
        for curr_op in use_list.options(curr_sec):
            invok_list.append((curr_sec, curr_op))
    return invok_list

def get_allinvok_section():
    return use_list.sections()


def get_option_byinvokCfg(section, option):
    if use_list.has_section(section):
        return use_list.get(section, option)

def get_invokList_byinvokCfg(section):
    if  use_list.has_section(section):
        return use_list.items(section)



def get_option_bysourceCfg(section, option):
    if fname_list.has_section(section):
        if fname_list.has_option(section, option):
            return fname_list.get(section, option)
