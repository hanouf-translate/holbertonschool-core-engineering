#!/usr/bin/env python3

import asyncio
import websockets

async def echo(websocket):
    async for message in websocket:
        await websocket.send(messag)


async def main():
    async with websockets.serve(echo,'127.0.0.1', 8765):
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())