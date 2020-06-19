def pat1(n, ty):
    if ty=='des':
        if n > 0:
            print(n, end="")
            pat1(n-1, ty)
    elif ty=='aes':
        a=1
        pattern1(a, n)


def pattern1(i, n):
    if i<=n:
        print(i, end="")
        i=i+1
        # print("i after increment : ", i)
        pattern1(i, n)
