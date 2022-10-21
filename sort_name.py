def filter_name():
    x=open("spisok.txt", "r", encoding="UTF-8")
    my_list=[(line.strip())[0:-1] for line in x.readlines()]
    print(my_list)
    my_list=sorted(my_list,key=lambda i:((((i.split(","))[1]).split(" "))[0], (((i.split(","))[1]).split(" "))[1], (((i.split(","))[1]).split(" "))[2]))
    print(my_list)
    return my_list

