# -*- coding:utf8 -*-
import os
import re
from PIL import Image
import shutil

# 全局搜索脚本

path = unicode(r"E:\Work\platform_config\ios")

for f_path, f_dir, f_list in os.walk(path):
    for item in f_list:
        get_file = open(f_path + "\\" + item)
        if r"g1004tb.nwny.pinjintech.com" in get_file.read():
            print item
