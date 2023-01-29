
def get_class():
    return input("Введите номер класса (букву кириллицей, например 1б): ")

def get_subject():
    subject = input("Какой предмет Вас интересует? Математика - введите 1, русский язык - введите 2, английский -введите 3: ")
    while True:
        try:
            int(subject)
            return int(subject)
        except:
            print("Ошибка ввода. Введите одно число: 1 или 2 или 3, без пробелов и запятых еще раз.")
    

def show(text):
    print(text)

