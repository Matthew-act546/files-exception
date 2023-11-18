import json 

filename = "files_exception/JSON/numbers.json"
with open(filename) as f:
    numbers = json.load(f)
    

print(numbers)