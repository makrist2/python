s = '05.17.2015'
s1 = s.split('.')
day = s1[1]
month = s1[0]
year = s1[2]
result = ('Euro date is: %s.%s.%s' % (day, month, year))
print(result)
