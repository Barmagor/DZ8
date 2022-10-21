def filter_date():
    x=open("spisok.txt", "r", encoding="UTF-8")
    my_list=[(line.strip())[0:-1] for line in x.readlines()]
    my_list=sorted(my_list,key=lambda i:(int((((i.split(","))[2]).split("."))[2]), int((((i.split(","))[2]).split("."))[1]), int((((i.split(","))[2]).split("."))[0])))
    return my_list