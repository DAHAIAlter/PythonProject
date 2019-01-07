# -*-coding: utf-8 -*-


# "<uses-permission .\S+\"(.+)\".+"     XML权限文件获取
# 正则表达式识别特定标识
import re
import os
print "XML自动修改工具Demo1"

def load_xml(path):
    if (not os.path.isfile(path)):
        print path+"  is a Error Path"
        return
    if os.path.splitext(path)[1]!=".xml":
        print "file %s is no a xml file" % path
        return

    xml = open(path)    # 加载xml文件
    xml_str = xml.read()    # 获取xml文本

    # Load xml Item
    xml_tag = "<uses-permission .\S+\"(.+)\".+"
    xml_pag_name = "package=\"(.+)\""
    xml_activity = "<activity[\s\S]*?</activity>"
    xml_provider = "<provider[\s\S]*?</provider>"
    xml_activity_line = "<activity[^>]*/>"
    xml_list = re.findall("<uses-permission .\S+\"(.+)\".+", xml_str)

    #print  xml_list

    for liteItem in xml_list:
        print liteItem



def load_cfg():
    xml_cfg = open(r"D:\PycharmProjects\Hellow\pow_cfg.txt").read()


load_xml(r"D:\PycharmProjects\Hellow\GameNode.txt")
