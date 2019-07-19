from collections import namedtuple
from collections import defaultdict
import functools

statistics = defaultdict(list)
Order = namedtuple('Order', ['success', 'portions'])

recipes = {
    'Бутерброд с ветчиной': {'Хлеб': 50, 'Ветчина': 20, 'Сыр': 20},
    'Салат Витаминный': {'Помидоры': 50, 'Огурцы': 20, 'Лук': 20, 'Майонез': 50, 'Зелень': 20}
}

store = {
    'Хлеб': 250, 'Ветчина': 120, 'Сыр': 120,
    'Помидоры': 50, 'Огурцы': 20, 'Лук': 20,
    'Майонез': 50, 'Зелень': 20
}

def collect_statistics(statistics):
    def decorator(func):
        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            result = func(*args, **kwargs)
            if args[0] not in statistics.keys():
                statistics[args[0]] = []
            statistics[args[0]].append( Order(result[0], result[1] if result[0] == 1 else args[1] - result[1] ) )
            return result
        return wrapped
    return decorator

@collect_statistics(statistics)
def check_portions(food, count, recipes=recipes, store=store):
    '''
    returns (sucees_or_not, number_of_cooked_portions)
    '''
    local_store = dict(store)
    count_cooked = 0

    if food in recipes.keys():
        for n in range(count):
            for ing, ing_count in recipes[food].items():
                if ing not in local_store.keys():
                    return (0, 0)
                else:
                    if ing_count <= local_store[ing]:
                        local_store[ing] -= ing_count
                    else:
                        return (0, count_cooked)
            count_cooked += 1
        if (count_cooked >= count):
            return (1, count)
    
    else:
        return (0, 0)
        
check_portions('Бутерброд с ветчиной', 20, {
    'Бутерброд с 22': {'Хлеб': 50, 'Ветчина': 20, 'Сыр': 20},
    'Салат 22': {'Помидоры': 50, 'Огурцы': 20, 'Лук': 20, 'Майонез': 50, 'Зелень': 20}
}, {
    'Хлеб': 250, 'Ветчина': 120, 'Сыр': 120,
    'Помидоры': 50, 'Огурцы': 20, 'Лук': 20,
    'Майонез': 50, 'Зелень': 20
}) 
print(len(statistics['Бутерброд с ветчиной']))
# check_portions('Салат Витаминный', 1)
# print(statistics)
# check_portions('Бутерброд с ветчиной', 2)
# print(statistics)

