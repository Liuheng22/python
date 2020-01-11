n = int(input())
a = sum([1/i if i%2 == 1 else -i/i for i in range(1,n)])
print(a)
