purchases = [
    {"item": "apple", "category": "fruit", "price": 1.2, "quantity": 10},
    {"item": "banana", "category": "fruit", "price": 0.5, "quantity": 5},
    {"item": "milk", "category": "dairy", "price": 1.5, "quantity": 2},
    {"item": "bread", "category": "bakery", "price": 2.0, "quantity": 3},
]


def total_revenue(purchases):
    summ = 0
    for i in purchases:
        summ += i['price'] * i['quantity']
    return summ


def items_by_category(purchases):
    new_purchases = {}

    for i in purchases:
        for key, value in i.items():
            if key == 'item':
                a = value
            if key == 'category':
                b = value
        new_purchases[a] = b

    key_list = list(set(new_purchases.values()))

    result_dict = {}
    for i in key_list:
        value_set = set()
        for k, v in new_purchases.items():
            if v == i:
                value_set.add(k)
        result_dict[i] = list(value_set)
    return result_dict


def expensive_purchases(purchases, min_price):
    new_dict = []
    for i in purchases:
        if i['price']>min_price:
            new_dict.append(i)
    return new_dict


def average_price_by_category(purchases):
    category = set()
    result_dict = {}

    for i in purchases:
        category.add(i['category'])
    category = list(category)

    for cat in category:
        summ = 0
        cnt = 0
        for i in purchases:
            if cat == i['category']:
                summ += i['price']
                cnt += 1
        result_dict[cat] = summ / cnt
    return result_dict


def most_frequent_category(purchases):
    category = set()
    result_dict = {}

    for i in purchases:
        category.add(i['category'])
    category = list(category)

    for cat in category:
        summ = 0
        cnt = 0
        for i in purchases:
            if cat == i['category']:
                summ += i['quantity']
                cnt += 1
        result_dict[cat] = summ
    m = max(result_dict.values())
    key = next(key for key, value in result_dict.items() if value == m)
    return key


print('Общая выручка:', total_revenue(purchases))
print('Товары по категориям:', items_by_category(purchases))
print('Покупки дороже 1.0:', expensive_purchases(purchases, 1.0))
print('Средняя цена по категориям:', average_price_by_category(purchases))
print('Категория с наибольшим количеством проданных товаров:', most_frequent_category(purchases))






