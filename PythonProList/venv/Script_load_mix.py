# -*- coding:utf-8 -*-
# PROTOTYPE
# 识别文件树
# path = r"E:\Work\game\Assets\Plugins\Android"
# dirs = os.listdir(path)
# #print dirs
#
# for dirName, subdirList, fileList in os.walk(path,topdown=False):
#  #print ("FileName %s"% dirName)
#  for fname in fileList:
#      #print('\t%s' % fname)
#      #print os.path.splitext(fname)
#      if os.path.splitext(fname)[1]==".xml":
#          print  fname

# path = r"D:\PycharmProjects\Hellow\EightWrapper.mm"
# oc_file = open(path)
# #print oc_file.read()
# oc_c_code_block=re.findall("\s+(?=void|bool)[^}]+?\}",oc_file.read())
# #print oc_c_code_block[0]
# for line in oc_c_code_block:
#     oc_c_code_block_fname = re.findall("\s+(?=void|bool)([^{]+)?\{",line)
#     oc_c_code_block_fcode = re.findall("[\s,\S]+?\{([^}]+)?\}",line)
#     # print "函数名%s" % oc_c_code_block_fname
#     # print "函数体%s," % oc_c_code_block_fcode
#
# for item in oc_c_code_block_fcode:
#     print item
import re
import random
import string
import os
import ConfigParser
import datetime
import sys


path = r"D:\PycharmProjects\Hellow\XMl_text"
xmlfile = open(path).read()
useless_file_size = 0


pro_info = ConfigParser.ConfigParser();
pro_info.read(r"D:\PycharmProjects\Hellow\pow_cfg.cfg")
re_lib = ConfigParser.ConfigParser()
re_lib.read(r"D:\PycharmProjects\Hellow\venv\RegularExpressionLib.cfg")

RE_XML_Per = re_lib.get('RE',"XML_Permission")
RE_XML_Name = re_lib.get('RE',"XML_Name")
RE_XML_OC = re_lib.get('CODE',"CODE_OC")
CODE_Var = re_lib.get('CODE',"CODE_Var")

OC_Path = "D:\PycharmProjects\Hellow\OC_mix.txt";
OC_File = open(OC_Path)
OC_List = re.findall(RE_XML_OC,OC_File.read())


# for item in OC_List:
#     print item[1]



# 加载权限标签
def getpermission():
    permission_list = re.findall(RE_XML_Per,xmlfile)
    for item in permission_list:
        # print item
        getPermissionByName(item)


# 通过名字加载权限
def getPermissionByName(name):
    if pro_info.has_option("Permission",name):
        print pro_info.get("Permission",name)
    else:
        print name


# getpermission()
# 加载XML文件
def getNameByTag(tag):
    activity_list = re.findall(RE_XML_Name% tag, xmlfile)
    print len(activity_list)
    for item in activity_list:
        print item
    return activity_list


# 根据传值获取随机数
def get_random_text(num):
    if num<=0:
        return
    ran_list =[random.choice(string.ascii_letters+string.digits) for i in range(num)]
    ran_txt = ''.join(ran_list)
    print ran_txt
    return ran_txt


# 生成C函数
def load_OC_Code():
    fun_name =''.join(random.sample(string.ascii_letters,1))+get_random_text(random.randint(5,8))
    fun_main = "print \"%s\""%get_random_text(10)
    a = get_random_text(10)
    print "void %s(){ \n" "\t try{ \n \t\t print(\"%s\");} \n}"% (fun_name,get_random_text(100))
    print fun_main
    return


# 更改文件md5
def chage_file(path):
    if(not os.path.isfile(path)):
        return
    print path+"  Is File"
    file_ram = open(path,'a+')
    file_ram.write(get_random_fname(10))
    file_ram.close()
    print open(path).read()

# 创建垃圾文件

def init_mix_cfg():
    if not init_mix_flie():
        return
    if os.getcwd()!=PRO_PATH+"\MixFile\BackCfg":
        os.chdir(PRO_PATH+"\MixFile\BackCfg")
    useless_file_cfg = open("useless_file_cfg.cfg",'a+')
    print useless_file_cfg
    useless_file_cfg.close()

def init_mix_flie():
    if not os.path.exists(PRO_PATH+"\MixFile"):
        os.mkdir(PRO_PATH+"\MixFile")
        os.mkdir(PRO_PATH+"\MixFile\MixCobe")
        os.mkdir(PRO_PATH+"\MixFile\BackCfg")
        os.mkdir(PRO_PATH+"\MixFile\Useless")
    os.chdir(PRO_PATH+"\MixFile")
    if not os.path.exists("MixCobe"):
        os.mkdir("MixCobe")
    if not os.path.exists("BackCfg"):
        os.mkdir("BackCfg")
    if not os.path.exists("Useless"):
        os.mkdir("Useless")
        os.chdir(PRO_PATH)
    return True

