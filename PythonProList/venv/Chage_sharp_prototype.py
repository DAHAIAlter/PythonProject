# -*- coding:utf-8 -*-
# 该脚本注重于对工程中的CS脚本进行修改


import os
import re
import sys

sys.path.append("function_cfg.py")
import function_cfg

# function_cfg.clean_all()
RE_FNAME = r"(void|int|bool)([\s\S]+)?\("
pro_path = r"E:\Work\game\Assets\Script"
test_pro_path = r"C:\Users\Administrator\Desktop\oc\Assets"
log_path = r"D:\PycharmProjects\Hellow\venv\Find_All_Log.txt"

# LogInit Begin

# if not os.path.exists(log_path):
#     print ""
log_file = open(log_path, "a+")


def log(txt):
    log_file.write(txt + "\n")


# LogInit Finish
# Find C# Script in gameProject Begin
cs_list = []
path = test_pro_path
for pro_path, pro_dir, pro_list in os.walk(path):
    for item in pro_list:
        if os.path.splitext(item)[1] == ".cs":
            cs_list.append([pro_path, item])
log("查找到的CS脚本有%s个" % len(cs_list))
# Find C# Script Finish


# for item in cs_list:
#     print item
count = 0


def add_fun2log(fun_list):
    if not len(fun_list) == 4:
        return
    a, b, c, d = "", "", "", "";
    if fun_list[0] == "": a = "prive"
    b, c, d = fun_list[1], fun_list[2], fun_list[3]
    log(a + " " + b + " " + c + " " + d)


# 记录函数的所有应用

def change_fname(tager, list):
    cfile = open(tager[0] + "//" + tager[1])
    # print tager[1]
    lins = cfile.readlines()
    cfile.close()


class_name_list = []
SYSTEM_RESERVE = ["Color", "Vector3","Dictionary"]
SYSTEM_RESERVE_FNAME = ["start", "update", "awake"]


def chagne_fname():
    for item in cs_list:
        if not os.path.exists(item[0] + "\\" + item[1]):
            print "error"
            return
        # 读取脚本
        class_path = item[0] + "\\" + item[1]
        mix_script = open(class_path)
        mix_txt = mix_script.read()
        # 获取类名,默认只获取第一次匹配到的类名 也就是find_name[0][0]
        find_cname = re.findall(r"\n\s*(?:public|)\s*class\s*([^:\{\n\s]+)\s?\:*([^\{\n]+)?(\n|\{)", mix_txt)
        if len(find_cname) == 0: continue
        class_name = find_cname[0][0]
        # 注册全局的类名列表,方便修改时进行判断
        class_name_list.append(class_name)
        # 获取所有的函数名,第一为访问标识符,第二位为函数名,第三位为参数列表
        find_list = re.findall(r"(?:\n    |\n\t)(private|public|)\s*(int|void|bool)\s*([^\(\n\:\= ]+)\s*(\(.*\)).*?\n",
                               mix_txt)
        # 将获取到的所有函数名添加到FunctionName.cfg中,详细请看对应脚本
        for fname in find_list:
            function_cfg.init_cs_path(class_name, class_path)
            function_cfg.add_Fname_CFG(class_name, fname[2])

        # 获取该脚本中所有创建的实例
        useList = re.findall(r"([^\s]+) *= *new ([^\(]+)", mix_txt)
        # 过滤系统类
        ctrl_useList = []
        for i in useList:
            if not i[1] in SYSTEM_RESERVE:
                ctrl_useList.append(i)
        # 记录该对象在该脚本的函数调用情况,ctrl_useList不为空时,则表示已经捕获到非系统示例
        if not len(ctrl_useList) == 0:
            for use_obj in ctrl_useList:
                use_fun_list = re.findall("%s\.([^\(\n]+)?\(" % use_obj[0], mix_txt)

                for use_fun_list_item in use_fun_list:
                    function_cfg.add_Use_CFG(class_name,use_obj[0] + "\\" + use_fun_list_item,use_obj[1])


def cs_replace(source_path, invoke_path, obj, fname, fname_new):
    if not os.path.exists(source_path) and os.path.exists(invoke_path):
        return
    # 获取对应脚本的行
    with open(source_path, 'r') as source_file:
        source_lines = source_file.readlines()
    with open(invoke_path, 'r') as invoke_file:
        invoke_lines = invoke_file.readlines()
    # 初始化对应的修改标识
    source_tag = fname
    invoke_tag = "%s.%s" % (obj, fname)
    # 源类的修改
    with open(source_path, 'w') as source_file:
        for source_line in source_lines:
            if source_tag in source_line:
                source_line = source_line.replace(" " +source_tag, " " + fname_new)
            source_file.write(source_line)
    # 耦合类的修改
    with open(invoke_path, "w") as invoke_file:
        for invoke_line in invoke_lines:
            if invoke_tag in invoke_line:
                invoke_line = invoke_line.replace(invoke_tag, "%s.%s" % (obj, fname_new))
            invoke_file.write(invoke_line)


# 获取并解析需要混淆的数据，该类的查询重点为目标类，也就是在耦合类中寻找原类 然后进行同步修改
def mix_script():
    # 获取到需要修改的类和相应的与该类耦合的类
    invok_list = function_cfg.get_allinvok_section()
    if not len(invok_list) == 0:
        for invok_list_item in invok_list:
            invoke_class = invok_list_item
            # 获取相互耦合的类中的实际例名与调用的函数
            invoke_info_list = function_cfg.get_invokList_byinvokCfg(invoke_class)
            if not len(invoke_info_list) == 0:
                for invoke_info_item in invoke_info_list:
                    source_class = invoke_info_item[1]
                    fname = invoke_info_item[0].split("\\")[1]
                    obj = invoke_info_item[0].split("\\")[0]
                    # 每个类都有对应的路径标识
                    source_path = function_cfg.get_option_bysourceCfg(source_class, "path")
                    invoke_path = function_cfg.get_option_bysourceCfg(invoke_class, "path")
                    # 在记录相应类名的时候就已经生产了随机的函数名
                    source_new_fn = function_cfg.get_option_bysourceCfg(source_class, fname)
                    # 将对应信息传递给实现函数
                    cs_replace(source_path,invoke_path, obj, fname, source_new_fn)


chagne_fname()
mix_script()
