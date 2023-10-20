a = input("Введите предложение на английском: ")
print("1)Длина предложения: ", len(a))
b = a.lower()
print("2)Предложение в нижнем регистре: ", b)
print("3)Кол-во гласных в введенном предложении: ", b.count('a') + b.count('e') + b.count('i') + b.count('o') + b.count('u'))
c = b.replace('ugly', 'beauty')
print("4)Измененое предложение: ", c)

if c.startswith('the') == True:
    print("5)Предложение начинается с The")
else: print("5)Предложение не начинается с The")

if c.endswith('end') == True:
    print("6)Предложение заканчивается на End")
else: print("6)Предложение не заканчивается на End")