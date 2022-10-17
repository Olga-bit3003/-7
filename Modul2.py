import Modul1 as md

def lst_name_logger(data):
    md = data.now().strdata('')
    with open('12345.csv', 'a') as file:
        file.write('{};lst_name;{}\n'.format(lst_name_logger))

def lst_surname_logger(data):
    md = data.now().strdata('')
    with open('12345.csv', 'a') as file:
        file.write('{};lst_surname;{}\n'.format(lst_surname_logger))

def  phone_num_logger(data):
    md = data.now().strdata('')
    with open('12345.csv', 'a') as file:
        file.write('{};phone_num;{}\n'.format( phone_num_logger))

