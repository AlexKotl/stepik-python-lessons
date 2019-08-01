import asyncio

class ClientServerProtocol(asyncio.Protocol):
    data = {}
    
    def _put(self, key, value, timestamp=None):
        print(f'putting {key} {value}')
        
    def _get(self, key):
        print(f'getting {key}')
        
    def process_data(self, data):
        params = data.split(' ')
        method = params[0]
        key = params[1]
        if method == 'get':
            self._get(key)
            return "ok\n\n"
        elif method == 'put':
            value = params[2]
            timestamp = None if len(params) < 4 else params[3]
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