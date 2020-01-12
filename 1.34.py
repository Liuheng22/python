from random import randint

class Die():
    """随机生成一个10个的随机序列"""

    def __init__(self):
        self.sides = 6

    def update_sides(self,n):
        self.sides = n

    def roll_die(self):
        return [randint(1,self.sides) for i in range(10)]

while True:
    print("Enter 0 to quit!")
    x = int(input('Please enter a number:'))
    if x==0:
        break
    else:
        ans = Die()
        ans.update_sides(x)
        print(ans.roll_die())


