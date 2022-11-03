def pay():
    if hr > 40:
        ot = hr-40
        pay = (40*rate) + (ot*(rate*1.5))
        return pay
    else:
        pay = hr*rate
        return pay

hr = int(input("How many hours did you work last week?"))
rate = int(input("What is your pay rate per hour(between 10-25)"))
print(pay())