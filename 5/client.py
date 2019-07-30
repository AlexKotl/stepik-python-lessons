class Client:
    def __init__(self, host, port, timeout=None):
        pass
    
    def get(self, metric):
        pass
        
    def put(self, metric, value, timestamp=None):
        pass
    
class ClientError(Exception):
    pass