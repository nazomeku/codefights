"""Implement a function that will turn the old-style string formating s into a
new one."""


import re
def newStyleFormatting(s):
    return re.sub(r'%[a-z]', '{}', s.replace('%%', 'temp')).replace('temp', '%')
