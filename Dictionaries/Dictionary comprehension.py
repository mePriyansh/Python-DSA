import random

city=['London', 'Berlin', 'Paris', 'Madrid', 'Rome', 'Athens', 'Brussels']

city_temp = {city: random.randint(20, 30) for city in city}
print(city_temp)

city_high={city:temp for city,temp in city_temp.items() if temp>25}
print(city_high)