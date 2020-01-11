def main():
    pinyin = ['ling','yi','er','san','si','wu','liu','qi','ba','jiu']
    num = input()
    sum = 0
    for x in num:
        sum+=int(x)
    sum = list(str(sum))
    for x in range(0,len(sum)):
        if x!=len(sum)-1:
            print(pinyin[int(sum[x])],end=' ')
        else:
            print(pinyin[int(sum[x])])

if  __name__ == "__main__":
    main()
