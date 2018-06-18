import string


def encode(str_to_encode):
    encrypted = ''
    shift = 5
    enc_table = string.ascii_lowercase + string.digits
    str_split = str_to_encode.split(' ')
    enc_table_len = len(enc_table)
    len_str_split = len(str_split)
    for word in str_split:
        length_word = len(word)
        for i in range(length_word):
            if enc_table.find(word[i]) != -1:
                enc_ind = enc_table.find(word[i])
                encrypted += enc_table[(enc_ind + shift) % enc_table_len]
            else:
                encrypted += word[i]
        if len_str_split > 1:
                encrypted += ' '
                len_str_split -= 1
    return encrypted


str1 = input('Plz input str')
print(encode(str1))