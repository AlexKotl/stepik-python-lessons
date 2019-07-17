import json
import functools

def to_json(func):
    @functools.wraps(func)
    def wrapped(*kargs, **kwargs):
        return json.dumps(func(*kargs, **kwargs))
    return wrapped

# @to_json
# def get_data():
#     return {
#         'data': 42
#     }
# 
# print(get_data())