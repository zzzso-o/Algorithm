n = []
bucket = []
for _ in range(10):
    n.append(int(input()))
for i in range(10):
    bucket.append(n[i]%42)
print(len(set(bucket)))