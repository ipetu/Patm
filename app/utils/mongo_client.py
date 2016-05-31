#!/usr/bin/env python
# -*- coding: utf-8 -*-


import pymongo
from tornado.options import options
import app.dbConfig
conn = None
db = None
try:
    from pymongo.objectid import ObjectId
except ImportError:
    from bson.objectid import ObjectId

class MongoClient:
    @staticmethod
    def init():
        global conn
        global db
        #conn = pymongo.Connection(host='192.168.1.27',port=27017)
        conn = options.mongo_conn    #pymongo.Connection(options.mongo_conn)
        db = conn.douqu

    @staticmethod
    def insert(post_json,collection):
        global db
        table = db[collection] 
        return table.insert(post_json),db.error()

    @staticmethod
    def remove(where,collection):
        if where is None or len(where)==0:
            return
        global db
        table = db[collection]
        table.remove(where)

    @staticmethod
    def update(where,updated,collection):
        if where is None or len(where)==0:
            return
        global db
        table = db[collection]
        return table.update(where,updated,multi=True)

    @staticmethod
    def upsert(where,updated,collection):
        if where is None or len(where)==0:
            return
        global db
        table = db[collection]
        return table.update(where,updated,upsert=True)

    @staticmethod
    def find(where,collection,orderby,asc,index,count_pre_page):
        global db
        table = db[collection]
        if orderby == "":
             return table.find(where).limit(count_pre_page).skip(index)
        else:
            if asc:
                return table.find(where).sort(orderby,pymongo.ASCENDING).limit(count_pre_page).skip(index)
            else:
                return table.find(where).sort(orderby,pymongo.DESCENDING).limit(count_pre_page).skip(index)


    @staticmethod
    def finds(where,collection,filter=None,orderby="",asc=True,index=0,count_pre_page=0):
        global db
        table = db[collection]
        if orderby == "":
             return table.find(where).limit(count_pre_page).skip(index)
        else:
            if asc:
                return table.find(where).sort(orderby,pymongo.ASCENDING).limit(count_pre_page).skip(index)
            else:
                return table.find(where).sort(orderby,pymongo.DESCENDING).limit(count_pre_page).skip(index)

    @staticmethod
    def find_one(where,collection,filter=None):
        global db
        table = db[collection]
        if filter !=None or filter !="":
            return table.find_one(where,filter)
        else:
          return table.find_one(where)

    @staticmethod
    def find_all(where,collection,filter=None):
        global db
        table = db[collection]
        if filter !=None or filter !="":
            return table.find(where,filter)
        else:
            return table.find(where)

    @staticmethod
    def find_and_modify(where,updated,collection):
        if where is None or len(where)==0:
             return
        global db
        table = db[collection]
        return table.find_and_modify(where,updated,multi=True, new=True)

    @staticmethod
    def  getObjectByID(id,collection):
        global db
        table = db[collection]
        where={'_id':ObjectId(id)}
        """
        where_dumps=json.dumps(where, cls=JSONEncoder)
        
        where_dic=json.loads(where_dumps, object_hook=decoder)
        """
        return table.find_one(where)

    @staticmethod
    def delete(where,collection):
        if where is None or len(where)==0:
            return
        global db
        table = db[collection]
        table.remove(where)
    
    @staticmethod
    def count(where,collection):
        global db
        table = db[collection]
        return table.find(where).count()
    
    @staticmethod
    def aggregate_one(keys,collection,where={},count_name="count"):
        global db
        table = db[collection]
        result = {}
        result = table.aggregate([
                                    {"$match":where},
                                        {"$group":
                                                {"_id":keys,count_name: {"$sum": 1}}
                                         }
                                    ])

        if result.has_key("result"):
            return result.get("result")
        else:
            return None
