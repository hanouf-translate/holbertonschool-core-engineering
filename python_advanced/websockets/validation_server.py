#!/usr/bin/env python3

import asyncio
import websockets
from websockets.exceptions import ConnectionClosed, ConnectionClosedOK

connected_clients = set()

async def connection_handler(websocket):
    # connected_clients.add(websocket)
    print("Client connected!")

    try:
        async for message in websocket:
            if len(message.strip()) == 0:
                await websocket.send("ERR: EMPTY")
                continue
            else:
                await websocket.send("OK: " + message)
            print("Received:", message)

            await websocket.send(message)

            

    except Exception as error:
        print("Connection error:", error)

    finally:
        # connected_clients.discard(websocket)
        print("Client disconnected!")

async def main():
    async with websockets.serve(connection_handler,'127.0.0.1', 8765):
        await asyncio.Future()  # run forever

if __name__ == "__main__":
    asyncio.run(main())