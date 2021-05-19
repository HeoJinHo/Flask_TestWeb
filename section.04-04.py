

# List : Array

list1 = ['name', 'arg', 'id']
hash1 = [
    {
        "name": "jinho",
        "arg": 31,
        "id": "hjh701"
    },
    {
        "name": "sol",
        "arg": 26,
        "id": "solma"
    }
]

masol = []

for li in hash1:
    print(li)
    li['test'] = li
    masol.append(li.get("test"))

print(masol)