import re

try:
    f = open('/home/tarena/aid1808/tcp/MongoDB/day35.txt')
    print("打开文件")
    s = f.read(1024)
    print('读取文件')

# s = 'zhang:1993 li:1992'
    st = s.decode()

    pattern = r'*'
    l = re.findall(pattern,st)
    print('文件是：',l)
    f.close()

#compile对象调用
except:
    print('打开文件失败')
# regex = re.compile(pattern)
# l = regex.findall(s)
# print(l)

# l1 = re.split(r'\s+','Hello   world!')
# print(l1)

# s = re.sub(r'\s+','##','Hello world!    nihao beijing',2)
# print(s)

# s = re.subn(r'\s+','##','Hello world!    nihao beijing',2)
# print(s)

# s = re.match(r'A-Z','Hello world!    nihao beijing')
# print(s)