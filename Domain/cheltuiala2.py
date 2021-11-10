from datetime import datetime

def create_cheltuiala(id, nr_apartament, suma, data, tipul):
    '''
     :param id:
     :param nr_apartament:
     :param suma:
     :param data:
     :param tipul:
     :return noua cheltuila:
    '''
    return [id, nr_apartament, suma, data, tipul]

def get_id(cheltuiala):
    '''
    :param cheltuiala:
    :return:
    '''
    return cheltuiala[0]

def get_nr_apartament(cheltuiala):
    '''

    :param cheltuiala:
    :return:
    '''
    return cheltuiala[1]

def get_suma(cheltuiala):
    '''

    :param cheltuiala:
    :return:
    '''
    return cheltuiala[2]

def get_data(cheltuiala):
    '''

    :param cheltuiala:
    :return:
    '''
    return datetime.strptime(cheltuiala[3], '%d/%m/%Y')

def get_tipul(cheltuiala):
    '''
    :param cheltuiala:
    :return:
    '''
    return cheltuiala[4]


def to_str(cheltuiala):
    '''
    :param cheltuiala:
    :return: un string format cu cheltuielile
    '''

    return f'Cheltuiala cu id={get_id(cheltuiala)},\
    nr_apartamente={get_nr_apartament(cheltuiala)},\
    suma={get_suma(cheltuiala)},\
    data={cheltuiala["data"]},\
    tipul={[ "intretinere", "canal", "alte chetuieli" ] [ get_tipul(cheltuiala) ]}'
