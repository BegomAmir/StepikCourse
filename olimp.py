filePuff = input()
try:
    with open(filePuff, 'r') as file:
        content = file.read()
        count = 0
        tmp = '1'
        for word in content:
            if word == ' ' or word == '\n':
                if tmp != ' ' and tmp != '\n':
                    count += 1
            tmp = word
        count += 1
        print(count)
except IOError:
    print("Error: File not found or could not be opened.")


