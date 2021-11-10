from Domain.cheltuiala import create_cheltuiala, get_id, get_nr_apartament, get_data, get_tipul,get_suma
from Logic.file_ops import write_file

def get_by_id(cheltuieli,id):
    '''
    Gaseste cheltuielile dupa id.
    :param cheltuieli:
    :param id:
    :return: cheltuiala sau none daca nu exista
    '''
    for cheltuiala in cheltuieli:
        if get_id(cheltuiala) == id:
            return cheltuiala
    return None

def get_by_numar_apartament(cheltuieli, nr_apartament):
    '''
    Find all cheltuielii with nr_apartament
    :param cheltuieli:
    :param nr_apartament:
    :return all cheltuielii with nr_apartament
    '''
    return [cheltuiala for cheltuiala in cheltuieli if get_nr_apartament(cheltuiala) == nr_apartament]

def get_by_suma(cheltuieli, suma):
    '''

    :param cheltuieli:
    :param suma:
    :return:
    '''
    return [cheltuiala for cheltuiala in cheltuieli if get_suma(cheltuieli) == suma]

def get_by_data(cheltuieli, data):
    '''
    Find all cheltuielii with data
    :param cheltuieli:
    :param data:
    :return all cheltuielii with data
    '''
    return [cheltuiala for cheltuiala in cheltuieli if get_data(cheltuiala) == data]

def get_by_type(cheltuieli, type):
    '''
    Find all cheltuielii with type
    :param cheltuieli:
    :param type:
    :return all cheltuielii with type
    '''
    return [cheltuiala for cheltuiala in cheltuieli if get_tipul(cheltuiala) == type]

def add_cheltuiala(cheltuieli, cheltuiala ,filename='cheltuieli.txt'):
    '''
   :param cheltuiala: cheltuiala de adaugat
   :param cheltuieli: cheltuielile
   :raises: ValueError daca id-ul nu este unic
   '''
    cheltuiala_existenta=get_by_id(cheltuieli,id)
    if cheltuiala_existenta is not None:
        raise ValueError('Id-ul exista deja!')
    cheltuieli.append(cheltuiala)
    write_file(cheltuieli, filename)

def update_cheltuiala(cheltuieli, cheltuiala, filename='cheltuieli.txt'):
    result = [ cheltuiala_existenta for cheltuiala_existenta in cheltuieli if get_id(cheltuiala) != get_id(cheltuiala_existenta) ] + [ cheltuiala ]
    write_file(result, filename)
    return result

def delete_cheltuiala(cheltuieli,id,filename='cheltuieli.txt'):
    '''
    Sterge o cheltuiala.
    :param cheltuieli:lista de cheltuieli.
    :param id:id-ul cheltuielii care trb sters.
    :return:o noua lista din care va lipsi prajitura cu id-ul id.
    :raises: ValueError, daca id-ul nu exista

    '''
    cheltuiala_existenta=get_by_id(cheltuieli,id)
    if cheltuiala_existenta is None:
        raise ValueError('Id-ul dat nu exista!')
    rezultat=[cheltuiala for cheltuiala in cheltuieli if get_id(cheltuiala) != id]
    write_file(cheltuieli,filename)
    return rezultat


