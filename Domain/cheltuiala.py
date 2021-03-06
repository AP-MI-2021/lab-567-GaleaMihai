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
    return {
        'id': id,
        'nr_apartament': nr_apartament,
        'suma': suma,
        'data': data.strftime("%d/%m/%Y"),
        'tipul': tipul,
    }

def get_id(cheltuiala):
    '''
    :param cheltuiala:
    :return:
    '''
    return cheltuiala [ 'id' ]

def get_nr_apartament(cheltuiala):
    '''

    :param cheltuiala:
    :return:
    '''
    return cheltuiala [ 'nr_apartament' ]

def get_suma(cheltuiala):
    '''

    :param cheltuiala:
    :return:
    '''
    return cheltuiala [ 'suma' ]

def get_data(cheltuiala):
    '''

    :param cheltuiala:
    :return:
    '''
    return datetime.strptime(cheltuiala [ 'data' ], '%d/%m/%Y')

def get_tipul(cheltuiala):
    '''
    :param cheltuiala:
    :return:
    '''
    return cheltuiala [ 'tipul' ]

def set_tipul(cheltuiala, tipul):
    '''
        :param cheltuiala:
        :param tipul_intretinere:
        :return:
    '''
    cheltuiala['tipul'] = tipul

def set_suma(cheltuiala, suma):
    '''
    :param cheltuiala:
    :param suma:
    :return:
    '''
    cheltuiala['suma'] = suma

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