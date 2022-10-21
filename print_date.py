def print_fd(_list):
    _list = [((i.split(","))[2])[:-1] for i in _list]
    with open("birthday.txt", "w", encoding="UTF-8") as file:
        for i in _list:
            file.write(i + "\n")
            print("список сгенерирован в новый файл")
