print('Задание 1')
a = int (input ("Введите число: "))
b = int (input ( "Введите число: "))
q = input ('Введите операцию: ')
if q == '+':
    print(a+b)
elif q == '-':
    print(a-b)
elif q == '/':
    print(a/b)
elif q == '*':
    print(a*b)
elif q == 'mod':
    print(a%b)
elif q == 'pow':
    print(a**b)
elif q == 'div':
    print(a//b)
else:
    print('Неверно набранная операция')

print(' ')

print('Задание 2')
a = int (input ("Введите число: "))
b = int (input ( "Введите число: "))
if a%b == 0:
    print('число '+str(a)+ ' делится на ' +str(b)+ ' нацело')
else:
    print('число '+str(a)+ ' не делится на ' +str(b)+ ' нацело')

if b%a == 0:
    print('число '+str(b)+ ' делится на ' +str(a)+ ' нацело')
else:
    print('число '+str(b)+ ' не делится на ' +str(a)+ ' нацело')

print(' ')


print('Задание 3')
a = int (input ("Введите число: "))

h=a//100
print(h)
d=(a-h*100)//10
print(d)
e=a-h*100-d*10
print(e)

if (h==d) or (h==e) or (e==d):
    print('В числе есть одинаковіе ціфрі')
else:
    print('Нет одинаковіх цифр')
