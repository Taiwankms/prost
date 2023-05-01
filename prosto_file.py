def prosto_func(num, step):
    result = num ** step
    return result


prosto_spisok22 = [2, 4, 5, 8, 2, 9, 22, 33, 43]
prosto_spisok23 = [2, 4, 5, 8, 2, 9, 22, 33, 43]


for i in prosto_spisok22:
    for j in prosto_spisok23:
        result2 = prosto_func(num=i, step=j)
        print(result2)