# init_mix_cfg()

def cfg_add():
    os.chdir(PRO_PATH+"\MixFile")
    if not os.path.exists(PRO_PATH+"\MixFile\BackCfg\useless_file_cfg.cfg"):
        print "正在初始化混淆文件相关配置"
        init_mix_cfg()
        return
    print "add"
    configparser = ConfigParser.ConfigParser()
    configparser.read("useless_file_cfg.cfg")

# 创建无用文件
# 优先判断当前文件夹中已经创建的文件的大小
def creat_useless_file():
    if os.getcwd()!=PRO_PATH+"\MixFile\Useless":
        os.chdir(PRO_PATH+"\MixFile\Useless")
    filename =  get_random_text(5)
    useless = open(filename,'w+')
    for i in range(1,20):
        useless.write(get_random_text(1000000))
    useless.close()
    print os.path.getsize(PRO_PATH+"\MixFile\Useless")
# creat_useless_file()


def get_useLess_filesize():
    if not os.path.exists(PRO_PATH+"\MixFile\Useless"):
        return
    global useless_file_size
    os.chdir(PRO_PATH+"\MixFile");
    file_list = os.listdir("Useless")
    print file_list
    for item in file_list:
         file_size = os.path.getsize("Useless\\" + item) / 1048576
         useless_file_size = useless_file_size + file_size
    print "当前无用文件的总大小为%sM"%useless_file_size


# get_useLess_filesize()
import shutil

# 删除创建的无用文件
def remove_useless_file():
    #  os.remove(PRO_PATH+"\MixFile\Useless\8xmX4")
    if not os.path.exists(PRO_PATH + r"\MixFile\Useless"):
        return
    shutil.rmtree(PRO_PATH + r"\MixFile\Useless")

# remove_useless_file()
# cfg_add()

# init_mix_cfg()

# 用语句判断函数
# def load_script():

# "D:\PycharmProjects\Hellow\EightWrapper.h"
def load_code_h():
   file_h = open(r"D:\PycharmProjects\Hellow\EightWrapper.h")
   file_h_t = file_h.read()
   print re.findall(CODE_Var,file_h_t)


# load_code_h()

######################
# 改变图片质量实现包体改变包体差异



from PIL import Image


def mix_jpg(path):
    if not os.path.exists(path):
        print "%s文件路径有误"%path
        return
    img_path = path
    img = Image.open(img_path).save(img_path,quality=random.choice(range(70,99)))


# mix_jpg(r"C:\Users\Administrator\Desktop\mix_file\resloadbg.JPG")

lib_path =r"E:\Work\game\Assets\Localization\DyncTextures\export\SE_LANGUAGETYPE_Traditional_Chinese\texture\\"
lib_path_1 =r"E:\Work\game\Assets\Resources\GameAssets\Textures\Adventure\LevelBGTextures\\"
lib_path_2 =r"E:\Work\game\Assets\Resources\GameAssets\Textures\Icon\Elves\\"


file_list = os.listdir(lib_path);

jpg_list = []
count = 0
# for item in file_list:
#     if os.path.splitext(item)[1]==".jpg" or os.path.splitext(item)[1]==".JPG":
#         count = count+1
#         jpg_list.append(item)
#         mix_jpg(lib_path+item)
# print jpg_list
# print count

import hashlib
png_count = 0



#######################
# Img插件无法对png文件进行质量修改,只能通过在文件后添加字符的形式进行混淆
def mix_png(path):
    if not os.path.exists(path):
        print "%s文件不存在"%path
        return
    file_ram = open(path,'a+')
    file_ram.write(get_random_txt(10))
    print "文件%s经过混淆处理"%path
    md5 = hashlib.md5()
    md5.update(file_ram.read())
    hash = md5.hexdigest()
    print hash
    file_ram.close()


def get_random_txt(num):
    if num<=0: return
    txt_list = [random.choice(string.ascii_letters) for i in range(num)];
    random_txt = ''.join(txt_list);
    return random_txt


# mix_jpg(r"C:\Users\Administrator\Desktop\mix_file\img\after\avatar_bg_6.JPG")
# mix_png(r"C:\Users\Administrator\Desktop\mix_file\avatar_bg_6.PNG")




png_path = r"E:\Work\game\Assets\Resources\GameAssets\Textures\ExploreTrifle\\"
png_list = os.listdir(png_path)

# for item in png_list:
#     if os.path.splitext(item)[1] ==".png" or os.path.splitext(item)[1] ==".PNG":
#         print item
#         mix_png(png_path+item)


from scipy.io import wavfile

def reLoad_music(path):

    sampleRate,musicDate = wavfile.read(path)
    wavfile.write(r'C:\Users\Administrator\Desktop\mix_file\aaa.wav',sampleRate//2,musicDate[::2])

reLoad_music(r"C:\Users\Administrator\Desktop\mix_file\sound_bgm.wav")

















