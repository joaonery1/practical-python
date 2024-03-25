def portofolio_cost(filename):
  total = 0.0
  with open(filename, 'rt') as f:
      headers = next(f)
      #print(headers)
      for line in f:
          row = line.split(',')
          nshares = int(row[1])
          #print(nshares)
          price = float(row[2])
          #print(price)
          total = total + (nshares*price)
      return total

cost = portofolio_cost('Work/Data/portfolio.csv')
print('Total cost:', cost)