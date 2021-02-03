from aiohttp import web
import asyncio

from setup import setupDB
from routes import routes


loop  = asyncio.get_event_loop()
db = loop.run_until_complete(setupDB())


app = web.Application()
app['db'] = db

routes(app)

web.run_app(app)