import view
import json


class_list =[]
global path
path = "JOURNAL\data_base.txt"

def open_class_num():
    # """ проверяем наличие класса с таким номером """
    while True:
        class_num = view.get_class()
        if class_num in class_list:
            return True
        else:
            view.show("Нет такого класса, попробуйте ввести номер класса еще раз")  
            continue  

def select_subject():
    subject_num = view.get_subject()
    while True:
        try:
            subject_num = int(subject_num)
        except:
            view.show("Введите цифру 1, 2 или 3 без пробелов")
            continue

def get_data_base():
    global path
    path = "JOURNAL\data_base.txt"
    global data_base
    data_base = {}
    our_str = ''
    with open(path, 'r', encoding ='UTF-8') as file:
        for el in file:
            our_str += el
   
        our_list = our_str.split('--')
        res_res_dic ={}
        res_dic ={}
        our_dic = {}

        for i in range(0, len(our_list), 2):
            our_dic[our_list[i]]= our_list[i+1]

            str_string = our_dic[our_list[i]]
            list_list = str_string.split(":")
            
            new_dic = {}
            for j in range(0, len(list_list), 2):
                new_dic[list_list[j]]= list_list[j+1]   
                
            
                str_str_str = new_dic[list_list[j]]
                lis_lis_lis = str_str_str.split(';')
                
                new_new_dic ={}  
                for z in range(0, len(lis_lis_lis), 2):
                    new_new_dic[lis_lis_lis[z]] = lis_lis_lis[z+1]
                res_res_dic[list_list[j]] = new_new_dic
            data_base[our_list[i]] = res_res_dic
                



            res_dic[our_list[i]] = new_dic
   
        print(data_base)

           
            


get_data_base()


def get_class_list(class_num):
    pass

