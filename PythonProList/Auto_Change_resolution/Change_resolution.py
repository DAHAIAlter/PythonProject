# -*- coding=utf-8 -*-
import os
from PIL import Image
import shutil

c_path = "E:\Work\game\pack\iOS"
tag_path = unicode(r"E:\Work\SDK相关\iOS官网提审相关\1.7.0", "utf8")


# size_list = [36, 48, 57, 72, 76, 96, 114, 120, 144, 152, 167, 180, 192, 512, 1024]


def change_icon():
    print tag_path
    print r"E:\Work\SDK相关\SDK_File\iOS\14-拉克斯\弹珠幻想\2_icon\icon-0\\"
    for file_path, file_dis, file_list in os.walk(tag_path):
        print file_list
        for item in file_list:
            if os.path.splitext(item)[1] == ".png":
                print item
                image_info = Image.open(file_path + "\\" + item)
                print image_info.size[0]
                if image_info.size[0] == image_info.size[1] == 512:
                    for item_size in size_list:
                        image_new = image_info.resize((item_size, item_size), Image.ANTIALIAS)
                        image_new.save(tag_path + "\\" + "%s.png" % item_size)


size_list = [57, 76, 72, 114, 120, 144, 152, 167, 180, 1024]
souce_path = unicode(r"E:\Work\SDK相关\iOS官网提审相关\1.7.1\游戏应用icon", "utf8")
pake_path = r"E:\Work\game\Assets\Editor\XUPorter\Mods\EIGameWrapper\Images.xcassets\AppIcon.appiconset"

souce_path_list = []
souce_path_dis = {}
for file_path, file_dis, file_list in os.walk(souce_path):
    for png_item in file_list:
        if os.path.splitext(png_item)[1] == ".png":
            image_info = Image.open(file_path + "//" + png_item)
            print image_info.size[0]
            souce_path_dis[image_info.size[0]] = souce_path + "//" + png_item
            souce_path_list.append(souce_path + "//" + png_item)

print souce_path_dis

for item_size in size_list:
    if item_size in souce_path_dis.keys():
        shutil.copy(souce_path_dis[item_size], pake_path + "\\" + "Icon%s.png" %
                    ("@2x" if item_size == 114
                     else "" if item_size == 57
                    else "-%s" % item_size))

        # for file_path, file_dis, file_list in os.walk(pake_path):
#     print file_list
#     for item in file_list:
#         if os.path.splitext(item)[1] == ".png":
#             print item
#             image_info = Image.open(file_path + "\\" + item)
#             print image_info.size[0]
#             if image_info.size[0] == image_info.size[1] == 1024:
#                 for item_size in size_list:
#                     if item_size in souce_path_dis.keys():
#                         shutil.copy(souce_path_dis[item], pake_path + "\\" + "Icon % s.png" %
#                                     ("@2x" if item_size == 114
#                                      else "" if item_size == 57
#                                     else "-%s" % item_size))

# image_new = image_info.resize((item_size, item_size), Image.ANTIALIAS)
# image_new.save(
#     pake_path + "\\" + "Icon%s.png" %
#     ("@2x" if item_size == 114
#      else "" if item_size == 57
#     else "-%s" % item_size)
# )

# print souce_path_dis[167]
