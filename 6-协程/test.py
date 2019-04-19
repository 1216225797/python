def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total/count

ave = averager()
next(ave)
print(ave.send(10))
print(ave.send(20))