car = {'brand': 'Toyota',
        'year': 2010, 
        'price': 400.45
}

car['name'] = car['brand']
del car['brand']
car = dict(sorted(list(car.items())))
print(car)