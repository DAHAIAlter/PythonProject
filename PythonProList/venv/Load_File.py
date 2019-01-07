# -*- coding:utf-8 -*-
# 该脚本为测试脚本 重点是加载对应文件夹的所有的jpg图片 png图片 和音频资源等

import os
import random
import string
import hashlib
from PIL import Image
from scipy.io import wavfile



PRO_PATH = "E:\Work\game\Assets"
jpg_list = []
png_list = []
wav_list = []


def load_png():
    print os.listdir(PRO_PATH)
    for dirName, fileList, fileName in os.walk(PRO_PATH, topdown=False):
        for item in fileName:
            if os.path.splitext(item)[1] == ".jpg" or os.path.splitext(item)[1] == ".JPG":
                jpg_list.append(dirName + "\\" + item)
            if os.path.splitext(item)[1] == ".PNG" or os.path.splitext(item)[1] == ".png":
                png_list.append(dirName + "\\" + item)
            if os.path.splitext(item)[1] == ".wav" or os.path.splitext(item)[1] == ".WAV":
                wav_list.append(dirName + "\\" + item)


    print "工程中一共找到jpg文件%s个"% len(jpg_list)
    print "工程中一共找到png文件%s个"% len(png_list)
    print "工程中一共找到wav文件%s个"% len(wav_list)


load_png()

# 下位png文件的混淆实现

png_count = 0


def mix_png(path):
    if not os.path.exists(path):
        print "%s文件不存在" % path
        return
    file_ram = open(path, 'a+')
    file_ram.write(get_random_txt(random.choice(range(4,8))))
    # print "文件%s经过混淆处理" % path
    global png_count
    png_count = png_count + 1
    md5 = hashlib.md5()
    md5.update(file_ram.read())
    hash = md5.hexdigest()
    # print hash
    file_ram.close()


def get_random_txt(num):
    if num <= 0: return
    txt_list = [random.choice(string.ascii_letters) for i in range(num)];
    random_txt = ''.join(txt_list);
    return random_txt


jpg_count = 0


def mix_jpg(path):
    if not os.path.exists(path):
        print "%s文件路径有误" % path
        return
    img_path = path

    try:
        img = Image.open(img_path)
        img.save(img_path, quality=random.choice(range(70, 99)))

    except BaseException:
        return

    global jpg_count
    jpg_count = jpg_count + 1


# print "文件%s经过混淆处理" % path


for item in png_list:
    mix_png(item)
for item in jpg_list:
    mix_jpg(item)
print "共有%s个jpg文件经过处理" % jpg_count
print "共有%s个png文件经过处理" % png_count
