x = open('myFile.txt', 'r')

def main():
    data = x.read()

    k = data.split()

    return f'Total words are {len(k)}'

print(main())