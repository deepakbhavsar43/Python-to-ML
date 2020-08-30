def memoize(func):
    cache = {}

    def wrapper(*args):
        if args not in cache:
            print(f"Caching NEW value for {func.__name__}{args}")
            cache[args]=func(*args)
        else:
            print(f"Using OLD value for {func.__name__}{args}")
        return cache[args]
    # print(cache)
    return wrapper

@memoize
def add(x, y):
    print("Running add!")
    return x+y

@memoize
def sub(x, y):
    print("Running sub!")
    return x-y

print(add(1, 2))
print(sub(1, 2))
print(add(1, 2))
print(sub(1, 2))
print(add(2, 2))
print(sub(4, 2))