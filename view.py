def start():
    print("Если хотите отсортировать список по дате рождения, введите 1")
    print("Если хотите отсортировать список по ФИО, введите 2")
    print("Если хотите отсортировать список по ID, введите 3")
    print("Если хотите распечатать список из дней рождений, введите 4")
    print("Если хотите распечатать список из ФИО, введите 5")
    print("Если хотите сгенерировать новый список, введите 6")
    print("Если хотите вывести список, введите 7")
    print("Если хотите выйти, введите 8")
    num = int(input())
    while num<1 or num>8:
        print("Введите число от 1 до 8")
        try:
            num = int(input())
        except ValueError:
            print("Введите корректное число")
    return num