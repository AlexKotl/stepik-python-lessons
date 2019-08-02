import asyncio

class ClientServerProtocol(asyncio.Protocol):
    data = {}
    
    def _put(self, key, value, timestamp=None):
        if key not in self.data:
            self.data[key] = []
        new_record = (key, value, timestamp)
        if new_record not in self.data[key]:
            self.data[key].append(new_record)
        
    def _get(self, key):
        result = 'ok\n'
        if key == '*':
            for metric in self.data.values():
                if len(metric) > 0:
                    for key, value, timestamp in metric:
                        result += f"{key} {value} {timestamp}\n"
        elif key in self.data:
            for key, value, timestamp in self.data[key]:
                result += f"{key} {value} {timestamp}\n"
        result += "\n"
        return result
        
    def process_data(self, data):
        params = data.split(' ')
        method = params[0]
        key = params[1].rstrip()
        if method == 'get':
            return self._get(key)
        elif method == 'put':
            value = params[2].rstrip()
            timestamp = None if len(params) < 4 else params[3].rstrip()
            self._put(key, value, timestamp)
            return "ok\n\n"
        else:
            return "error\nwrong command\n\n"
        
        return "responce for ".format(data)
        
    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        resp = self.process_data(data.decode())
        self.transport.write(resp.encode())

def run_server(host, port):
    loop = asyncio.get_event_loop()
    coro = loop.create_server(
        ClientServerProtocol,
        host, 
        port
    )

    server = loop.run_until_complete(coro)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()

run_server('127.0.0.1', 8888)