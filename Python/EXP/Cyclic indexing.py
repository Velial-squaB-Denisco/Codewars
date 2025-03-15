keyi = 0
text = "hello"
key = "key"
newkey = list()

for a in text:
    newkey.append(key[keyi])
    keyi = (keyi + 1) % len(key)