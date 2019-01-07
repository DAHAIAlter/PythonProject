# -*- coding:utf-8 -*-

import os
import re
import string
import random
import sys

sys.path.append("pro_Cfg.py")
import pro_Cfg

# if len(sys.argv) >=0:
#     print len(sys.argv)

RANDOM_POOL = string.ascii_letters


def get_random_letter(num):
    if not num > 0:
        print ("获取随机数不合法:%s" % num)
        return
    random_list = [random.choice(RANDOM_POOL) for i in range(num)]
    random_txt = "".join(random_list)
    return random_txt


pro_m_list = []
pro_h_list = []
pro_png_list = []
# pro_path = pro_Cfg.get_pro_path().decode('utf8')
pro_path = r"E:\Work\game\Assets\Editor\XUPorter\Mods\EIGameWrapper";
pro_json_list = []

images_xcassets = ""


def get_all_file(path):
    print os.path.exists(path)
    global json_Con
    for fpath, fdirs, flist in os.walk(path):
        if os.path.split(fpath)[1] == "Images.xcassets":
            global images_xcassets
            images_xcassets = fpath

        for item in flist:
            if item == "Contents.json":
                pro_json_list.append((fpath, item))
            if os.path.splitext(item)[1] == ".h":
                pro_h_list.append(fpath + "\\" + item)
            if os.path.splitext(item)[1] == ".m":
                pro_m_list.append(fpath + "\\" + item)
            if os.path.splitext(item)[1] == ".png":
                pro_h_list.append(fpath + "\\" + item)


get_all_file(pro_path)


def change_png_name():
    if not os.path.exists(images_xcassets):
        print "路径%s异常，png文件名字修改失败"
        return
    os.chdir(images_xcassets)
    appIcon_list = []
    launchImage_list = []
    for arg, dirname, names in os.walk(images_xcassets):
        print arg
        if os.path.split(arg)[1] == "AppIcon.appiconset":
            for item_name in names:
                if item_name == "Contents.json" or os.path.splitext(item_name)[1] == ".png":
                    appIcon_list.append(item_name)
        if os.path.split(arg)[1] == "LaunchImage.launchimage":
            for item_name in names:
                if item_name == "Contents.json" or os.path.splitext(item_name)[1] == ".png":
                    launchImage_list.append(item_name)
    print launchImage_list
    change_name(appIcon_list, images_xcassets + "\\" + "AppIcon.appiconset")
    # change_name(launchImage_list,images_xcassets+"\\"+"LaunchImage.launchimage")


re_filename = r"\"filename\" *\: *\"%s\""

# 替换的随机字符要长于本身自带的字符，不然会出现后面的字符替换不完整导致后排多出文本信息
def change_name(list, path):
    if "Contents.json" in list:
        json_fil = open(path + "\\" + "Contents.json", 'r+')
        json_txt = json_fil.read()
        for item_name in list:
            if os.path.splitext(item_name)[1] == ".png":
                if os.path.exists(path + "\\" + item_name):
                    old_name = item_name
                    new_name = get_random_letter(17) + ".png"
                    json_txt = replace_filename(re_filename % old_name, json_txt, old_name, new_name)
                    os.rename(path+"\\"+item_name,path+"\\"+new_name)
                    print json_fil.tell()
                    json_fil.seek(0,0)
                    json_fil.write(json_txt)
        json_fil.close()
        # print json_txt


def replace_filename(re_png, txt, oldtxt, newtxt):
    def _change(matched):
        print matched.group(0)
        return str.replace(matched.group(0), oldtxt, newtxt)
    return re.sub(re_png, _change, txt)


change_png_name();

def replace_classname():
    print
