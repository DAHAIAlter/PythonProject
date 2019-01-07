# -*- coding:utf8 -*-
import os
from PIL import Image

path = unicode(r"E:\Work\SDK相关\SDK_File\iOS\14-拉克斯\诺斯里特（诺文尼亚）\诺斯里特\诺斯里特0910\3_loading\加载页",
               "utf8")
print path
if os.path.exists(path+".png"):
    Image.open(path + ".png").save(path + ".jpg")
