import re
import os

filename = os.path.basename('C:\\Users\\makri\\Desktop\\folder\\SomeDocument1.docx')
filename_without_docx = os.path.splitext(filename)[0]
filename_full = os.path.basename(filename)

i_hope_its_right = re.sub(r'SomeDocument1', "<A HREF=\"" + filename_without_docx + '.docx >' + filename_full + '</A>', filename_without_docx)

print(i_hope_its_right)