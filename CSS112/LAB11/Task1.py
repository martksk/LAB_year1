def gen5odds():
    return ([i+j for j in range(10) if j%2] for i in range(0,100,10))

def Problem1(): 
    x=[]
    for i in gen5odds():
        x.append(sum(i))
    return x