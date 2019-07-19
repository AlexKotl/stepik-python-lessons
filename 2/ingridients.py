recipes = {
    'Бутерброд с ветчиной': {'Хлеб': 50, 'Ветчина': 20, 'Сыр': 20},
    'Салат Витаминный': {'Помидоры': 50, 'Огурцы': 20, 'Лук': 20, 'Майонез': 50, 'Зелень': 20}
}

store = {
    'Хлеб': 250, 'Ветчина': 120, 'Сыр': 120,
    'Помидоры': 50, 'Огурцы': 20, 'Лук': 20,
    'Майонез': 50, 'Зелень': 20
}

def check_portions(food, count, recipes=recipes, store=store):
    local_store = dict(store)
    count_cooked = 0

    if food in recipes:
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

#print(check_portions('Бутерброд с ветчиной', 2))
#print(check_portions('Бутерброд с ветчиной', 10))