# -*- coding:UTF-8 -*-
# coding =utf8
# Python默认编码格式为ASCII 无法识别中文

# print "Hello Python"  # 输出英文
# print "你好 Python"  # 输出中文
# print """Line1
# line2"""            # 多行输入
# print "Item 1"; print "Item2"
########################################
"""path = r"E:\1.5.0压测1.txt"
print path
# path_xml = "C:\\Users\\Administrator\\Desktop\\backUp\\nosdk\\AndroidManifest.xml"
b = open(unicode(path, "utf-8"))

C:\Users\Administrator\Desktop\mix_file\img\after\avatar_bg_1.PNG

print b.read()"""


########################################

# 修改图片,音频等文件中的UTF8值
def change_md5(path):
    img = path
    print img
    img_after = open(unicode(img, "utf-8"), 'a')
    img_after.write("###@@@")
    img_after.close()
    return [img_after]


change_file = change_md5(r"D:\PycharmProjects\Hellow\pow_cfg.txt")
