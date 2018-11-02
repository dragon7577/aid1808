import re

# s = 'heLLo world'
# pattern = r'Hello'
# regex = re.compile(pattern,flags=re.I)  #flags=re.I匹配时忽略字母大小写 

# s = '''hello world
# hello kitty
# 你好 北京
# '''
# pattern = r'.+'
# regex = re.compile(pattern,re.S) # re.S使.可以匹配换行

s = '''hello world
Hello kitty
nihao 北京
'''
pattern = r'^hello'
regex = re.compile(pattern,re.M|re.I) # re.M使其可以匹配每行的开头结尾
                                      #  re.M|re.I 同时使用多个

# s = '''hello world
# hello kitty
# nihao 北京
# '''
# pattern = r'''hello  #匹配hello
# \s+                  #匹配空格
# world                #匹配world
# '''
# regex = re.compile(pattern,re.X)  #re.X可以给正则表达式添加注释

try:
    s = regex.search(s).group()
except Exception:
    print('没有匹配到内容')
else:
    print(s)