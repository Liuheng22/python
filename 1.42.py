import json

numbers = [x for x in range(2,14,2)]

filename = 'numbers.json'
with open(filename,'w') as f_obj:
    json.dump(numbers,f_obj)

with open(filename,'r') as f_obj:
    ans = json.load(f_obj)

print(ans)