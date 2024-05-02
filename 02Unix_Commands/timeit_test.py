import timeit

def test(n):
    return sum(range(n))

# print(test(10))

result = timeit.timeit(lambda: test(100))
print(result)