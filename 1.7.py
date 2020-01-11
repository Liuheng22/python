x = int(input())
n = 0;
while True:
    if x%2==0:
        x/=2
    else:
        if x==1:
            break
        else:
            x = (3*x+1)/2
    n+=1
print(n)
