from writeinputinfile3 import writing_scv
from input2 import read1, get_info, write_newfile_alldata, write_newfile_namedata

print('Меню', "\n1 - добавить сотрудника","\n2 - напечатать данные о сотрудниках",
      "\n3 - экспортировать данные в новый файл", "\n4 - экспортировать данные об именах сотрудноков (фамилия и имя) "
                                                  "в новый файл")
# writing_scv()
# read1()
while True:
    x = input('Введите команду: ')
    if x == '1':
        info = get_info()
        writing_scv(info)
    elif x == '2':
        read1()
    elif x == "3":
        write_newfile_alldata()
    elif x == "4":
        write_newfile_namedata()
