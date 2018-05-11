s = 'Leo Tolstoy*1828-08-28*1910-11-20'
s1 = s.split('*')
name = s1[0]
birthday = s1[1].split('-')
birthday_year = int(birthday[0])
death = s1[2].split('-')
death_year = int(death[0])
age = death_year - birthday_year
print('%s, %d' % (name, age))