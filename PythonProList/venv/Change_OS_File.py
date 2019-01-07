#-*- coding:utf-8 -*-
import ConfigParser
import os
import re
import random
import string
import shutil


Pro_cfg = ConfigParser.ConfigParser()
Pro_cfg.read(r"D:\PycharmProjects\Hellow\venv\mix_cfg.cfg")

def loadCfg(name):
    return Pro_cfg.get('cfg',name)


PRO_Path = loadCfg("PRO_Path")
PRO_XUPor = PRO_Path + "\Assets\Editor\XUPorter\Mods"
######################################
# 初始化无用信息的文件树，确保PRO_Path的路径配置正确，以下函数将在工程路径下初始化文件树
def init_Useless_ft():
    if not os.path.exists(PRO_XUPor+"\MixFile"):
        os.mkdir(PRO_XUPor+"\MixFile")
        os.mkdir(PRO_XUPor+"\MixFile\MixCobe")
        os.mkdir(PRO_XUPor+"\MixFile\BackCfg")
        os.mkdir(PRO_XUPor+"\MixFile\Useless")
    os.chdir(PRO_XUPor+"\MixFile")
    if not os.path.exists("MixCobe"):
        os.mkdir("MixCobe")
    if not os.path.exists("BackCfg"):
        os.mkdir("BackCfg")
    if not os.path.exists("Useless"):
        os.mkdir("Useless")
        os.chdir(PRO_XUPor)
    return True

init_Useless_ft()
######################################
#1.生成随机数，生成包含字母和数字的文本并写入到文件中
def get_random_text(num):
    if num<=0:
        return
    ran_list =[random.choice(string.ascii_letters+string.digits) for i in range(num)]
    ran_txt = ''.join(ran_list)
   # print ran_txt
    return ran_txt


def create_ramdon_file():
    if os.getcwd() != PRO_XUPor + "\MixFile\Useless":
        os.chdir(PRO_XUPor + "\MixFile\Useless")
    filename = get_random_text(5)
    useless = open(filename, 'w+')
    for i in range(1, 20):
        useless.write(get_random_text(random.choice(range(10000,200000))))
    useless.close()

create_ramdon_file()

useless_file_size = 0
def get_useLess_filesize():
    if not os.path.exists(PRO_XUPor+"\MixFile\Useless"):
        print "文件目录不存在"
        return
    global useless_file_size
    os.chdir(PRO_XUPor+"\MixFile");
    file_list = os.listdir("Useless")
    for item in file_list:
         file_size = os.path.getsize("Useless\\" + item) / 1048576
         useless_file_size = useless_file_size + file_size
    print "当前无用文件的总大小为%sM"%useless_file_size
get_useLess_filesize()

######################################
# 资源混淆，对部分资源进行混淆操作，一般为在该文件后面插入随机数量的随机文本




######################################
# 对代码进行修改，修改变量名和函数名以及生成无用的代码文件


######################################
# 恢复函数，还原所有该脚本执行的修改
def remove_useless_file():
    #  os.remove(PRO_PATH+"\MixFile\Useless\8xmX4")
    if not os.path.exists(PRO_XUPor + r"\MixFile\Useless"):
        return
    shutil.rmtree(PRO_PATH + r"\MixFile\Useless")