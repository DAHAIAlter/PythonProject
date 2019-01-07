#-*-coding:utf-/8-*-
import random
import string




for i in range(1):
    ran_str = ''.join(random.sample(string.ascii_letters + string.digits, random.randint(5, 12)))
    fp = open("D:\\PycharmProjects\\Hellow\\" + ran_str + ".txt", 'w+')
    
    fp.write(''.join(random.sample(string.ascii_letters + string.digits, random.randint(20, 80))))
    fp.close()

