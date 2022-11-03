def checkk():
    try: 
        x = open('myFile.txt','r')
    except:
        return 'Unable to open file myFile.txt'
    else:
        res = x.read()
        return f'{res} \nSuccessfully print content in myFile.txt'
    x.close()


print(checkk())