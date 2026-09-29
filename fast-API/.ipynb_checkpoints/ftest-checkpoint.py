dic = {
    "P002": {"name":"asad", "age":24, "grade": 'A', "city":"lahore", "weight": 54}
}

d = {"name":"asad", "age":24, "grade": 'A', "city":"lahore", "weight": 54}


dic2 = {
    "city": "chitral", "weight": 56
}

for key , value in dic2.items():
    d[key] = value

print(d)