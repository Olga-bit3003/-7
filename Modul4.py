
import csv
from Modul1 import lst_name_view
from Modul1 import lst_surname_view
from Modul1 import phone_num_view

def create(device=2):
    Style = 'style =" font-size:22px;"'
    txt = 'csv >\n <head>\n<body>\n'
    txt+= '<p{}>lst_name:{} c </p>\n'.format(Style,lst_name_view(device))
    txt+= '<p{}>lst_surname:{} c </p>\n'.format(Style,lst_surname_view(device))   
    txt+= '<p{}>phone_num:{} c </p>\n'.format(Style,phone_num_view(device))
    txt+='<body>\n</csv>'


    with open ('54321.csv', 'w') as data:
        data.write(csv)
        return csv
         
