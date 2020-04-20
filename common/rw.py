import re
import importlib
import sys
importlib.reload(sys)
# 读写文件 从一个文件读写到另一个文件

# 判断是否为中文的正则表达式
# pchinese = re.compile('([\u4e00-\u9fa5]+)+?')
# 打开要提取的文件
f = open(".gitignore")
# 打开要写入的文件
fw = open("a.MD", "w")
# 循环读取要读取文件的每一行
for line in f.readlines():
    # 使用正则表达获取中文
    m = str(line)
    if m:
        # 将获取中文内容按空格分开
        str2 = m
        # 写入文件
        fw.write(str2)
        # 不同行的要换行
# 关闭文件
f.close()
fw.close()
