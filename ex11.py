#!/usr/bin/python


Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'

print('-' * len(Belgium))              # hyphens
print(Belgium.replace(',', ':'))       # replace commas

fields = Belgium.split(',')
country_population = int(fields[1])
capital_population = int(fields[3])

print("Country population:", country_population)
print("Capital population:", capital_population)
print("Total population:", country_population + capital_population)
