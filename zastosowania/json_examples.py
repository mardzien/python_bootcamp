import json

text = '''{
"ala": "kot",
"x": [1, 2, 3]
}'''

print(type(text))
obiekt = json.loads(text)
print(obiekt)
print(type(obiekt))

python_obj = [1, 2, 3, 4, 'a', 'b']
json_obj = json.dumps(python_obj)

print(python_obj)
print(json_obj)
print(type(json_obj))

with open("dane.json") as fp:
    dane = json.load(fp)
    print(dane)


with open('dane2.json', 'w') as f:
    json.dump(python_obj, f)

with open('dane2.json') as f:
    dane = json.load(f) # deserializacja
    dane.append(123)

with open('dane2.json', 'w') as f:
    json.dump(dane, f)