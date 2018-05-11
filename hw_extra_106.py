s = 'john@google.com'
s1 = s.split('@')[1:]
s2 = s1[0].split('.')[0]
print(s2)