import websockets
import asyncio
import time
#libraries to generate random strings
from random import choice
from string import ascii_uppercase

# The main function that will handle connection and communication
# with the server
async def ws_client():
    print("WebSocket: Client Connected.")
    url = "ws://127.0.0.1:7890"
    # Connect to the server
    async with websockets.connect(url) as ws:
        # Stay alive forever, listen to incoming msgs
        def get_size_of_string(string:str):
            encoded_bytes = string.encode("utf-8")
            size_in_bytes = len(encoded_bytes)
            return size_in_bytes
        counter=1
        while True:
            time.sleep(0.09)
            msg1=''.join(choice(ascii_uppercase) for i in range(368010))
            await ws.send(f"{msg1}")
            start = time.perf_counter()
            msg = await ws.recv()
            order = await ws.recv()
            request_time = time.perf_counter() - start
            print(f"the response time of the message is:{round(request_time,3)}, while the size of the messge={get_size_of_string(msg)}, the order of the packet is{order}")
            counter+=1
            if counter > 1000:
                break
 
# Start the connection
asyncio.run(ws_client())