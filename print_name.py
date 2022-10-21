def print_fio(_list):
    _list = [(i.split(","))[1] for i in _list]
    with open("names.txt", "w", encoding="UTF-8") as file:
        for i in _list:
            file.write(i+"\n")
            print("список сгенерирован в новый файл")