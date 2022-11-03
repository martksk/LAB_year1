def checkname():
    fname = {"Jeff","Jack","Jim"}
    if namecap in fname:
            checkname = ("Hello, "+namecap+". Good morning my friend!")
            return checkname
    else :
            checkname = ("Who are you?\nNice to meet you anyway..."+namecap+" :).")
            return checkname

name = str(input("What is your name?:"))
namecap = name.capitalize()
print(checkname())