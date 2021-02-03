import asyncio
from aiohttp import web
import json
from bson import json_util

#get all data
async def get(request):
    db = request.app['db']
    al = []
    async for document in db.collection.find():
        al.append(document)
    return web.Response(text=json.dumps(str(al)))

    
#retrieve the data
async def retrieve(request):
    user = request.match_info.get('user')
    user = str(user)
    db = request.app['db']      
    docs = []
    async for document in db.collection.find({'name': {'$eq': user}}):
        docs.append(document)
    response_obj = json.loads(json_util.dumps(docs)) 
    return web.Response(text=json.dumps(response_obj), status=200)    
        

# insert the data
async def add(request):
    user = request.match_info.get('user')
    db = request.app['db']
    user = str(user)
    db.collection.insert_one({'name': user})
    result = {"status":"data inserted"}
    return web.Response(text=json.dumps(result))


#update the data
async def update(request):
    old_user_name = request.match_info.get("old_user")
    new_user_name = request.match_info.get("new_user")
    db = request.app['db']
    await db.collection.update_one({"name":old_user_name}, {'$set' :{"name":new_user_name}})   
    result = {"status": "data updated"}
    return web.Response(text=json.dumps(result))


#delete the data
async def delete(request):
    user = request.match_info.get('user')
    db = request.app['db']
    await db.collection.delete_many({'name': user})
    result = {"status": "data deleted"}
    return web.Response(text=json.dumps(result))

