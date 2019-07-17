import os
import tempfile
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument("--key")
parser.add_argument("--val")
args = parser.parse_args()

data = {}
storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
if not os.path.isfile(storage_path):
    open(storage_path, 'w').close()

with open(storage_path, 'r+') as f:
    content = f.read()
    if content != '':
        data = json.loads(content)
    
if args.val == None and args.key in data:
    print(data[args.key])
else:
    if (args.key in data and data[args.key] != None):
        data[args.key] += ', ' + args.val
    else:
        data[args.key] = args.val
        
    with open(storage_path, 'w') as f:
        f.write(json.dumps(data))