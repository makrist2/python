def is_isogram(word):
    true_word = word.lower()
    for char in true_word:
        if true_word.count(char) > 1:
            return False
    return True


print(is_isogram('ms acquired g?th_b'))