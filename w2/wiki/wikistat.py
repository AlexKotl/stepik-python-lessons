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
    """
    finds a shortest path in undirected `graph` between `start` and `goal`. 
    If no path is found, returns `None`
    """
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
    return None  # no path found. not strictly needed
    
# Вспомогательная функция, её наличие не обязательно и не будет проверяться
def build_bridge(start, end, path):
    files = build_tree(start, end, path)
    bridge = bfs2(files, start, end) or []
    
    return bridge

def parse(start, end, path):
    """
    Если не получается найти список страниц bridge, через ссылки на которых можно
    добраться от start до end, то по крайней мере, известны сами start и end, и можно
    распарсить только их. Оценка за тест, в этом случае, будет сильно снижена, но на
    минимальный проходной балл наберется, и тест будет пройден. Чтобы получить
    максимальный балл, придется искать все страницы. Удачи!
    """

    # Искать список страниц можно как угодно, даже так:
    # bridge = [start,] if start == end else [start, end]
    bridge = build_bridge(start, end, path)
    # Когда есть список страниц, из них нужно вытащить данные и вернуть их
    out = {}
    for file in bridge:
        with open(os.path.join(path, file)) as data:
            soup = BeautifulSoup(data, "lxml")

        body = soup.find(id="bodyContent")

        # TODO посчитать реальные значения
        # Количество картинок (img) с шириной (width) не меньше 200
        imgs = 5
        # Количество заголовков, первая буква текста внутри которого: E, T или C
        headers = 10
        # Длина максимальной последовательности ссылок, между которыми нет других тегов
        linkslen = 15
        # Количество списков, не вложенных в другие списки
        lists = 20

        out[file] = [imgs, headers, linkslen, lists]

    return out
