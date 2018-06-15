def is_isogram(word):
    true_word = word.lower()
    if len(word.replace(' ', '')) == len(set(true_word.replace(' ', ''))):
        return True
    else:
        return False


print(is_isogram('ms acquired g?th_b'))
print(is_isogram('wheel'))
print(is_isogram('machine'))