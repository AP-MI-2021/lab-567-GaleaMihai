from Domain.cheltuiala import get_suma, set_suma, get_tipul, get_id, create_cheltuiala, get_nr_apartament, get_data
from Logic.crud import get_by_numar_apartament, delete_cheltuiala, get_by_data, update_cheltuiala, get_by_type

def stergere_cheltuieli(cheltuieli, ap):
    '''
    sterge toate cheltuielile la un apartament
    :param cheltuieli: cheltuielile
    :param ap: apartamentul de sters
    :return: cheltuielile fara cheltuielile pt apartamentul dat
    '''
    found = get_by_numar_apartament(cheltuieli, ap)
    for cheltuiala in found:
        cheltuieli = delete_cheltuiala(cheltuieli, get_id(cheltuiala))
    return cheltuieli

def adaugare_valoare_pt_o_data(cheltuieli, valoare, data):
    '''
        adauga o suma la toate cheltuielile din data ceruta
        :param cheltuieli:
        :param undo: lista de undo
        :param valoare:
        :param data:
        :return: cheltuielile dupa modificare
    '''
    found = get_by_data(cheltuieli, data)
    for cheltuiala in found:
        new_cheltuiala = create_cheltuiala(get_id(cheltuiala),
                                           get_nr_apartament(cheltuiala),
                                           get_suma(cheltuiala) + valoare,
                                           get_data(cheltuiala),
                                           get_tipul(cheltuiala))
        cheltuieli = update_cheltuiala(cheltuieli, new_cheltuiala)
    return cheltuieli

def cheltuiala_mare(cheltuieli):
    '''
    :param cheltuieli:
    :return afisarea cheltuielilor dupa suma in ordine descrescatoare
    '''
    result = {}
    for type in range(1, 4):
        found = get_by_type(cheltuieli, type)
        if not found:
            continue
        found.sort(key=lambda cheltuiala: get_suma(cheltuiala), reverse=True)
        max = found[0]
        type_str = ["intretinere", "canal", "alte chetuieli"][get_tipul(max)]
        result[type_str] = max

    return result

def ordonare_descrescator(cheltuieli):
    '''
    cheltuielile ordonate descrescator dupa suma
    :param cheltuieli:
    :return: cheltuielile ordonate descrescator dupa suma
    '''
    cheltuieli = cheltuieli[:]
    cheltuieli.sort(key=lambda cheltuiala: get_suma(cheltuiala), reverse=True)
    return cheltuieli

def suma_lunara_per_ap(cheltuieli):
    '''
    raportul cu sumele totale pe apartament pe luna
    :param cheltuieli:
    :return: dictionar cu keia aprtamentul si valoarea suma totala lunara
    '''
    result = {}
    for cheltuiala in cheltuieli:
        ap = get_nr_apartament(cheltuiala)
        month = get_data(cheltuiala).strftime('%m/%Y')
        if ap not in result:
            result[ap] = {}
        if month not in result[ap]:
            result[ap][month] = 0
        result[ap][month] = result[ap][month] + get_suma(cheltuiala)

    return result