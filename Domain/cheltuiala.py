from datetime import date


def creeaza_cheltuiala(nrAp, suma, data, tipul):
    """
    creeaza o cheltuiala

    :param nrAp: string, numarul apartamentului
    :param suma: float, suma cheltuielii
    :param data: datetime, data cheltuielii
    :param tipul: string, tipul rezervarii
    :return: un obiect cheltuiala
    """
    tip_cheltuiala = ["apa", "curent", "gaz"]
    if nrAp < 1 and nrAp != int(nrAp):
        raise ValueError('Numarul apartamentului trebuie sa fie natural')
    if tipul not in tip_cheltuiala:
        raise ValueError('Tipul nu este valid')
    if suma < 0:
        raise ValueError('Suma trebuie sa fie pozitiva')
    # if data:
    # raise ValueError('Data trebuie sa fie de tipul datetime')

    return {
        "nrAp": nrAp,
        "suma": suma,
        "data": data,
        "tipul": tipul
    }


def get_nrAp(cheltuiala):
    """
    Numarul apartamentului cheltuielii

    :param cheltuiala:
    :return: numarul apartamentului cheltuielii
    """
    return cheltuiala["nrAp"]


def get_suma(cheltuiala):
    """
    Suma cheltuielii

    :param cheltuiala:
    :return: suma cheltuielii
    """
    return cheltuiala["suma"]


def get_data(cheltuiala):
    """
    Data cheltuielii

    :param cheltuiala:
    :return: data cheltuielii
    """
    return cheltuiala["data"]


def get_tipul(cheltuiala):
    """
    Tipul cheltuielii

    :param cheltuiala:
    :return: tipul cheltuielii
    """
    return cheltuiala["tipul"]


def to_string(cheltuiala):
    """
    Creeaza un string cu proprietatiile cheltuielii

    :param cheltuiala:
    :return: un string format cu proprietatiile cheltuielii
    """
    return "nrAp: {}, suma: {}, data: {}, tipul: {}".format(
        get_nrAp(cheltuiala),
        get_suma(cheltuiala),
        get_data(cheltuiala),
        get_tipul(cheltuiala)
    )
