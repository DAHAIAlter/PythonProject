# -*- coding:utf8 -*-
import re
import os
import sys
import random
import string
import datetime

print sys.argv[0]
# curr_path = os.path.split(sys.argv[0])
curr_path = r"E:\Demo\out_oc"

CLASS_COUNT = 100
FUN_COUNT = 100

create_path = curr_path + "\\" + "out_" + datetime.datetime.strftime(datetime.datetime.now(), "%m_%d_%H%M%S")
create_path_file = create_path + "\\" + "file"
os.makedirs(create_path)
os.makedirs(create_path_file)


def get_random_num():
    return ''.join(random.sample(["1", "2", "3", "4", "5", "6", "7", "8", "9"], random.choice(range(6, 8))))


def get_random_text():
    return random.choice(string.ascii_letters) + "".join(
        random.sample(string.ascii_letters + string.digits, random.choice(range(7, 10))))


def get_fun_type():
    return random.choice(["(BOOL)", "(int)", "(NSString *)", "(UIView *)"])


def get_return_value():
    return random.choice(["(BOOL)", "(int)", "(NSString *)", "(UIView *)"])


def get_fun_item():
    fun_l = random.choice(range(1, 6))
    item = ""
    for k in range(fun_l):
        item = item + "%s:%s%s" % (get_random_text(), get_fun_type(),
                                   get_random_text() + ("" if k == fun_l - 1 else " ")
                                   )
    return item


fun_dic = {}


def get_fun_list(f_count):
    fun_list = ""
    for j in range(f_count):
        fun_list = fun_list + "-%s%s;%s" % (get_return_value(), get_fun_item(), "" if j == f_count - 1 else "\n")
    return fun_list


def do_create_h(s_name, f_count):
    f_script = open(create_path_file + "\\" + s_name + ".h", "r+")
    h_text = "#import <Foundation/Foundation.h>\n" \
             "#import <UIKit/UIKit.h>\n" \
             "@interface %s : UIViewController\n\n" \
             "%s\n" \
             "+(%s *)sharedHelper;\n" \
             "@end" % (s_name, get_fun_list(f_count), s_name)
    f_script.write(h_text)
    f_script.close()


invoke_dis = {}


#
#
def get_invoke_item(invoke_script):
    item = random.choice(invoke_dis[invoke_script])
    r_item = ""
    sub_fun = re.findall("([0-9a-zA-Z]+):(\(.+?\))", item)
    for sub_item in sub_fun:
        r_item = r_item + sub_item[0] + ":" + (
            get_random_num() if sub_item[1] == "(int)" else "true" if sub_item[1] == "(BOOL)"
            else "@\"%s\"" % get_random_text() if sub_item[1] == "(NSString *)"
            else "[UIView alloc]" if sub_item[1] == "(UIView *)"
            else ""
        ) + ("" if sub_item == sub_fun[len(sub_fun) - 1] else " ")
    return r_item


def create_fun(s_name, fun_tit_list, invoke_script):
    fun_list = []
    fun_block = ""
    for item in fun_tit_list:
        fun_text = item + "\n"
        # 开始生成函数
        for f_name in re.findall("([^) ]+)?:\(", item):
            fun_text = fun_text + "\tNSLog(@\"%s\");\n" % f_name
        random_num = random.choice([0, 1])
        if random_num == 0 and not invoke_script == "":
            num_1 = get_random_num()
            num_2 = get_random_num()
            fun_text = fun_text + "\t[[%s sharedHelper]%s];\n" \
                                  "\tint rand_num = arc4random() %s;\n" \
                                  "\tif(rand_num>%s){\n" \
                                  "\t\t return %s;\n" \
                                  "\t}else{\n" \
                                  "\t\t return %s;" \
                                  "\n\t}\n" \
                                  "}\n" % (invoke_script, get_invoke_item(invoke_script), r"% " + num_1 + " + "
                                           + num_2, num_1, num_2, num_1)
        else:
            fun_list.append(item)
            num_1 = get_random_num()
            num_2 = get_random_num()
            fun_text = fun_text + "\tint rand_num = arc4random() %s;\n" \
                                  "\tif(rand_num>%s){\n" \
                                  "\t\t return %s;\n" \
                                  "\t}else{\n" \
                                  "\t\t return %s;\n" \
                                  "\t}\n" \
                                  "}\n" % (r"% " + num_1 + " + " + num_2, num_1, num_2, num_1)
        fun_block = fun_block + fun_text
    if len(fun_list) > 0:
        invoke_dis[s_name] = fun_list
    return fun_block


