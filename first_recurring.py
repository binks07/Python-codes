def recurring(f):
    a=list(f)
    b="none"
    for i in a:
        k=f.count(i)
        if k>1:
            b=i
            break
    return b



foo=input("please enter the name")
f=str(foo)
print(recurring(f))

