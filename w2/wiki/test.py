# скрипт для проверки решений студентов по Практическому заданию по Beautiful Soup
# https://stepik.org/lesson/106955/step/1?unit=81478
#
# запуск тестов
# $ python3 test.py
#
# система оценивания - двухэтапная: на первом этапе проверяются правильность сбора
# статистики со страниц (проверяется только на начальной и на конечной), при успешном
# прохождении тестов - решение считается засчитанным с начислением 0.5 баллов,
# далее тестируется правильность нахождения минимального пути, и соответсвие статистики
# контрольным данным, за прохождение тестов добавляются баллы (максимально возможное
# количество - 0.5)

from wikistat import parse
import os

# путь до директории с файлами
PATH = 'wiki/'
path = os.path.normpath(PATH)


def grade(path):
    # количество пройденных тестов, необходимо для вычисления баллов
    successful_tests = 0
    # лог сообщений об падениях тестов
    fail_log = []
    # =======================================================================================
    # набор тестов - пример из описания
    # =======================================================================================
    # контрольные данные для примера из описания
    correct = {
        "Stone_Age": [13, 10, 12, 40],
        "Brain": [19, 5, 25, 11],
        "Artificial_intelligence": [8, 19, 13, 198],
        "Python_(programming_language)": [2, 5, 17, 41]
    }
    # список наборов параметров для parse
    params = (
        # начальная и конечная страницы совпадают
        ("Stone_Age", "Stone_Age", path),
        # пример из описания
        ("Stone_Age", "Python_(programming_language)", path),
    )
    # =======================================================================================
    # Тест 1. вызов parse не выбрасывает исключений
    # =======================================================================================
    try:
        for start, end, path in params:
            result = parse(start, end, path)
    except Exception as err:
        message = (
            f'Тест 1. Вызов функции parse({start}, {end}, {path}) выбрасывает '
            f'исключение {err.__class__.__name__}.'
        )
        return [0, message]

    # =======================================================================================
    # Тест 2.  функция parse возвращает словарь, ключ строка, значение список
    # =======================================================================================
    message = (
        'Тест 2. Вызов функции parse("Stone_Age","Python_(programming_language)",'
        '"wiki") возвращает результат не соответствующий спецификации. '
        'Проверьте типы возвращаемых значений.'
    )
    if not isinstance(result, dict):
        return [0, message]

    for key, value in result.items():
        if not isinstance(key, str) or not isinstance(value, list) or \
                not all(map(lambda x: isinstance(x, int), value)):
            return [0, message]

    # =======================================================================================
    # Тест 3. начальная и конечная страницы содержатся в выводе функции parse
    # =======================================================================================
    for page_name in ('Stone_Age', 'Python_(programming_language)'):
        if page_name not in result.keys():
            print(page_name)
            message = (f'Тест 3.Вызов функции parse("Stone_Age","Python_(programming_'
                       f'language)","wiki"). В выводе отсутствует страница {page_name}.')
            return [0, message]

    # =======================================================================================
    # **** Тест 8. функция parse возвращает правильный путь *******
    #             тест из второго этапа проверок
    # =======================================================================================
    if set(result.keys()) != set(correct.keys()):
        message = (
            f'Тест 8. Вызов функции parse("Stone_Age","Python_(programming_language)",'
            f'"wiki_local/") не правильно вычисляет кратчайший путь. Ваш вывод: '
            f'{list(result)}. Ожидалось {list(correct)}')
        fail_log.append(message)

    successful_tests += 1
    # =======================================================================================
    # Тест 4. функция parse возвращает правильную статистику (пример из описания),
    # проверяем только начальную и конечную страницы (минимум для прохождения теста)
    # =======================================================================================
    # Тест 4.
    for page_name in ('Stone_Age', 'Python_(programming_language)'):
        if result[page_name] != correct[page_name]:
            message = (
                f'Тест 4.Вызов функции parse("Stone_Age","Python_(programming_language)",'
                f'"wiki_local/") не правильно вычисляет статистику для {page_name}. '
                f"Ваш вывод: {result[page_name]}")
            return [0, message]

    # =======================================================================================
    # ***** Тест 9. функция parse возвращает правильную статистику ******
    #             тест из второго этапа проверок
    # =======================================================================================

    for page_name in ("Stone_Age", "Python_(programming_language)",
                      'Artificial_intelligence', 'Brain'):

        # Тест 9.0. проверим правильность минимального пути
        if page_name not in result:
            message = (f'Тест 9.0.Вызов функции parse("Stone_Age","Python_(programming_'
                       f'language)","wiki"). В выводе отсутствует страница {page_name}.')
            fail_log.append(message)
            break

        # Тест 9.1. проверим правильность возвращаемой статистики
        if result[page_name] != correct[page_name]:
            message = (
                f'Тест 9.1. Вызов функции parse("Stone_Age","Python_(programming_language)",'
                f'"wiki_local/") не правильно вычисляет статистику для {page_name}. '
                f"Ваш вывод: {result[page_name]}")
            fail_log.append(message)
            break

    successful_tests += 1

    # =======================================================================================
    # Тесты на данных из описания
    # =======================================================================================
    # test_5, проверка - начальная и конечная страницы совпадают, 4 случайных страниц
    # (на данных из описания), 2 страницы содержащие ссылку только на себя и 2 страницы
    # содержащие ссылки на другие страницы
    # =======================================================================================
    correct = {"Fiber_disk_laser": [1, 2, 5, 4],
               "Time_evolution": [0, 1, 8, 4],
               "Echinoderm": [9, 6, 13, 36],
               "Spectrogram": [1, 2, 5, 7]}

    for page_name in correct:
        # Тест 5.0. вызов функции parse вызывает исключение
        try:
            result = parse(page_name, page_name, path)
        except Exception as err:
            message = (
                f'Тест 5.0. Вызов функции parse({page_name}, {page_name}, {path}) '
                f'выбрасывает исключение {err.__class__.__name__}.')
            return [0, message]

        # Тест 5.1. проверим, что возвращается словарь с одним значением
        if list(result) != [page_name, ]:
            message = (
                f'Тест 5.1. Вызов функции parse({page_name},{page_name},{path}") '
                f'возвращает не верный путь. Ваш вывод: {result.keys()}.')
            return [0, message]

        # Тест 5.2. проверим правильность возвращаемой статистики
        for page, statistic in result.items():
            if statistic != correct[page]:
                message = (
                    f'Тест 5.2. Вызов функции parse({page_name},{page_name},{path}) '
                    f'возвращает не верный результат {statistic}.Ожидалось '
                    f'{correct[page]}.')
                return [0, message]

    # =======================================================================================
    # test_6, проверка - прямой переход (ссылка на конечную страницу находится на
    # начальной странице)
    # =======================================================================================
    params = [
        ("Theory", "Sociology"),
        ("Deuterostomia", "Rouphozoa"),
        ("John_Lucas_(philosopher)", "Greats"),
        ("Vitamin", "Selenium")
    ]

    data_statistics = {
        "Theory": [0, 5, 58, 12],
        "Sociology": [5, 15, 19, 36],
        "Deuterostomia": [5, 4, 8, 37],
        "Rouphozoa": [1, 3, 8, 34],
        "John_Lucas_(philosopher)": [0, 3, 10, 11],
        "Greats": [0, 2, 11, 11],
        "Vitamin": [3, 4, 15, 33],
        "Selenium": [5, 8, 11, 49]
    }

    for start, end in params:
        # Тест 6.0. вызов функции parse вызывает исключение
        try:
            result = parse(start, end, path)
        except Exception as err:
            message = (
                f'Тест 6.0. Вызов функции parse({start}, {end}, {path}) выбрасывает '
                f'исключение {err.__class__.__name__}.')
            return [0, message]

        # Тест 6.1. проверяем правильность минимального пути
        if set(result.keys()) != {start, end}:
            message = (
                f'Тест 6.1. Вызов функции parse({start},{end},{path}) '
                f'возвращает не верный путь - {result.keys()}.')
            return [0, message]

        # Тест 6.2. проверим правильность возвращаемой статистики
        for page, statistic in result.items():
            if statistic != data_statistics[page]:
                message = (f'Тест 6.2. Вызов функции parse({start},{end},{path}) '
                           f'возвращает не верный результат {statistic}. Ожидалось '
                           f'{data_statistics[page]}.')
                return [0, message]

    # =======================================================================================
    # test_7, проверка - максимальное количество переходов, 2 случайных
    # страницы (на данных из описания), проверяем только начальную и конечную страницы
    # =======================================================================================
    data_paths = {
        "Agnostic": [
            "Haifa_bus_16_suicide_bombing",
            "Second_Intifada",
            "The_New_York_Times",
            "University_of_Chicago",
            "Illinois",
            "Binyamina_train_station_suicide_bombing"],

        "2017_Serbian_protests": [
            "Bioengineering",
            "Mathematical_and_theoretical_biology",
            "Artificial_intelligence",
            "John_von_Neumann",
            "Laser",
            "Israel_Defense_Forces",
            "Second_Intifada",
            "Bioprocess_engineering"]
    }
    data_statistics = {'Binyamina_train_station_suicide_bombing': [1, 3, 6, 21],
                       'Haifa_bus_16_suicide_bombing': [1, 4, 15, 23],
                       'Second_Intifada': [9, 13, 14, 84],
                       'The_New_York_Times': [5, 9, 8, 42],
                       'University_of_Chicago': [20, 5, 32, 36],
                       'Illinois': [32, 18, 21, 72],
                       'Agnostic': [3, 9, 6, 72],
                       'Bioprocess_engineering': [1, 1, 11, 5],
                       'Bioengineering': [1, 2, 19, 21],
                       'Mathematical_and_theoretical_biology': [1, 5, 16, 18],
                       'Artificial_intelligence': [8, 19, 13, 198],
                       'John_von_Neumann': [9, 9, 24, 60],
                       'Laser': [19, 11, 14, 27],
                       'Israel_Defense_Forces': [49, 11, 26, 70],
                       '2017_Serbian_protests': [2, 2, 7, 23]

                       }

    for start in data_paths:
        # начальная страница ключ в словаре, конечная страница - последний элемент значения
        end = data_paths[start][-1]
        # вызов функции parse вызывает исключение
        try:
            result = parse(start, end, path)
        except Exception as err:
            message = (f'Тест 7.0. Вызов функции parse({start}, {end}, {path}) '
                       f'выбрасывает исключение {err.__class__.__name__}.')
            return [0, message]

        # Тест 7.1. проверим, что как минимум start и end есть в результатах
        for page_name in (start, end):
            message = (f'Тест 7.1. Вызов функции parse({start},{end},{path}. В выводе '
                       f'отсутствует страница {page_name}. Ваш вывод: {result.keys()}.')
            if page_name not in result.keys():
                return [0, message]

        # Тест 7.2. проверим правильность возвращаемой статистики для start и end
        for page_name in (start, end):
            if result[page_name] != data_statistics[page_name]:
                message = (
                    f'Тест 7.2. Вызов функции parse({start},{end},{path})возвращает не '
                    f'верный результат {result[page_name]}.Ожидалось '
                    f'{data_statistics[page_name]}.')
                return [0, message]

        # ============================================================================
        # *****  следующие два теста - второй этап ******
        # ============================================================================
        # Тест 10. проверим правильность возвращаемого минимального пути
        if set(result.keys()) != set(data_paths[start] + [start, ]):
            message = (
                f'Тест 10. Вызов функции parse({start},{end},{path}) '
                f'не правильно вычисляет кратчайший путь. Ваш вывод: '
                f'{list(result)}. Ожидалось {list(data_paths[start] + [start, ])}')
            fail_log.append(message)
        successful_tests += 1

        # Тест 11. проверим правильность возвращаемой статистики для всех страниц
        for page_name in result.keys():
            if result[page_name] != data_statistics[page_name]:
                message = (
                    f'Тест 11. Вызов функции parse({start},{end},{path}) '
                    f'не правильно вычисляет статистику для {page_name}. '
                    f"Ваш вывод: {result[page_name]}. "
                    f"Ожидалось: {data_statistics[page_name]}.")
                fail_log.append(message)
                break
            successful_tests += 1

    # =======================================================================================
    # обработка результатов теста
    # =======================================================================================
    if fail_log:
        message = ('Вы набрали необходимое для прохождения задания количество баллов. '
                   'Некоторые из тестов были провалены - ')
        return [0.5 + 0.025 * successful_tests, message + fail_log[0]]

    return [1, 'Отличная работа!']
    # =======================================================================================


if __name__ == '__main__':
    print(grade(path))
