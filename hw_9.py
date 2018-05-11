s = 'employee_first_name'
s1 = s.split('_')
first = s1[0].capitalize()
second = s1[1].capitalize()
third = s1[2].capitalize()
print('Result: %s%s%s' % (first, second, third))