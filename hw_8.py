name = input('Input your name (ex. Mark Zuckerberg)\n')
s = name.split(' ')
f_name = s[0]
l_name = s[1]
result = 'Actual name is %s %s' % (l_name, f_name)
print(result)