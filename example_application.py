# Standard Python modules
from time import sleep

# Import everything from the audiosocket module
import asyncio
from audiosocket import *

# Create a new Audiosocket instance, passing it binding
# information in a tuple just as you would a raw socket

WS_ADDRESS = '127.0.0.1'
WS_PORT = 8765

async def main():
  # Create a new Audiosocket instance
  audiosocket = Audiosocket(("127.0.0.1", 9092))

  # This will block until a connection is received
  conn = await audiosocket.listen()

  print('Received connection from {0}'.format(conn.peer_addr))

  # While a connection exists, send all received audio back to Asterisk (creates an echo)
  async with websockets.connect(f'ws://{WS_ADDRESS}:{WS_PORT}') as websocket:

    while conn.connected:
      audio_data = await conn.read(websocket)
      conn.write(audio_data)

    print('Connection with {0} over'.format(conn.peer_addr))


# Run the asynchronous main function
asyncio.run(main())
