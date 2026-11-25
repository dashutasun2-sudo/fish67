import math
a=int(input())
b=float(input())
print(f"Сумма:  {a+b}")
print(f"Разность:  {a-b}")
print(f"Произведение:  {a*b}")
print(f"Частное:  {a/b}")
if a%b==0:
    print('тип: целочисленное')
else:
    print("тип: с остатком")
pi=3.14159
r=5
s=pi*r**2
s2=round(s,2)
print(f"Площадь круга:  {s2}")
