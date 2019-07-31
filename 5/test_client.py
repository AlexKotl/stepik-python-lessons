from client import Client

client = Client("127.0.0.1", 8888, timeout=15)
print(client.get("*"))