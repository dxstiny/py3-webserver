from argparse import ArgumentParser

import asyncio
from aiohttp import web
from aiohttp_index import IndexMiddleware

argumentParser = ArgumentParser(description="Python Basic Webserver")
argumentParser.add_argument("-p", "--port", required=False,
default=8080, help="port")
arguments = argumentParser.parse_args() # get arguments

async def getHandler(request: web.Request):
    print("[GET]", await request.content.read())
    return web.Response(status = 200, text = "success!")

async def postHandler(request: web.Request):
    print("[POST]", await request.content.read())
    return web.Response(status = 200, text = "success!")

async def headHandler(request: web.Request):
    print("[HEAD]", await request.content.read())
    return web.Response(status = 200, text = "success!")

async def putHandler(request: web.Request):
    print("[PUT]", await request.content.read())
    return web.Response(status = 200, text = "success!")

async def patchHandler(request: web.Request):
    print("[PATCH]", await request.content.read())
    return web.Response(status = 200, text = "success!")

async def deleteHandler(request: web.Request):
    print("[DELETE]", await request.content.read())
    return web.Response(status = 200, text = "success!")

app = web.Application(middlewares=[IndexMiddleware()])

app.router.add_get('/test/get', getHandler)
app.router.add_post('/test/post', postHandler)
app.router.add_head('/test/head', headHandler)
app.router.add_put('/test/put', putHandler)
app.router.add_patch('/test/patch', patchHandler)
app.router.add_delete('/test/delete', deleteHandler)

app.router.add_static('/', '.')
asyncio.run ( web._run_app(app, port=arguments.port) )
