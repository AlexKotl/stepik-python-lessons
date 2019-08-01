import socket
import time

class Client:
    def __init__(self, host, port, timeout=None):
        self.sock = socket.create_connection((host, port), timeout)
    
    def get(self, key):
        result = {}
        try:
            self.sock.send(f"get {key}\n".encode())
            data = self.sock.recv(2048).decode("utf8").split("\n")
            if data[0] == 'error':
                raise ClientError
            for row in data[1:]:
                if row == '':
                    continue
                row = row.split(' ')
                name = row[0]
                value = float(row[1])
                timestamp = int(row[2])
                
                if name not in result:
                    result[name] = []
                result[name].append((timestamp, value))
        except socket.error as err:
            print("Get data error:", err)
            raise ClientError
        
        return result
        
    def put(self, key, value, timestamp=None):
        timestamp = timestamp or str(int(time.time()))
        string = f"put {key} {value} {timestamp}\n"
        self.sock.sendall(string.encode())
        data = self.sock.recv(2048).decode("utf8").split("\n")
        if data[0] == 'error':
            raise ClientError
    
class ClientError(Exception):
    pass

class ClientSocketError(ClientError):
    pass

class ClientProtocolError(ClientError):
    pass