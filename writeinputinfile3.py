from input2 import get_info as gi #из модуля user_interface импортируем метод get_info(заполняющий тел. книгу).


def writing_scv (info): #функция, которая при заполнении тел. книги, форматирует ее визуальную структуру (данные заполняются в строку)
    file = 'Phonebook.csv'
    with open (file, 'a', encoding = 'utf-8') as data:
        data.write(f'{info[0]["Фамилия"]}; {info[1]["Имя"]}; {info[2]["Телефон"]}; {info[3]["Описание"]}; '
                   f'{info[4]["Зароботная плата (тыс. руб.)"]}\n')




