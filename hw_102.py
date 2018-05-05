import re
import os

filename = os.path.basename('C:\\Users\\makri\\Desktop\\folder\\SomeDocument1.docx')
filename1 = os.path.splitext(filename)[0]

i_hope_its_right = re.sub(r'SomeDocument1', "<A HREF=\"" + filename1 + '.docx >' + filename1 + '</A>', filename1)

print(i_hope_its_right)
