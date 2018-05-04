import re

li = ['0x012345', '0xa1b2c3', '0xdeadbeef', '0x0x0x0x', '0xabcdefg', '0xabcdefg']  # list of strings
for val in li:
        if re.match('0[xX][0-9a-fA-F]+$', val):
            print('yes')
        else:
           print('no')
