import copy
import datetime
from datetime import date

from Domain.cheltuiala import creeaza_cheltuiala, get_nrAp, get_suma, get_data, get_tipul
from Logic.crud import adauga_cheltuiala, afisare_cheltuieli, sterge_cheltuiala, get_by_nrAp, update_cheltuiala
from Logic.functionalities import cheltuieli_suma_maxima_per_tip, adunare_la_o_cheltuiala_din_data


def adaugare_cheltuiala_ui(lista, nrAp, suma, data, tipul):
    cheltuiala = creeaza_cheltuiala(nrAp, suma, data, tipul)
    adauga_cheltuiala(lista, cheltuiala)


def afiseaza_cheltuieli_ui(lista):
    if len(lista) == 0:
        print("Lista de cheltuieli e goala")
    else:
        afisare_cheltuieli(lista)


def sterge_cheltuiala_ui(lista_cheltuieli, nrAp):
    ok = False
    i = 0
    while i <= len(lista_cheltuieli) - 1:
        if get_nrAp(lista_cheltuieli[i]) == nrAp:
            sterge_cheltuiala(lista_cheltuieli, lista_cheltuieli[i])
            ok = True
        else:
            i += 1
    if not ok:
        print("Cheltuiala cu acest numar de apartament nu exista !")


def modificare(lista_cheltuieli):
    try:
        nrAp = int(input("Dati numarul apartamentului: "))
        cheltuiala_existenta = get_by_nrAp(lista_cheltuieli, nrAp)
        if cheltuiala_existenta is None:
            raise ValueError("Nici o cheltuiala cu numarul de apartamentului dat")

        suma = input("Dati suma (lasati gol pentru a nu se schimba): ")
        if suma == "":
            suma = get_suma(cheltuiala_existenta)
        else:
            suma = float(suma)

        print("Dati data (lasati gol pentru a nu se schimba): ")
        data = date(int(input("Anul: ")), int(input("Luna: ")),int(input("Ziua: ")))
        if data == "":
            data = get_data(cheltuiala_existenta)
        else:
            data = data

        tipul = input("Dati tipul (lasati gol pentru a nu se schimba): ")
        if tipul == "":
            tipul = get_tipul(cheltuiala_existenta)
        else:
            tipul = str(tipul)

        cheltuiala_noua = creeaza_cheltuiala(nrAp, suma, data, tipul)
        lista_cheltuieli = update_cheltuiala(lista_cheltuieli, cheltuiala_noua)

        print("Cheltuiala a fost modificata !")
        return lista_cheltuieli
    except ValueError as ve:
        print("Eroare:", ve, ", reincercati !")
    return lista_cheltuieli

def afiseaza_meniu():
    print("0.Exit")
    print("1.Adaugare cheltuiala")
    print("2.Stergere cheltuiala")
    print("3.Afiseaza cheltuielile")
    print("4.Update")
    print("5.Adunarea unei valori la toate cheltuielile dintr-o data citita")
    print("6.Determinarea celei mai mari cheltuieli pentru fiecare tip de cheltuiala")


def run_console(lista_cheltuieli):
    done = False
    istoric = []

    while not done:
        afiseaza_meniu()
        x = input("Dati o comanda: ")

        if x == "0":
            done = True
            print("Goodbye!")
        elif x == "1":
            istoric.append(lista_cheltuieli.copy())
            nrAp = int(input("Numarul apartamentului cheltuielii: "))
            suma = int(input("Suma cheltuielii: "))
            data = date(int(input("Anul:")), int(input("Luna:")), int(input("Ziua:")))
            tipul = input("Tipul cheltuielii: ")
            try:
                adaugare_cheltuiala_ui(lista_cheltuieli, nrAp, suma, data, tipul)
            except ValueError as ve:
                print(str(ve))
        elif x == "2":
            nrAp = int(input("Numarul apartamentului cheltuielii: "))
            sterge_cheltuiala_ui(lista_cheltuieli, nrAp)
        elif x == "3":
            afiseaza_cheltuieli_ui(lista_cheltuieli)
        elif x == "4":
            lista_cheltuieli = modificare(lista_cheltuieli)
        elif x == "5":
            print("Data:")
            data = date(int(input("Anul: ")), int(input("Luna: ")), int(input("Ziua: ")))
            x = int(input("Valoarea care trebuie adunata:"))
            print(adunare_la_o_cheltuiala_din_data(lista_cheltuieli, data, x))
        elif x == "6":
            print(cheltuieli_suma_maxima_per_tip(lista_cheltuieli))
        else:
            print("Optiune invalida, reincearca !")