脚本自动生成工具以及引用自动生成工具
python 2.7

>生成文件
|生成的文件为相应的.h和.m文件,文件名,函数名,类名全为随机,而类会在自身随机调用,而为了避免函数形成随机调用链所以被调用的函数里都不会进行别的调用
|针对OC层调用,由于混淆函数存在不确定因素的影响,有可能会导致进程卡死,所以在实现调用是用了try来进行尝试运行
|函数调用对应为 (int)->随机数字 (NSString *)->随机字符串  (UIView *)->[UIVew alloc] (BOOL)->true