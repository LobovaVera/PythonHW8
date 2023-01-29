import view
import json

global class_info
class_info = {}

global class_list
class_list =[]

global subject_class_info
subject_class_info = {}

global path
path = "JOURNAL\data_base.txt"

global class_num
class_num = 0


def get_data_base():
    global path
    path = "JOURNAL\data_base.txt"

    global data_base
    data_base = {}

    our_str = ''
    # записываем данные в строку
    with open(path, 'r', encoding ='UTF-8') as file:
        for el in file:
            our_str += el
#    создаем словарик 1 уровня
        our_list = our_str.split('--')
        res_res_dic ={}

        our_dic = {}
        for i in range(0, len(our_list), 2):
            our_dic[our_list[i]]= our_list[i+1]

            str_string = our_dic[our_list[i]]
            list_list = str_string.split(":")
            
#    создаем словарик 2 уровня            
            new_dic = {}
            for j in range(0, len(list_list), 2):
                new_dic[list_list[j]]= list_list[j+1]   
                
            
                str_str_str = new_dic[list_list[j]]
                lis_lis_lis = str_str_str.split(';')
                
#    создаем словарик 3 уровня
                new_new_dic ={}  
                for z in range(0, len(lis_lis_lis), 2):
                    new_new_dic[lis_lis_lis[z]] = lis_lis_lis[z+1]
# собираем словарь из словариков
                res_res_dic[list_list[j]] = new_new_dic
            data_base[our_list[i]] = res_res_dic
             
            # res_dic[our_list[i]] = new_dic
    
    # print("get_data_base")
    view.show("Вы открыли журнал")

           
def get_class_list():
    global class_list
    class_list =[]
    for el in data_base:
        el = el.strip()
        class_list.append(el)
    print("get_class_list")

def open_class_num():
    global class_num
    # """ проверяем наличие класса с таким номером """
    while True:
        class_num = view.get_class()
        print(class_num)
        print(class_list)

        for i in class_list:
            if i == class_num:
                print(class_num)
                return class_num  
        else:
            view.show("Нет такого класса, попробуйте ввести номер класса еще раз")  
            continue  

def get_class_info():
    global class_info
    class_info = {}
    for el in data_base:
        # print(el)
        # print(class_num)
        if el == class_num:
            class_info = data_base[el]
            # view.show(class_info)


def get_subject_class_info():
    global subject_class_info
    subject_class_info = {}
    subject = ''
    subj_num = view.get_subject()
    match subj_num:
        case 1:
            subject = '\nматематика'
        case 2:
            subject = '\nрусский'
        case 3:
            subject = '\nанглийский'
    # print(class_info)
    for el in class_info:
        # print(el)
        # print(subject)
        if el == subject:
            subject_class_info = class_info[el]
            view.show(subject_class_info)
    # print("get_class_info")





# def select_subject():
#     subject_num = view.get_subject()
#     while True:
#         try:
#             subject_num = int(subject_num)
#         except:
#             view.show("Введите цифру 1, 2 или 3 без пробелов")
#             continue


