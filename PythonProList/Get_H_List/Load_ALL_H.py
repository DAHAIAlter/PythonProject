# -*- coding=utf-8 -*-
import os
import re
import sys
import random
import string
import datetime
import shutil

print sys.argv[0]

oc_path = r"E:\Out_Mix\Out\new\out_12_06_152025\file"
out_path = r"E:\Out_Mix\Out\new"

create_path = out_path + "\\" + "out_" + datetime.datetime.strftime(datetime.datetime.now(), "%m_%d_%H%M%S")
create_path_file = create_path + "\\" + "file"
os.makedirs(create_path)
os.makedirs(create_path_file)

with open(create_path + "\\" + "mix.h", 'w+') as invoke_f:
    invoke_f.close()
with open(create_path + "\\" + "mix.m", 'w+') as function_f:
    function_f.close()

import_file = open(r"E:\Out_Mix\Out\new\out_12_06_152025" + "\\" + "mix.h", 'r+')
invoke_list = open(r"E:\Out_Mix\Out\new\out_12_06_152025" + "\\" + "mix.m", 'r+')

function_list = []
h_list = []
for file_name, dirs, files in os.walk(oc_path):
    for file_item in files:
        if os.path.splitext(file_item)[1] == ".h":
            h_list.append(file_item)


def get_random_num(num):
    return ''.join([random.choice(string.digits) for i in range(num)])


def get_random_str(num):
    return ''.join([random.choice(string.letters) for i in range(num)])


invoke_list_t = []


def get_list(count):
    for i in range(count):
        file_h = random.choice(h_list)
        class_n = os.path.splitext(file_h)[0]

        shutil.copy(file_name + "\\" + class_n + ".h", create_path_file)
        shutil.copy(file_name + "\\" + class_n + ".m", create_path_file)
        h_list.remove(file_h)

        import_file.writelines("#import \"%s\"\n" % file_h)
        h_file = open(file_name + "\\" + file_h)
        fun_list = re.findall(r"\n-\((?:BOOL|int|void|NSString)[ *]*?\)([^\n]+)?\;", h_file.read())
        f_count = random.choice(range(6))
        for j in range(f_count):
            name_item = random.choice(fun_list)
            if ":" not in name_item:
                invoke_list_t.append("[[%s] %s];\n" % (os.path.splitext(file_h)[0] + " sharedHelper", name_item))
            if ":" in name_item:
                sub_list = re.findall(r"(\S+):\(([\S]+)(?: \*|)\)", name_item)
                invoke_lin = "[%s]" % (os.path.splitext(file_h)[0] + " sharedHelper")
                for sub_item in sub_list:
                    def _type(txt):
                        if txt == "BOOL":
                            return "true"
                        if txt == "id":
                            return "@\"%s\"" % get_random_num(random.choice(range(5, 10)))
                        if txt == "int":
                            return get_random_num(random.choice(range(10, 15)))
                        if txt == "NSString":
                            return "@\"%s\"" % get_random_str(random.choice(range(10, 15)))
                        if txt == "UIView":
                            return "[UIView alloc]"

                    invoke_lin = "%s %s:%s" % (invoke_lin, sub_item[0], _type(sub_item[1]))
                invoke_list_t.append("[" + invoke_lin + "];\n")
    import_file.close()
    random.shuffle(invoke_list_t)
    for item in invoke_list_t:
        invoke_list.write(item)
    invoke_list.close()


# get_list(100)

lins = open(r"E:\Out_Mix\Out\new\out_12_06_152025\mix.m").readlines()

print len(lins)
i = 0
count = 0
out_txt = ""
while len(lins) >= 1:
    num = random.choice(range(30, 50))
    o_lin = ""
    for i in range(num):
        if len(lins) == 0:
            break
        item = random.choice(lins)
        o_lin = o_lin + "\t\t\t" + item
        lins.remove(item)
    out_txt = out_txt + "\t\ttry{\n%s\t\t}\n\t\tcatch " \
                        "(NSException *exception) {\n\t\t\tNSLog(@\"MixScpritError\");\n\t\t}\n\n" % o_lin + "\n"
    count = count + 1
print count

with open(create_path + "\\" + "out_use.txt", 'w+') as function_o:
    function_o.close()
out_use = open(create_path + "\\" + "out_use.txt", "r+")
out_use.write(out_txt)
out_use.close()
# print "\t\ttry{\n\t\t%s\t\t}\n\t\tcatch (NSException *exception) {\n\t\t\n\t\t}" % lin
