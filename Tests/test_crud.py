from Domain.cheltuiala import create_cheltuiala, get_id
from Logic.crud import add_cheltuiala, get_by_id, delete_cheltuiala, get_by_numar_apartament
from datetime import datetime


def date_time(str):
    return datetime.strptime(str, '%d/%m/%Y')


def test_add_cheltuiala():
    cheltuieli = []
    p1 = create_cheltuiala(10, 1, 1, date_time('10/12/2004'), 1)
    add_cheltuiala(cheltuieli, p1)
    assert len(cheltuieli) == 1
    assert get_by_id(cheltuieli, 10) == p1

    p2 = create_cheltuiala(5, 2, 2, date_time('11/11/2020'), 2)
    add_cheltuiala(cheltuieli, p2)
    assert len(cheltuieli) == 2
    assert get_by_id(cheltuieli, 10) == p1
    assert get_by_id(cheltuieli, 5) == p2


def test_delete_cheltuiala():
    cheltuieli = []
    add_cheltuiala(cheltuieli, create_cheltuiala(10, 1, 1, date_time('10/12/2004'), 1))
    add_cheltuiala(cheltuieli, create_cheltuiala(5, 2, 2, date_time('11/11/2020'), 2))

    cheltuieli = delete_cheltuiala(cheltuieli, 10)
    assert get_id(get_by_id(cheltuieli, 5)) == 5
    assert get_id(get_by_numar_apartament(cheltuieli, 2)[0]) == 5
    assert get_by_id(cheltuieli, 10) is None

    try:
        cheltuieli = delete_cheltuiala(cheltuieli, 67)
        assert False
    except Exception:
        pass

    assert len(get_by_numar_apartament(cheltuieli, 1)) == 0
    assert get_id(get_by_numar_apartament(cheltuieli, 2)[0]) == 5

