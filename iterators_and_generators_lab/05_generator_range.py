def genrange(start, end):
    current = start
    while current <= end:
        yield current
        current += 1


for num in genrange():
    print(num)

print(list(genrange(1, 10)))
