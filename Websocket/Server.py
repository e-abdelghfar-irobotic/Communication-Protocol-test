import websockets
import asyncio
#libraries to generate random strings
from random import choice
from string import ascii_uppercase 
# Creating WebSocket server
async def ws_server(websocket):
    print("WebSocket: Server Started.")
 
    try:
        counter=1
        while True:
            # Receiving values from client
            await websocket.recv()             
            await websocket.send(f"{''.join(choice(ascii_uppercase) for i in range(368010))}")
            await websocket.send(str(counter))
            print(f"The sent packet order:{counter}")
            counter+=1
 
    except websockets.ConnectionClosedError:
        print("Internal Server Error.")
 
 
async def main():
    async with websockets.serve(ws_server, "localhost", 7890,):
        await asyncio.Future()  # This will keep the server alive and run continuously 
 
if __name__ == "__main__":
    asyncio.run(main())