def do_create_m(s_name):
    m_file = open(create_path_file + "\\" + s_name + ".m", "r+")
    h_file = open(create_path_file + "\\" + s_name + ".h", "r+")
    f_list = []
    for item in h_file.readlines():
        if "-" in item:
            f_list.append(item.replace(";", "{"))
    invoke_n = "" if len(invoke_dis) <= 1 else random.choice(invoke_dis.keys())
    m_file.write("#import \"%s.h\"\n"
                 "%s"
                 "@implementation %s\n"
                 "\n\n"
                 "static %s* s_helper;\n"
                 "+(%s *)sharedHelper{\n"
                 "\tif (s_helper == nil) {\n"
                 "\t\ts_helper = [[self alloc] init];\n"
                 "\t}\t\t\n"
                 "\t return s_helper;\n"
                 "}\n%s"
                 "\n@end" % (s_name, "" if invoke_n == "" else "#import \"%s.h\"\n" % invoke_n, s_name, s_name, s_name,
                             create_fun(s_name, f_list, invoke_n)))
    m_file.close()


def create_script(s_name, f_count):
    with open("%s\%s" % (create_path_file, s_name + ".h"), 'w+') as script_h:
        script_h.close()
    with open("%s\\%s" % (create_path_file, s_name + ".m"), 'w+') as script_m:
        script_m.close()
    do_create_h(s_name, f_count)
    do_create_m(s_name)


for i in range(100):
    create_script(get_random_text(), 100)

# 下为构建引用文件
with open(create_path + "\\" + "mix.h", 'w+') as import_f:
    import_f.close()
with open(create_path + "\\" + "invoke.txt", 'w+') as invoke_f:
    invoke_f.close()

import_file = open(create_path + "\\" + "mix.h", 'r+')
invoke_list = open(create_path + "\\" + "invoke.txt", 'r+')

function_list = []
h_list = []

for file_name, dirs, files in os.walk(create_path_file):
    for file_item in files:
        if os.path.splitext(file_item)[1] == ".h":
            h_list.append(file_item)

print len(h_list)


def get_list():
    invoke_list_t = []
    for file_h in h_list:
        import_file.writelines("#import \"%s\"\n" % file_h)
        h_file = open(file_name + "\\" + file_h)
        fun_list = re.findall(r"\n-\((?:BOOL|int|void|NSString)[ *]*?\)([^\n]+)?;", h_file.read())
        f_count = random.choice(range(1, 6))
        for j in range(f_count):
            name_item = random.choice(fun_list)
            if ":" not in name_item:
                invoke_list_t.append("[[%s] %s];\n" % (os.path.splitext(file_h)[0] + " sharedHelper", name_item))
            if ":" in name_item:
                sub_list = re.findall(r"(\S+):\(([\S]+)(?: \*|)\)", name_item)
                invoke_lin = "[%s]" % (os.path.splitext(file_h)[0] + " sharedHelper")
                for sub_item in sub_list:
                    invoke_lin = "%s %s:%s" % (invoke_lin, sub_item[0],
                                               "true" if sub_item[1] == "BOOL"
                                               else "@\"%s\"" % get_random_num() if sub_item[1] == "id"
                                               else get_random_num() if sub_item[1] == "int"
                                               else "@\"%s\"" % get_random_text() if sub_item[1] == "NSString"
                                               else "[UIView alloc]" if "UIView"
                                               else "")
                invoke_list_t.append("\t\t\t[" + invoke_lin + "];\n")
    import_file.close()

    inv_item_list = random.sample(invoke_list_t, 50)
    o_lin = ""
    out_txt = ""
    block_count = 5
    for l in range(block_count):
        for fun_item in inv_item_list:
            o_lin = o_lin + fun_item
        out_txt = out_txt + "\t\ttry{\n" \
                            "%s\t\t}\n" \
                            "\t\tcatch (NSException *exception) {\n" \
                            "\t\t\tNSLog(@\"MixScriptError\");\n" \
                            "\t\t}\n\n" % o_lin + "\n"
    invoke_list.write(out_txt)
    invoke_list.close()


get_list()
