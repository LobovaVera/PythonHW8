# 1. Какой класс? открываем конкретный файл
# 2. Какой предмет?
# 3. Показывает весь список учеников и их оценки по предмету
#  4. Вызвать к доске? если ввести exit то выходит из программы
# 5. На какую оценку ответ?
# 6. После выхода сохранить все изменения в текущий файл


import view
import model
def start():
    
    # 1. Какой класс? открываем конкретный файл
    model.get_data_base()
    model.get_class_list()
    model.open_class_num()
    model.get_class_info()
    model.get_subject_class_info()

    
start()