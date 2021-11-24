import copy

from Domain.cheltuiala import create_cheltuiala, get_id
from Logic.crud import add_cheltuiala, get_by_numar_apartament, get_by_data, get_by_type, get_by_suma
from Logic.operatiuni import stergere_cheltuieli, adaugare_valoare_pt_o_data, suma_lunara_per_ap
from datetime import datetime

from UI.console import undo


def date_time(str):
    return datetime.strptime(str, '%d/%m/%Y')


def test_undo():
    cheltuieli = []
    undo_list = []
    redo_list = []
    add_cheltuiala(cheltuieli, create_cheltuiala(10, 1, 1, date_time('10/12/2004'), 1))
    add_cheltuiala(cheltuieli, create_cheltuiala(5, 2, 2, date_time('11/11/2020'), 2))
    print(cheltuieli)
    ap = 5
    new_list = copy.deepcopy(cheltuieli)
    undo_list.append(new_list)
    new_cheltuieli = stergere_cheltuieli(cheltuieli, 10)
    list = copy.deepcopy(new_cheltuieli)
    redo_list.append(list)

    print(list)
    redo_list.append(copy.deepcopy(cheltuieli))
    cheltuieli = undo(cheltuieli, undo_list)

    print(get_id(get_by_numar_apartament(cheltuieli, 2)[1]))

    assert get_id(get_by_numar_apartament(cheltuieli, 2)[0]) == 10
