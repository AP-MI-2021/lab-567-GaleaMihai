from Domain.cheltuiala import get_suma, get_tipul, get_data


def cheltuieli_suma_maxima_per_tip(lista_cheltuieli):
    """
    Determina cheltuiala cu suma maxima pentru fiecare tip.
    :param lista_cheltuieli:
    :return: un dictionar unde cheile sunt clasele si valorile sunt raspunsurile asociate
    """

    result = {}
    for cheltuiala in lista_cheltuieli:
        suma = get_suma(cheltuiala)
        tipul = get_tipul(cheltuiala)

        if tipul not in result or suma > get_suma((result[tipul])):
            result[tipul] = cheltuiala

    return result


def adunare_la_o_cheltuiala_din_data(lista_cheltuieli, data, x):
    for che in lista_cheltuieli:
        if get_data(che) == data:
            y = get_suma(che)
            che["suma"] = y + x
