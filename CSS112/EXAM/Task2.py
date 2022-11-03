from unittest import result


def plangnuay(*som):
    inch = som[0]/2.54
    pon = som[1]*2.2
    return inch,pon

n = 2
k = 2
while n>1:    
    print("Select an operation.\n\n1.Convert Centimeter into Inch\n2.Convert Kilogram into Pound\n3.Convert Celcius into Farenheit\n4.Convert Litre into US Gallon\n")
    while k > 1:
        chc = int(input("Enter choice(1/2/3/4): "))
        if chc > 4 or chc < 1:
            print("Invaid Input")
            continue
        else:
            if chc == 1:
                di = float(input("Enter dimension in Centimeter: "))
                res= plangnuay(di,0)[0]
                print(f"The {di} Centimeter(s) equal to {res:.2f} inch(es).")
                nex = str(input("Let's do next calculation? (y/n): "))
            if chc == 2:
                w = float(input("Enter weight in Kilogram: "))
                res= plangnuay(0,w)[1]
                print(f"The {w:.1f} Kilogram(s) equal to {res:.2f} Pound(s).")
                nex = str(input("Let's do next calculation? (y/n): "))
            # if chc == 1:
            #     di = float(input("Enter dimension in Centimeter: "))
            #     res= plangnuay(di)
            #     print(f"The {di} Centimeter(s) equal to {res:.2f} inch(es).")
            #     nex = str(input("Let's do next calculation? (y/n): "))
            # if chc == 1:
            #     di = float(input("Enter dimension in Centimeter: "))
            #     res= plangnuay(di)
            #     print(f"The {di} Centimeter(s) equal to {res:.2f} inch(es).")
            #     nex = str(input("Let's do next calculation? (y/n): "))
                
            break
    if nex == "y":
        continue
    else:
        break
