from bs4 import BeautifulSoup
import re
import os


# Вспомогательная функция, её наличие не обязательно и не будет проверяться
def build_tree(start, end, path):
    link_re = re.compile(r"(?<=/wiki/)[\w()]+")
    files = dict.fromkeys(os.listdir(path))
    
    # Проставить всем ключам в files правильного родителя в значение, начиная от start
    for file in files:
        if files[file] == None:
            files[file] = []
        content = open(os.path.join(path, file), "r").read()
        for url in link_re.findall(content):
            # skip the rest of urls
            if url not in files:
                continue
            if url not in files[file] and file != url:
                files[file].append(url)
    return files


def bfs2(graph, start, goal):

    if start == goal:
        return [start]
    visited = {start}
    queue = [(start, [])]

    while queue:
        current, path = queue.pop(0)
        visited.add(current)
        for neighbor in graph[current]:
            if neighbor == goal:
                return path + [current, neighbor]
            if neighbor in visited:
                continue
            queue.append((neighbor, path + [current]))
            visited.add(neighbor)   
    return None
    
# Вспомогательная функция, её наличие не обязательно и не будет проверяться
def build_bridge(start, end, path):
    files = build_tree(start, end, path)
    bridge = bfs2(files, start, end) or []
    
    return bridge

def parse(start, end, path):
    if start == end:
        bridge = [start]
    else:
        bridge = build_bridge(start, end, path)
    
    out = {}
    for file in bridge:
        with open(os.path.join(path, file)) as data:
            soup = BeautifulSoup(data, "lxml")

        body = soup.find(id="bodyContent")

        # Количество картинок (img) с шириной (width) не меньше 200
        imgs = 0
        for img in body.find_all('img', width=True):
            if int(img['width']) >= 200:
                imgs += 1
                
        # Количество заголовков, первая буква текста внутри которого: E, T или C
        headers = 0
        for header in body.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
            if header.get_text()[:1] in ('E', 'T', 'C'):
                headers += 1

        # Длина максимальной последовательности ссылок, между которыми нет других тегов
        linkslen = 15
        # Количество списков, не вложенных в другие списки
        lists = 20

        out[file] = [imgs, headers, linkslen, lists]

    return out
