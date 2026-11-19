#!/usr/bin/env python3

import asyncio
import websockets

async def connection_handler(websocket):
    print("Client connected!")

    try:
        async for message in websocket:
            print("Received:", message)

            await websocket.send(
                websocket.send(message)
            )

    except Exception as error:
        print("Connection error:", error)

    finally:
        print("Client disconnected!")


async def main():
    async with websockets.serve(connection_handler,'127.0.0.1', 8765):
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())