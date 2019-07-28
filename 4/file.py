import tempfile
import os

class File:
    def __init__(self, filename):
        self.filename = filename

    def write(self, content):
        with open(self.filename, 'w') as f:
            f.write(content)
    
    def read(self):
        with open(self.filename, 'r') as f:
            return f.read()
        
    def __str__(self):
        return self.filename
        
    def __add__(self, file2):
        new_filename = os.path.basename(self.filename) + '.' + os.path.basename(file2.filename)
        new_file = File(os.path.join(tempfile.gettempdir(), new_filename)) 
        new_file.write(self.read() + file2.read())
        return new_file
        
    def __iter__(self):
        self.f = open(self.filename, "r")
        return self
        
    def __next__(self):
        line = self.f.readline()
        if not line:
            raise StopIteration
        return line