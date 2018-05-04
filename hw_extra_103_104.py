from re import sub


def rle_encode(value):
    return sub(r'(.)\1*', lambda m: str(len(m.group(0))) + m.group(1),
               value)


def rle_decode(value):
    return sub(r'(\d+)(\D)', lambda m: m.group(2) * int(m.group(1)),
               value)


s1 = "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWB"
# s2 = "AAAAAAAAAAAAAAAAAGGGGGGGGGGGGGGGGGGGGGGGBBTTTTTTTTTTTTTTTTTTTTTTTT" ---- test

print(rle_encode(s1))
print(rle_decode(rle_encode(s1)))
