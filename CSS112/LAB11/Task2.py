def Problem2():
    return  [sum(k) for k in ([i+j for j in range(10) if j%2] for i in range(0,100,10))]