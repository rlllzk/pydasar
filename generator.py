def generator(n):
    MAX=214748
    while n < MAX:
        yield n
        n+=1
g=generator(0)
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())

