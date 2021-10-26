from datetime import date

from Domain.cheltuiala import creeaza_cheltuiala
from UI.console import run_console


def main():
    lista_cheltuieli = []
    lista_cheltuieli.append(creeaza_cheltuiala(1, 100, date(2020, 7, 15), "gaz"))
    lista_cheltuieli.append(creeaza_cheltuiala(2, 800, date(2020, 7, 10), "curent"))
    lista_cheltuieli.append(creeaza_cheltuiala(1, 70, date(2020, 5, 12), "gaz"))
    lista_cheltuieli.append(creeaza_cheltuiala(3, 900, date(2020, 6, 25), "curent"))
    lista_cheltuieli.append(creeaza_cheltuiala(4, 120, date(2020, 8, 5), "apa"))
    lista_cheltuieli = run_console(lista_cheltuieli)

main()