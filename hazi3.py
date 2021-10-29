m = [[1, 1, 1, 2, 1], [2, 3, 2, 2, 2], [3, 3, 2, 3, 3], [4, 4, 4, 3, 4]]

result = 0

for i in m:
    for j in range(len(i)):
        result += i[j]

print(result)

cars = [
    {
        "price": 1549,
        "passengerQty": 4,
        "currency": "EUR",
        "type": "Kia",
        "transmission": "manual",
        "passengers": ["Gabor", "Andras", "Timea", "Martin", "Miklos"]
    },
    {
        "price": 1954,
        "passengerQty": 5,
        "currency": "EUR",
        "type": "Suzuki",
        "transmission": "manual",
        "passengers": ["Gabor", "Andras", "Timea", "Martin", "Miklos"]
    },
    {
        "price": 2544,
        "passengerQty": 5,
        "currency": "USD",
        "type": "Opel",
        "transmission": "manual",
        "passengers": ["Gabor", "Andras", "Timea", "Martin", "Miklos"]
    },
    {
        "price": 2544,
        "passengerQty": 2,
        "currency": "USD",
        "type": "Opel",
        "transmission": "manual",
        "passengers": ["Gabor", "Timea", "Miklos"]
    },
    {
        "price": 9542,
        "passengerQty": 4,
        "currency": "USD",
        "type": "Ford",
        "transmission": "automatic",
        "passengers": ["Gabor", "Timea", "Miklos"]
    },
]

for c in cars:
    if c["passengerQty"] < len(c["passengers"]):
        print(f'a(z) {c["type"]} típusú autóban túl sok az utas')

for p in cars:
    p["currency"] = "EUR"
    p["price"] = round(p["price"] * 0.87)
    print(f'a(z) {p["type"]} ára {p["price"]} {p["currency"]}')

persons = ["John", "Marissa", "Pete", "Dayton"]
restaurants = ["Japanese", "American", "Mexican", "French"]

for person in persons:
    for restaurant in restaurants:
        print(person + " eats " + restaurant)

my_list = [[4, 5], [7, 4], [2, 5], [9, 4]]

for l in my_list:
    number = 0
    for t, k in enumerate(range(len(l))):
        number += l[k]
        if t == 1:
            l.append(number)

print(my_list)