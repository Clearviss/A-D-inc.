import re

phonerex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
numer = 'vtygvytuctc ycui yuvuyvivuyv  323-323-3232'
o = phonerex.search(numer)
print(o.group(1))
print(o.groups())