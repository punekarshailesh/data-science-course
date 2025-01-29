import json

# Given JSON array of objects
data = [
    {"name": "Alice", "age": 22},
    {"name": "Bob", "age": 37},
    {"name": "Charlie", "age": 18},
    {"name": "David", "age": 73},
    {"name": "Emma", "age": 57},
    {"name": "Frank", "age": 30},
    {"name": "Grace", "age": 32},
    {"name": "Henry", "age": 10},
    {"name": "Ivy", "age": 50},
    {"name": "Jack", "age": 68},
    {"name": "Karen", "age": 7},
    {"name": "Liam", "age": 18},
    {"name": "Mary", "age": 73},
    {"name": "Nora", "age": 13},
    {"name": "Oscar", "age": 42},
    {"name": "Paul", "age": 13}
]

# Sort the data first by age, then by name
sorted_data = sorted(data, key=lambda x: (x['age'], x['name']))

# Print the sorted JSON
print(json.dumps(sorted_data, separators=(',', ':')))
