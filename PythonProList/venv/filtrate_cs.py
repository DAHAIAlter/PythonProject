# -*- coding:utf-8 -*-
# 被注释的代码不会添加到工程中
# resource中的文件会被打入包体中
# 私有函数自身调用
# 受保护的函数在子类的重写
# 函数被添加到侦听事件中
import os
import re

RE_FNAME = r"\n*(private|public|)\s*(override|)\s*(int|void|bool|string)\s*([^\(\.\n\:\= ]+)\s*(\(.*\))"
RE_INVOKE = r"((this\.|)%s\([^\:\)]*?\))"

Target_Path = r"E:\Work\game\Assets\Script\BaseScript\Module\MainModule\MainUI.cs"
Target_Path_1 = r"E:\Work\game\Assets\Script\BaseScript\UI\UIView.cs"
targget_file = open(Target_Path_1)
targget_txt = targget_file.read()
capture_list = re.findall(RE_INVOKE % "TestPrintStack", targget_txt)
for item in capture_list:
    print item
print len(capture_list)

# 子类
