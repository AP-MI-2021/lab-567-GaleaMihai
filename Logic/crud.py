from Domain.cheltuiala import to_string, get_nrAp, get_suma, get_data, get_tipul


def adauga_cheltuiala(lista, cheltuiala):
    lista.append(cheltuiala)


def afisare_cheltuieli(lista):
    for che in lista:
        print(to_string(che))


def sterge_cheltuiala(lista_cheltuieli, nrAp):
    lista_cheltuieli.remove(nrAp)


def get_by_nrAp(lista_cheltuieli, nrAp):
    """
    Gaseste cheltuielile dupa numarul apartamentului
    :param lista_cheltuieli:
    :param data:
    :return: cheltuiala sau none daca nu exista
    """
    for cheltuiala in lista_cheltuieli:
        if get_nrAp(cheltuiala) == nrAp:
            return cheltuiala
    return None


def update_cheltuiala(lista_cheltuieli, cheltuiala):
    result = [cheltuiala_existenta for cheltuiala_existenta in lista_cheltuieli] + [cheltuiala]
    return result


def add_cheltuiala(lista_cheltuieli, cheltuiala):
    """

    :param lista_cheltuieli:cheltuielile
    :param cheltuiala: cheltuiala de adaugat
    :return:
    """
    lista_cheltuieli.append(cheltuiala)
