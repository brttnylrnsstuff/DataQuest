from operator import itemgetter

crime_rates = list()
with open('crime_rates.csv', 'r') as f:
    for line in f:
        city, rate = line.rstrip().split(',')
        crime_rates.append((city, int(rate)))

print(max(crime_rates, key=itemgetter(1)))
print(min(crime_rates, key=itemgetter(1)))
