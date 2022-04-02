word = input().upper()
unique_words = list(set(word))

bucket = []
for i in unique_words:
    bucket.append(word.count(i))

if bucket.count(max(bucket)) > 1:
    print('?')
else:
    max_index = bucket.index(max(bucket))
    print(unique_words[max_index])
