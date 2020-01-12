
x = int(input('please enter a number:'))
y = int(input('please enter a number:'))

try:
    answer = x/y
except ZeroDivisionError:
    print("you can't divide by zero!")
else:
    print(answer)