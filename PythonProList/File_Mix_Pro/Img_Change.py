# -*- coding:utf-8 -*-
# oc混淆脚本生成器的原型
import os
import sys
import string
import random
import hashlib

from PIL import Image
"""
img_list = []
png_list = []
wav_list = []
for f_name, f_dir, f_list in os.walk("E:\Work\game_pure\Assets"):
    for file_item in f_list:
        if os.path.splitext(file_item)[1] == ".jpg" or os.path.splitext(file_item)[1] == ".JPG":
            img_list.append(f_name + "\\" + file_item)
        if os.path.splitext(file_item)[1] == ".png" or os.path.splitext(file_item)[1] == ".PNG":
            png_list.append(f_name + "\\" + file_item)
        if os.path.splitext(file_item)[1] == ".wav":
            wav_list.append(f_name + "\\" + file_item)


def mix_jpg(path):
    if not os.path.exists(path):
        print "%s文件路径有误" % path
        return
    img_path = path
    img = Image.open(img_path).save(img_path, quality=random.choice(range(70, 99)))


for i in range(300):
    f_jpg = random.choice(img_list)
    img_list.append(f_jpg)
    mix_jpg(f_jpg)

print str.split(".\key\\aa\\bbs", "\\")
path = ""
for item in str.split(".\key\\aa\\bbs", "\\"):
    if item == '.':
        continue
    path = path + "\\" + item

print os.path.abspath(".\key\\aa\\bbs")


def get_random_txt(num):
    if num <= 0:
        return
    txt_list = [random.choice(string.ascii_letters) for i in range(num)];
    random_txt = ''.join(txt_list)
    return random_txt


png_count = 0


def mix_png(path):
    if not os.path.exists(path):
        print "%s文件不存在" % path
        return
    file_ram = open(path, 'a+')
    file_ram.write(get_random_txt(random.choice(range(4, 8))))
    # print "文件%s经过混淆处理" % path
    global png_count
    png_count = png_count + 1
    md5 = hashlib.md5()
    md5.update(file_ram.read())
    # hash = md5.hexdigest()
    # print hash
    file_ram.close()

#
# for i in range(100):
#     mix_png(random.choice(png_list))
"""