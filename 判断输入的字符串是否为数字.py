'''
s = input('please input a string:')
print(s.isdigit())
'''
import re
s = input('please input a string:')
def is_num(s):
    a = re.compile(r'^[-+]?[-0-9]\d*\.\d*|[-+]?\.?[0-9]\d*$')
    result = a.match(s)
    if result:
        return True
    else:
        return False

print(is_num(s))
