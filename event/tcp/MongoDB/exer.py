import re

f = open('/home/tarena/aid1808/tcp/MongoDB/test.txt')
data = f.read()
pattern = r'-?\d+\.?\d*%?'
l = re.findall(pattern,data)
print(l)