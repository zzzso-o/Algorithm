moeum = ['a', 'e', 'i', 'o', 'u']

while True:
    text = input()
    if text == 'end':
        break
    for i in range(len(text)):
        if text[i] in moeum:
            continue
        if i+2 < len(text):
            if text[i] == text[i+1] == text[i+2]:

