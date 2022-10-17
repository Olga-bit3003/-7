import Modul1 as prov
import Modul2 as log

def lst_name_view(data):
    data = prov.get_lst_name(data)
    log.lst_name_logger(data)
    return data

def lst_surname_view(data):
    data = prov.get_lst_surname(data)
    log.lst_surname_logger(data)
    return data
def  phone_num_view(data):
    data = prov.get_phone_num (data)
    log. phone_num_logger(data)
    return data