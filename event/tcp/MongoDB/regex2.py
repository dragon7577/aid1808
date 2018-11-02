import re

pattern = r'(?P<cat>ab)cd(?P<dog>ef)'

regex = re.compile(pattern)

#获取match对象
obj = regex.search('abcdefgh',pos=0,endpos=6)

#obj属性变量
print(obj.pos)  #目标自字串的开始位置
print(obj.endpos)   #目标字串的结束位置
print(obj.re)       #正则表达式
print(obj.string)   #目标字符串
print(obj.lastgroup)#最后一组组名
print(obj.lastindex)#最后一组序号
print('=====================================')

print(obj.span())  #匹配内容的起止位置
print(obj.start()) #匹配内容的开始位置
print(obj.end())   #匹配内容的结束位置
print(obj.group()) #获取匹配到的内容
print(obj.group(1))#获取匹配到的第1子组对应的内容
print(obj.group('dog')) #获取组名为dog对应的内容
print(obj.groupdict())  #捕获组字典
print(obj.groups())     #捕获子组对应内容