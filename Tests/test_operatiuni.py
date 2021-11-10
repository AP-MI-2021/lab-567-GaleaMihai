from Domain.cheltuiala import create_cheltuiala, get_id
from Logic.crud import add_cheltuiala, get_by_numar_apartament, get_by_data, get_by_type, get_by_suma
from Logic.operatiuni import stergere_cheltuieli, adaugare_valoare_pt_o_data, suma_lunara_per_ap
from datetime import datetime


def date_time(str):
    return datetime.strptime(str, '%d/%m/%Y')


def test_stergere_cheltuieli():
    cheltuieli = []
    add_cheltuiala(cheltuieli, create_cheltuiala(10, 1, 1, date_time('10/12/2004'), 1))
    add_cheltuiala(cheltuieli, create_cheltuiala(5, 2, 2, date_time('11/11/2020'), 2))

    cheltuieli = stergere_cheltuieli(cheltuieli, 10)

    assert get_id(get_by_numar_apartament(cheltuieli, 2)[0]) == 5


def test_adaugare_valoare_pt_o_data():
    cheltuieli = []
    add_cheltuiala(cheltuieli, create_cheltuiala(10, 1, 1, date_time('10/12/2004'), 1))
    add_cheltuiala(cheltuieli, create_cheltuiala(5, 2, 2, date_time('11/11/2020'), 2))

    valoare = 10
    data = date_time('11/11/2020')

    cheltuieli = adaugare_valoare_pt_o_data(cheltuieli, valoare, data)

    assert get_id(get_by_numar_apartament(cheltuieli, 2)[0]) == 5


'''def test_suma_lunara_per_ap():
    cheltuieli = [ ]
    add_cheltuiala(cheltuieli, create_cheltuiala(10, 1, 1, date_time('10/12/2004'), 1))
    add_cheltuiala(cheltuieli, create_cheltuiala(5, 2, 2, date_time('11/11/2020'), 2))


    cheltuieli = suma_lunara_per_ap(cheltuieli)

    assert get_by_numar_apartament(get_by_suma(cheltuieli, 2) [ 0 ]) == 2'''
