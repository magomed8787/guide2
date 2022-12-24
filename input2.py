
def get_info (): #функция заполнения телефонной книги
        info = []
        info.append({'Фамилия': input("Введите фамилию: ")})  # x [0]['a']= 1
        info.append({'Имя': input("Введите имя: ")})
        info.append({'Телефон': ""})
        valid = False
        while not valid:
            try:
                info[2] = {"Телефон": input("Введите номер телефона: ")}
                if len(info[2]["Телефон"]) != 11:
                    print('В номере телефона должно быть 11 цифр.')
                else:
                    info[2]["Телефон"] = int(info[2]["Телефон"])
                    valid = True
            except:
                print("Номер телефона должен состоять только из цифр")
        info.append({'Описание': input("Введите описание: ")})
        info.append({'Зароботная плата (тыс. руб.)': int(input("Введите размер зароботной платы: "))})
        print(info)
        return info

def read1 ():
        with open("Phonebook.csv", "r", encoding='utf-8') as file1:
            # итерация по строкам
            for line in file1:
                print(line.strip())

def write_newfile_alldata():
    with open('Phonebook.csv', 'r', encoding='utf-8') as first, open('Phonebook2.csv', 'w', encoding='utf-8') as second:
            data = first.read()
            second.write(data)

def write_newfile_namedata():
    with open('Phonebook.csv', 'r', encoding='utf-8') as first, open('Phonebook2.csv', 'w', encoding='utf-8') as second:
        for line in first:
            second.write(line.split(";")[0])
            second.write(line.split(";")[1] + '\n')

