from streaming_client import StreamingClient
import logging


def on_msg(data):
    print(data)

logging.basicConfig(level=logging.INFO)
sc = StreamingClient()
sc.register_all_symbols()
sc.run(on_msg)