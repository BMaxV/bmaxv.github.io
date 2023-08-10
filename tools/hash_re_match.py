import re

def check(s):
    pat = re.compile("[0-9a-fA-F]{64}")
    r = pat.match(s)
    # if it finds something it contains the symbols
    # and its the correct length
    return not (r==None)

