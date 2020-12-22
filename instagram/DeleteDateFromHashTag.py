filename = input('filename?')

data = ''
with open(filename, 'r') as f:
    data = f.read()

for line in data.split('\n'):
    if len(line) < 30:
        data = data.replace(line, '')
data = data.replace('\n', '')

with open('TrimmedFile.txt', 'w') as f:
    f.write(data)

        
