# -*- coding:utf-8 -*-
# 生成C#混淆脚本
import re
import os
import sys
import random
import string
import datetime


# 获取原本路径
curr_path = os.path.split(sys.argv[0])[0]

lib_file = open(curr_path + r"/Words/lib.txt")
lib_list = str.split(lib_file.read(), ",")

out_path = r"%s\file\out_%s" % (curr_path, datetime.datetime.strftime(datetime.datetime.now(), "%m_%d_%H%M%S"))
os.makedirs(out_path)
print len(lib_list)


def create_cs():
    cs_txt = ""
    cs_txt = cs_txt + "useing UnityEngine;\n\n"


def get_name():
    if len(lib_list) <= 1:
        return
    item = random.choice(lib_list)
    lib_list.remove(item)
    return random.choice(string.letters) + item + random.choice(string.letters)


def get_random_num():
    return random.choice(range(50, 1000))


fun_list = []


def createclass(name, count):
    global fun_list
    fun_list.append(name)
    return "public class %s{\n%s\n}" % (name, create_cun(name, count))


fun_list = []


def get_invoke(name):
    invoke_txt = ""
    if len(fun_list) <= 2:
        return ""
    invoke_name = random.choice(fun_list)
    while invoke_name == name:
        invoke_name = random.choice(fun_list)
    print invoke_name
    cs_file = open(invoke_name + ".cs")
    invoke_fun_list = re.findall(r"public *(?:void|int|bool) *([^\(]+)", cs_file.read())
    print name
    print len(invoke_fun_list)
    obj_name = get_name()
    invoke_txt = invoke_txt + "\n\t\t%s %s = new %s();\n" % (invoke_name, obj_name, invoke_name)
    count = random.choice(range(3, 5))
    for i in range(count):
        invoke_txt = invoke_txt + "\t\t%s.%s();\n" % (obj_name, random.choice(invoke_fun_list))
    return invoke_txt


print get_invoke("ambulatory_language")


def create_cun(class_name, count):
    cs_txt = ""
    variable_a = get_name()
    variable_b = get_name()
    for i in range(count):
        f_type = random.choice(["void", "int", "bool"])
        if f_type == "void":
            f_name = get_name()
            cs_txt = cs_txt + "\tpublic void %s() {%s\n" \
                              "\t\tint %s = Random.Range(10,%s);\n" \
                              "\t\tint %s = Random.Range(15,%s);\n\t}\n" % (
                         f_name, get_invoke(class_name), variable_a, get_random_num(), variable_b, get_random_num())
        if f_type == "int":
            cs_txt = cs_txt + "\tpublic int %s() {%s\n" \
                              "\t\tint %s = Random.Range(10,%s);\n" \
                              "\t\tint %s = Random.Range(15,%s);\n" \
                              "\t\treturn %s+%s;\n" \
                              "\t}\n" % \
                     (
                         get_name(), get_invoke(class_name), variable_a, get_random_num(), variable_b, get_random_num(),
                         variable_a, variable_b)
        if f_type == "bool":
            cs_txt = cs_txt + "\tpublic bool %s() {%s\n\t\tint %s = Random.Range(10,%s);\n" \
                              "\t\tint %s = Random.Range(15,%s);\n\t\tif(%s>=%s) {\n" \
                              "\t\t\treturn true;\n\t\t}\t\n\t\treturn false;\n\t}\n" % \
                     (
                         get_name(), get_invoke(class_name), variable_a, get_random_num(), variable_b, get_random_num(),
                         variable_a, variable_b)
    return cs_txt


def create_script(class_name, f_count):
    if not os.path.exists(out_path):
        print "导出脚本文件路径有误"
        return
    os.chdir(out_path)
    if os.path.exists(class_name + ".cs"):
        os.remove(class_name + ".cs")
    with open(class_name + ".cs", 'w') as new_file:
        new_file.close()
    script_file = open(class_name + ".cs", "r+")
    script_file.write("using UnityEngine;\n\n")
    script_file.write(createclass(class_name, f_count))


for i in range(120):
    create_script(get_name(), random.choice(range(10, 20)))

print fun_list
