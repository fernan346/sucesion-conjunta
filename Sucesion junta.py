def otra (n):
    a=1
    b=2
    c=1
    for i in range (n):
        if (c % 2==1):
            print(a)
            a=a+2
        else:
            print(b)
            b=b*2
        c=c+1
otra(10)