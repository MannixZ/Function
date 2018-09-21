import pymongo
from bson.objectid import ObjectId


myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mycol = myclient["rounood"]["mycol2"]

# 查找第一条
x = mycol.find_one({"_id" : ObjectId("5b850047072d3465a74c8a0a")})
print(x)
# for x in mycol.find({'id':ObjectId('50f0d76347f4ec148890ef1e')}):   #展示所有内容
#     print(x)

# 查找指定数据
# myquer = {"name":"第二条"}
# for x in mycol.find(myquer):
#         print(x)

'''
插入数据
'''
# 插入一条数据
# mydict = {"name":"wuyanzu", "title":"fensi", "url":"www.baidu.com", "age":18, "height":130}
# x = mycol.insert_one(mydict)
# print(x)
# print("我是id值: %s" % x.inserted_id)

# 插入多条数据
# mylist = []
# for i in range(15,17):
#         i = str(i)
#         j = int(i)
#         mydict = {"_id": i, "name": "wuyanzu"+i, "title": "fensi"+i, "url": "www.baidu.com"+i, "age": i, "height": j*j}
#         mylist.append(mydict)
#         # print(mylist)
# x = mycol.insert_many(mylist)
# print(x.inserted_ids)


'''
查询数据
'''
# 查询一条数据
# x = mycol.find_one()
# print(x)
#
# # 查询多条数据
# for i in mycol.find():
#         print(i)
#
# # 查询之后只显示某个key
# for y in mycol.find({},{"_id":0, "name":1}):
#         print(y)
#
# 查询特定条件  name:wuyanzu
# for a in mycol.find({"name":"wuyanzu15"}):
#         print(a)
#
# # 根据正则去查询
# print("我是正则")
# myquery = { "name": { "$regex": "^wuyanzu1" } }
# for b in mycol.find(myquery).limit(3):
#         print(b)

'''
修改数据
'''
# 把 name : wuyanzu15 改为 WUYANZU15
# newvalue = {"$set": {"name": "WUYANZU15"}}
# mycol.update_one({"name":"wuyanzu15"}, newvalue)

# 一次修改多个数据
# name = {"name":{"$regex": "^WUYANZU"}}
# newvalue = {"$set": {"name": "wuyanzu15"}}
# mycol.update_many(name, newvalue)

'''
数据排序
'''
# sort()  默认为升序, -1为降序
# for x in mycol.find({}, {"_id": 0}).sort("name", -1):
#         print(x)

'''
数据删除
'''
# 删除单个name：wuyanzu15
# myquery = {"name":"wuyanzu15"}
# mycol.delete_one(myquery)

# 删除多个
# myquery = {"name": {"$regex":"wuyanzu1"}}
# x = mycol.delete_many(myquery)
# print(x.deleted_count)

'''
删除文档
'''
# db_rounood = myclient["rounood"]["rounood"]
# x = db_rounood.delete_many({})
# print(x.deleted_count)

'''
删除集合
'''
# db_rounood = myclient["rounood"]["rounood"]
# db_rounood.drop()




