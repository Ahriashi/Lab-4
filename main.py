def BubbleSort(A): #Сортировка от меньшего к большему
    j = len(A) - 1
    flag = True
    while flag:  # Цикл
        flag = False
        for i in range(0, j):
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
                flag = True
        j -= 1

while True:
    while True:  # обработка ошибки ввода
        try:
            n = int(input("Введите количество сотрудников в компании или введите 0 чтобы закончить: ")) #Ввод данных пользователем
            break
        except ValueError:
            print("Вы ввели некорректное значение, введите цифру")
    if n == 0:  # если пользователь хочет закончить (выход из цикла)
        break
    while True:  # обработка ошибки ввода
        try:
            people = list(map(int, input("Введите расстояние в километрах, используя пробел: ").split()))  # Заполняем список расстояний
            break
        except ValueError:
            print("Введите цифры, через пробел")
    while True:  # обработка ошибки ввода
        try:
            taxi = list(map(int, input("Введите тарифы за проезд одного километра, используя пробел: ").split())) #Заполняем список тарифов
            break
        except ValueError:
            print("Введите тарифы цифрами, через пробел")
    for i in range(n):#Заполняем массивы
        people[i] = (people[i], i + 1)
    for i in range(n):
        taxi[i] = (-taxi[i], i + 1)  # Отрицательные значения чисел т.к. нам надо от наибольшего к наименьшему
    BubbleSort(people)  # Сортировка людей по от наименьшего расстояния к наибольшему
    BubbleSort(taxi)  # Сортировка цены от наибольшего к наименьшему
    ans = [0] * (n + 1)  # Создаёт список из n+1 элементов
    for i in range(n):  # Заполняем его
        ans[people[i][1]] = taxi[i][1]  # Соотношение наименьшего числа с наибольшим
    for i in range(1, n + 1):  # Выводим на экран до конечного элемета n+1
        print(i, "работнику надо поехать на такси номер", ans[i])
    num = int(0)
    for i in range(len(people)):
        num += (people[i][0] * -taxi[i][0])

    # Код из второй лабораторной работы
    W1a = ["один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
    W1b = ["одна", "две", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
    W2 = ["одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"]
    W3 = ["десять", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]
    W4 = ["сто", "двести", "триста", "четыреста", "пятьсот", "шестьсот", "семьсот", "восемьсот", "девятьсот"]
    W5 = ["тысяча", "тысячи", "тысяч"]
    W6 = ["рубль", "рубля", "рублей"]
    num1 = num // 100000
    num2 = (num // 10000) % 10
    num3 = (num // 1000) % 10
    num4 = (num // 100) % 10
    num5 = (num // 10) % 10
    num6 = num % 10
    poz = ""
    if num1 != 0:
        i1 = num1 - 1
        poz += W4[i1] + " "
    if num2 == 1 and num3 == 0:
        poz += W3[0] + " "
    if num2 != 1:
        if num2 != 0:
            i2 = num2 - 1
            poz += W3[i2] + " "
    if num3 != 0:
        if num2 == 1:
            i3 = num3 - 1
            poz += W2[i3] + " " + W5[2] + " "
        else:
            i3 = num3 - 1
            poz += W1b[i3] + " "
            if num3 == 1:
                poz += W5[0] + " "
            elif 1 < num3 < 5:
                poz += W5[1] + " "
            else:
                poz += W5[2] + " "
    if (num3 == 0) and (num2 or num1 != 0):
        poz += W5[2] + " "
    if num4 != 0:
        i4 = num4 - 1
        poz += W4[i4] + " "
    if num5 == 1 and num6 == 0:
        poz += W3[0] + " "
    if num5 != 1:
        if num5 != 0:
            i5 = num5 - 1
            poz += W3[i5] + " "
    if num6 != 0:
        if num5 == 1:
            i6 = num6 - 1
            poz += W2[i6] + " " + W6[2]
        else:
            i6 = num6 - 1
            poz += W1a[i6] + " "
            if num6 == 1:
                poz += W6[0] + " "
            elif 1 < num6 < 5:
                poz += W6[1]
            else:
                poz += W6[2]
    if (num6 == 0) and (num5 or num4 or num3 or num2 or num1 != 0):
        poz += W6[2]
    poz = poz.capitalize()
    print("Всего на дорогу придётся потратить", num, "(" + poz + ")\n")  # выводим общую стоимость сначала цифрой, потом буквами

