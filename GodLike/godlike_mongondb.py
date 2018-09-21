from pymongo import MongoClient
import os


#连接 大神推荐系统测试服 并查找数据
def recommend_system(col_name, myquery_dirc):  #clo_name 集合名称 ; myquery_dirc 筛选条件  如：myquery_dirc = {"tag_name": "荒野行动"}
    available_list = []
    recommend_system = MongoClient("mongodb://qa_ydb:netease#ydb@10.200.33.32:30011/godp?authMechanism=SCRAM-SHA-1")
    db = recommend_system["godp"][col_name]
    myquery = myquery_dirc
    for i in db.find(myquery):
        available_list.append(i)
    return available_list

#连接 大神App_server测试服 并查找数据
def App_server(col_name, myquery_dirc):
    available_list = []
    recommend_system = MongoClient("mongodb://qa_ydb:netease#ydb@10.200.33.32:30011/god?authMechanism=SCRAM-SHA-1")
    db = recommend_system["god"][col_name]
    myquery = myquery_dirc
    for i in db.find(myquery):
        available_list.append(i)
    return available_list
