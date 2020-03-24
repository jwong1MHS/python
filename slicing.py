def split_name(s):
    space = s.find(' ')
    return s[:space] + '\n' + s[space+1:]
print(split_name("John Shaft"))

def bondify(s):
    space = s.find(' ')
    return s[space+1:] + '... ' + s
print(bondify("Mr DW"))


def find_last(s, key):
    spot = s[::-1].find(key)
    if spot < 0:
        return spot
    return (len(s)-1) - spot

print(find_last('hello', 'l'))
print(find_last('hello', 'h'))
print(find_last('hello', 'z'))


def replace(s, key, replacement):
    key_start = s.find(key)
    key_end = key_start + len(key)
    if key_start < 0:
        return s
    return s[:key_start] + replacement + s[key_end:]

print(replace("I hate cs!", "hate", "love"))
