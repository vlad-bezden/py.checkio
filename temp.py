from collections import defaultdict

file_name = 'test.txt'
data = defaultdict(list)

with open(file_name) as f:
    for cnt, line in enumerate(f, 1):
        for word in line.strip().split():
            data[word].append(cnt)

print(data)
