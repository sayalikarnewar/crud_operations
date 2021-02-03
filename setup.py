import motor.motor_asyncio


async def setupDB():
    client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017")
    db = client.api
    return db