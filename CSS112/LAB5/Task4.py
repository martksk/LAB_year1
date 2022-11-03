def temp(start,end): 
    if (start <= end ): 
        res = (start*9/5)+32
        x.write(f'{start} degrees Celsius is {res:.2f} degrees Fahrenheit\n')
        temp(start+1,end)
    

start = int(input("Enter a beginning Celcius value: "))
end = int(input("Enter an ending Celcius value: "))
x = open("multiply.txt", 'w') 
temp(start,end)
