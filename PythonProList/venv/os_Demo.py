# -*- coding:utf-8 -*-

import os

# Windows 返回 'nt'; Linux 返回'posix'
print os.name

# 调用系统控制台 返回值中文会乱码
# os.system("ipconfig")
# os.system("ping baidu.com")

# cmd_file = os.popen("ipconfig")
# print cmd_file.read();

os.system("ping baidu.com")
