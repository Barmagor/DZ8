import sort_date
import sort_name
import view
import print_date
import print_name
import spisok_generation
import sort_id

my_list=spisok_generation.generation_list(50)
def click():
    global my_list
    while True:
        control=view.start()
        if control ==1:
            my_list=sort_date.filter_date()
        elif control ==2:
            my_list=sort_name.filter_name()
        elif control ==3:
            my_list=sort_id.filter_id()
        elif control ==4:
            print_date.print_fd(my_list)
        elif control ==5:
            print_name.print_fio(my_list)
        elif control ==6:
            spisok_generation.generation_list(50)
        elif control ==7:
            for i in my_list:
                print(i)
        elif control ==8:
            break
    
    
    