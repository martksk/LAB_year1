x  = open('myFile.txt', 'r')

def numalp():
    data = len(x.read())
    return f'Total letters are {data}'


print(numalp())