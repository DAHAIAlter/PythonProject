# -*- coding:utf-8 -*-

import os,re
import ConfigParser

# 加载配置文件,判断文件中路径是否合理
def load_File():
    pro_info = ConfigParser.ConfigParser();
    pro_info.read(r"D:\PycharmProjects\Hellow\venv\MixFile\BackCfg\useless_file_cfg.cfg")
    print pro_info
    if not pro_info.has_section("cfg"):
        pro_info.add_section("cfg")

    pro_info.set('cfg', 'Path_MixFile', r'D:\PycharmProjects\Hellow\venv\MixFile')


    pro_info.write(open(r"D:\PycharmProjects\Hellow\venv\MixFile\BackCfg\useless_file_cfg.cfg","w"))

    # PRO_PATH = pro_info.get('cfg', "FilePath")

load_File()