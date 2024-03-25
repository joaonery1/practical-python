total = 0.0
with open('Work/Data/portfolio.csv', 'rt') as f:
    headers = next(f)
    print(headers)
    for line in f:
        row = line.split(',')
        nshares = int(row[1])
        print(nshares)
        price = float(row[2])
        print(price)
        total = total + (nshares*price)

print(total)

