fi = open('input.txt', 'r', encoding='utf-8')
fo = open('output.txt', 'w')
print('Задача 1.1.')
fi.readline()
input_fi = fi.readline().strip()
num = int(input_fi)
fo.write('Задача 1.1.:\n' 'Число:' + str(num) + '\n')
if (num >= 1 and num <= 100):
    print("Число входит в диапазон от 1 до 100.  \n")
    fo = open('output.txt', 'a')
    fo.write("Число входит в диапазон от 1 до 100. \n")
if (num >= 200 and num <= 300):
    print("Число входит в диапазон от 200 до 300.  \n")
    fo = open('output.txt', 'a')
    fo.write("Число входит в диапазон от 200 до 300. \n")
if (num <= 0) or (num > 301) or(num > 101 and num < 199):
    print("Число не входит в жоден диапазон.  \n")
    fo = open('output.txt', 'a')
    fo.write("Число не входит в жоден диапазон. \n")

print('Задача 1.2.')
with open('input.txt', 'r', encoding='utf-8') as fi:
    for i in range(3):
        fi.readline()
    t = fi.readline().strip()
    x = int(t)
y = ((100 - x) * 2)
fo = open('output.txt', 'a')
fo.write('Задача 1.2.: \nКастрюля закипит через:' + str(y) + 'мин\n')
print("Кастрюля закипит через:", y, 'мин\n')


print('Задача 1.3')
with open('input.txt', 'r', encoding='utf-8') as f:
    for line in f:
        if line.startswith('Задача 1.3:'):
            x = int(f.readline())
    for i in range(x):
        r = str(i+1) + '.000'
        print(r)
fo = open('output.txt', 'a')
fo.write('Задача 1.3.\n')
fo = open('output.txt', 'a')
fo.write(r + '\n')


print('Задача 1.4.')
fo = open('output.txt', 'a')
fo.write('Задача 1.4:\n')
with open('input.txt', 'r', encoding='utf-8') as f:
    for line in f:
        if line.startswith('Задача 1.4:'):
            h = int(f.readline())
print("Используем число: ", h)
for i in range(h):
    result = "*" * (i + 1)
    print(result)
fo = open('output.txt', 'a')
fo.write(result + "\n")

with open('output.txt', 'a') as out:
    out.write('\nЗадание 2.1:')
print('Задача 2.1')
with open('input.txt', 'r') as f:
    for i in range(9):
        f.readline()
    a = int(f.readline().strip())
    b = int(f.readline().strip())
    c = int(f.readline().strip())
    m = int(f.readline().strip())
    k = int(f.readline().strip())
with open('output.txt', 'a') as out:
    if a <= m and b <= k or a <= k and b <= m or a <= m and c <= k or a <= k and c <= m or b <= m and c <= k or b <= k and c <= m:
        result = ('Коробка войдет в дверь\n')
        out.write('\nКоробка войдет в дверь\n')
    else:
        result = ('Коробка не войдет в дверь\n')
        out.write('\nКоробка не войдет в дверь\n')
print(result)


with open('output.txt', 'a') as fo:
    fo.write('\n\nЗадание 2.2: \n')
    print('Задание 2.2:')
with open('input.txt', 'r') as fi:
    for i in range(15):
        fi.readline()
    height = int(fi.readline().strip())
with open('output.txt', 'a') as fo:
    for i in range(height):
        fo.write(' ' * (height - i - 1) + '*' * (2 * i + 1) + '\n')
        print(' ' * (height - i - 1) + '*' * (2 * i + 1))


with open('output.txt', 'a') as fo:
    fo.write('\nЗадание 2.3: \n')
    print('\nЗадание 2.3: ')
with open('input.txt', 'r') as fi:
    for i in range(17):
        fi.readline()
    n = int(fi.readline().strip())
num = 1
with open('output.txt', 'a') as fo:
    while num ** 2 < n:
        fo.write(str(num ** 2) + '\n')
        num += 1
        print(str(num ** 2))


with open('output.txt', 'a') as fo:
    fo.write('\nЗадание 3.1:\n')
    print('Задание 3.1:')
with open('input.txt', 'r') as fi:
    for i in range(19):
        fi.readline()
    k = int(fi.readline().strip())
    with open('output.txt', 'a') as fo:
        if k % 3 == 0 or k % 5 == 0 or k % 3 + k % 5 == 5:
            fo.write("Можно купить ровно " + str(k) + " шариков мороженного\n")
            print('Можно купить ' + str(k) + ' шариков мороженного\n')
        else:
            fo.write("Нельзя купить ровно " + str(k) + " шариков мороженного\n")
            print('Нельзя купить ' + str(k) + ' шариков мороженного\n')



with open('output.txt', 'a') as fo:
    fo.write('\n\nЗадание 3.2:\n')
    print('Задание 3.2:')
with open('input.txt', 'r') as fi:
    for i in range(21):
        fi.readline()
    x = int(fi.readline().strip())
    y = int(fi.readline().strip())
    z = int(fi.readline().strip())
years = 0
while x < z:
    x = x * (1 + y / 100)
    years += 1
with open('output.txt', 'a') as fo:
    fo.write("Через " + str(years) + " лет сумма вклада превысит " + str(z) + " тысяч гривен")
    print('Через ' + str(years) + ' год сумма превысит ' + str(z) + ' тысяч гривен')


with open('output.txt', 'a') as fo:
    fo.write('\n\nЗадание 3.3:')
    print('Задание 3.3:')
with open('input.txt', 'r') as fi:
    for i in range(25):
        fi.readline()
    n = int(fi.readline().strip())
sum = 0
while n > 0:
    sum += n % 10
    n //= 10
with open('output.txt', 'a') as fo:
    fo.write('\nСумма цифр числа: ' + str(sum))
    print('\nСумма цифр числа: ' + str(sum))
