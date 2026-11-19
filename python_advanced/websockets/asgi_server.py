#!/usr/bin/env python3

from starlette.applications import Starlette
from starlette.responses import HTMLResponse
from starlette.routing import Route, WebSocketRoute

async def homepage(request):
    # HTML response here
    return HTMLResponse("<h1>WebSocket Echo</h1>")

async def websocket_endpoint(websocket):
    await websocket.accept()
    # message loop here
    async for message in websocket.iter_text():
        await websocket.send_text(f"Message text was: {message}")
    await websocket.close()

app = Starlette(routes=[
    Route("/", homepage),
    WebSocketRoute("/ws", websocket_endpoint),
])