a = [3, 4, 5, 10, 6, 1, 8, 2, 7, 9]

result = []
for _ in range(len(a)):
    m = min(a)
    inm = a.index(m)
    x = a.pop(inm)
    result.append(x)
print(result)





