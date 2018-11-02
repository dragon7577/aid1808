from pymongo import MongoClient

#创建数据连接
conn = MongoClient("localhost",27017)

#创建数据库对象
db = conn.stu

#创建集合对象
myset = db.class4

#数据操作
# print(dir(myset))

# 插入文档
# myset.insert_one({'name':'任贤齐','role':'令狐冲'})
# myset.insert_many([{'name':'许晴','role':'任盈盈'}])
# myset.insert({'name':'古天乐'})
# myset.insert([{'name':'李若彤','role':'小龙女'},{'name':'刘亦菲','role':'王语嫣'}])
# myset.save({'_id':1,'name':'李亚鹏','role':'令狐冲'})
# 查找操作
cursor = myset.find({'role':{'$exists':True}},{'_id':0})
# for i in cursor:
#     print(i['name'],'---',i['role'])

# print(cursor.next())

# for i in cursor.skip(1).limit(2):
#     print(i)

# for i in cursor.sort([('name',1),('role',-1)]):
#     print(i['name'],'---',i['role'])
#删除操作
# myset.delete_one({'name':'古天乐'})
# dir = {'$or':[{'role':{'$exists':False}},{'name':'古天乐'}]}
# d = myset.find_one(dir)
# print(d)
# myset.delete_many([{''},{}])
#创建索引


#查看索引
# for i in myset.list_indexes():
#     print(i)

#删除索引
# myset.drop_index('name_1')

#删除所有索引，不会删除'_id' 
# myset.drop_indexes()

#其他索引类型
index = myset.create_index('name',unique=True)

#关闭数据库连接
conn.close()