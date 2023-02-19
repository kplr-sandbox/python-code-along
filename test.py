import unicodedata
a='é'
def strip_accents(text):
    # Just a prefrence change
    text = unicodedata.normalize('NFD', text)
    text = text.encode('ascii', 'ignore')
    return text.decode("utf-8")
print(strip_accents(a))
# print(unicodedata.normalize('NFD',a).decode('utf-8'))
