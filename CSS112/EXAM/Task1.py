dog_age = int(input("ใส่อายุสุนัขของท่าน (เป็นจำนวนปีถ้วนๆ): "))
if dog_age > 2:
    ndog_age = dog_age - 2
    human_age = (ndog_age*4) + 22
else:
    human_age = dog_age * 11
print(f"อายุของสุนัขของท่านเทียบเท่ากับมนุษย์อายุ {human_age} ปี")