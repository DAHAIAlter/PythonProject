# -*- coding:utf-8 -*-
# 自动修改SDK相关文件。

import re
import os


# from PIL import Image


def change_b():
    b_path = r"E:\Work\game\Assets\Editor\Build\BuildUtils.cs"
    build_utils = open(b_path, "r+")

    def _change(aa):
        print aa.group(0)
        return "\"com.bwdl.zhanghuanhuan\""

    change = re.sub("\"net.game-magic.A2-ProjectProduction\"", _change, build_utils.read())
    build_utils.seek(0, 0)
    build_utils.truncate()
    build_utils.write(change)
    build_utils.close()


def change_item(tag_txt, tag, new):
    def _change(matched):
        print matched.group(1)
        lin = str.replace(matched.group(0), matched.group(1), new)
        print lin
        return lin

    tag_txt = re.sub("public const string %s *= \"(.+)\"" % tag, _change, tag_txt)
    return tag_txt


def change_p():
    p_path = r"E:\Work\game\Assets\Script\BaseScript\Utility\PlatformUtil.cs"
    p_file = open(p_path, "r+")
    p_content = p_file.read()
    p_content = change_item(p_content, "MOTHER_LABEL", "100001")
    p_content = change_item(p_content, "CHANNEL_LABEL", "eichannel_pjlakesi_dzhx")
    p_content = change_item(p_content, "CHANNEL_CODE", "CH0536")
    p_file.seek(0, 0)
    p_file.truncate()
    p_file.write(p_content)


def change_callback_item(tag_txt, new):
    def _change(matched):
        print matched.group(1)
        lin = str.replace(matched.group(0), matched.group(1), new)
        print lin
        return lin

    tag_txt = re.sub("#if UNITY_IOS\n\s*string callbackUrl = baseUrl *\+ *\"/uan1pay/(.+)\"", _change, tag_txt)
    return tag_txt


def change_r():
    r_path = r"E:\Work\game\Assets\Script\BaseScript\UI\Nodes\RechargeNode\RechargeManager.cs"
    r_file = open(r_path, "r+")
    r_content = r_file.read()
    r_content = change_callback_item(r_content, "pjlakesi")
    r_file.seek(0, 0)
    r_file.truncate()
    r_file.write(r_content)


# change_r()
# change_p()
# change_b()

# def load_certificate():
"""
c_path = "E:\Work\game\pack\iOS"
tag_path = unicode(r"E:\Work\\SDK相关\\SDK_File\\iOS\14-拉克斯\\弹珠幻想\\2_icon\\icon-0", "utf8")
print r"E:\Work\SDK相关\SDK_File\iOS\14-拉克斯\弹珠幻想\2_icon\icon-0\\"
for file_path, file_dis, file_list in os.walk(tag_path):
    print file_list
    for item in file_list:
        if os.path.splitext(item)[1] == ".png":
            print item
            image_info = Image.open(file_path + "\\" + item)
            print image_info.size[0]
            if image_info.size[0] == image_info.size[1] == 1024:
                image_new = image_info.resize((57, 57), Image.ANTIALIAS)
                image_new.save(tag_path + "\out\\" + "Icon-%s.png" % "57")
"""
pro_path = r"E:\Work\game"
if not os.path.exists(pro_path):
    print "error"
pro_pack = pro_path + "pack"
#
# for f_path, f_dirs, f_list in os.walk(unicode(r"E:\Work\SDK相关\SDK_File\iOS\14-拉克斯\拉克丝-弹珠幻想1009\弹珠幻想素材包\2_icon\icon-0", "utf8")):
#     for file_item in f_list:
#         if os.path.splitext(file_item)[1] == ".p12":
#             if "dev" in file_item and "push" in file_item:
#                 print file_item
#             if "dis" in file_item and "push" in file_item:
#                 print file_item
#             if "dis" in file_item and "push" not in file_item:
#                 print file_item
#             if "dev" in file_item and "push" not in file_item and "aps" not in file_item:
#                 print file_item
#         if os.path.splitext(file_item)[1] == ".mobileprovision":
#             if "dis" in file_item:
#                 print file_item
#             if "dev" in file_item:
#                 print file_item
#             if "adhoc" in file_item:
#                 print file_item

            # print unicode("你好", "gbk")
