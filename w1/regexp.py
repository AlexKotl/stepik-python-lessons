def calculate(data, findall):
    matches = findall(r"([abc])([\-\+])?=([abc])?([\-\+]?\d*)?")  # Если придумать хорошую регулярку, будет просто
    print(matches)
    for v1, s, v2, n in matches:  # Если кортеж такой структуры: var1, [sign]=, [var2], [[+-]number]
        # Если бы могло быть только =, вообще одной строкой все считалось бы, вот так:
        if s == '':
            data[v1] = data.get(v2, 0) + int(n or 0)
        else:
            data[v1] += (-1 if s == '-' else 1) * (data.get(v2, 0) + int(n or 0))

    return data
