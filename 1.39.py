filename='pi_digits.txt'

with open(filename,'a')as file_object:
    file_object.write("\nI love programming.")
with open(filename) as file_object:
    contents = file_object.read()

print(contents)