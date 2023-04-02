import math
from geopy.distance import geodesic

cd = (
    "Odessa", "1 200 000",  (30.716399437514013, 46.48625848852711),
    "Kiyv", "4 000 000", (30.51489320418375,50.44588846103565),
    )
city, population, coordinates = cd[0:3]

# функция расчета расстояния
def distance(city_1,city_2):
        # Перевод координат в радиан
        lat_1 = city_1[0] * math.pi/180 
        lon_1 = city_1[1] * math.pi/180
        lat_2 = city_2[0] * math.pi/180
        lon_2 = city_2[1] * math.pi/180
        # по формуле Гаверсинуса
        result_dist = 2 * 6371 * math.asin(math.sqrt(math.sin((lat_2 - lat_1)/2)**2 + \
                                                     math.cos(lat_1) * math.cos(lat_2) * math.sin((lon_2 - lon_1)/2)**2))
        return result_dist


print(f"Используя собственную функцию и формулу Гаверсинуса: {distance(list(cd[2]), list(cd[5])):.2f} километров")

point1 = list(cd[2])
point2 = list(cd[5])
result_dist2 = geodesic(point1, point2).km

print(f"Используя спецификацию языка:  {result_dist2:.2f} километров")