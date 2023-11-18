import json

numbers = [2, 5, 6, 3, 9, 7, 10, 8]

filename = "files_exception/JSON/numbers.json"
with open(filename, 'w') as f:
    json.dump(numbers, f)
