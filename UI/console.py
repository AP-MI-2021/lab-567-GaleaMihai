from datetime import datetime

from Domain.cheltuiala import to_str, create_cheltuiala, get_nr_apartament, get_tipul, get_data, get_suma
from Logic.crud import add_cheltuiala, delete_cheltuiala, get_by_id, update_cheltuiala
from Logic.file_ops import write_file
from Logic.operatiuni import stergere_cheltuieli, adaugare_valoare_pt_o_data, cheltuiala_mare, ordonare_descrescator, \
    suma_lunara_per_ap
from UI.newfile import run_console2
import copy


def print_menu():
    print('1. CRUD - Create, Read, Update, Delete')
    print('2. Operatiuni')
    print('u. Undo')
    print('r. Redo')
    print('3. Consola2')
    print('x. Iesire')

def run_crud(cheltuieli, undo_list,redo_list):
    def adaugare(cheltuieli, undo_list,redo_list):
        try:
            id = int(input('Dati id-ul:'))
            nr_apartament = int(input('Dati nr. ap.:'))
            suma = float(input('Dati suma:'))
            data = datetime.strptime(input('Dati data (ZZ/LL/AAAA):'), "%d/%m/%Y")
            print('1. Intretinere')
            print('2. Canal')
            print('3. Alte cheltuieli')
            tipul = int(input('Dati tipul (1-3):'))
            if tipul > 3 or tipul < 1:
                raise ValueError('Tip nesuportat')
            else:
                tipul = tipul - 1

            before_add = cheltuieli[:]
            cheltuiala = create_cheltuiala(id, nr_apartament, suma, data, tipul)
            add_cheltuiala(cheltuieli, cheltuiala)
            undo_list.append(before_add)
            redo_list.append(cheltuieli)
            print('Cheltuiala a fost adaugata')
        except ValueError as ve:
            print('Eroare:', ve, ',reincearca!')

    def modificare(cheltuieli,undo_list,redo_list):
        try:
            id = int(input('Dati id-ul: '))
            cheltuiala_existenta = get_by_id(cheltuieli, id)
            if cheltuiala_existenta is None:
                raise ValueError('Nici o cheltuiala cu id-ul dat')

            nr_apartament = input('Dati nr apartament (lasati gol pentru a nu se schimba): ')
            if nr_apartament == '':
                nr_apartament = get_nr_apartament(cheltuiala_existenta)
            else:
                nr_apartament = int(nr_apartament)

            data = input('Dati data (lasati gol pentru a nu se schimba): ')
            if data == '':
                data = get_data(cheltuiala_existenta)
            else:
                data = datetime.strptime(data, "%d/%m/%Y")

            suma = input('Dati suma (lasati gol pentru a nu se schimba): ')
            if suma == '':
                suma = get_suma(cheltuiala_existenta)
            else:
                suma = float(suma)

            print('1. Intretinere')
            print('2. Canal')
            print('3. Alte cheltuieli')
            tipul = input('Dati tipul (1-3, lasati gol pentru a nu se schimba):')
            if tipul == '':
                tipul = get_tipul(cheltuiala_existenta)
            else:
                tipul = int(tipul)
                if tipul > 3 or tipul < 1:
                    raise ValueError('Tip nesuportat')
                else:
                    tipul = tipul - 1

            undo_list.append(cheltuieli)
            cheltuiala_noua = create_cheltuiala(id, nr_apartament, suma, data, tipul)
            cheltuieli = update_cheltuiala(cheltuieli, cheltuiala_noua)
            redo_list.append(cheltuieli)




            print('Cheltuiala a fost modificata!')
            return cheltuieli
        except ValueError as ve:
            print('Eroare:', ve, ',reincearca!')
        return cheltuieli

    def stergere(cheltuieli,undo_list,redo_list):
        try:
            id = int(input('Dati id-ul de sters:'))

            new_cheltuieli = delete_cheltuiala(cheltuieli, id)
            undo_list.append(cheltuieli)
            cheltuieli = new_cheltuieli
            redo_list.append(cheltuieli)

            print('Cheltuiala a fost stearsa!')

            return cheltuieli
        except ValueError as ve:
            print('Eroare:', ve, ', reincearca!')
        return cheltuieli

    def handle_show_all(cheltuieli):
        for cheltuiala in cheltuieli:
            print(to_str(cheltuiala))
        if len(cheltuieli) == 0:
            print('Lista este goala!')

    while True:
        print('1. Adaugare')
        print('2. Stergere')
        print('3. Modificare')
        print('a. Afisare toate')
        print('b. Back')
        op = input('Alegeti optiunea: ')
        if op == '1':
            adaugare(cheltuieli, undo_list,redo_list)
        elif op == '2':
            cheltuieli = stergere(cheltuieli,undo_list,redo_list)
        elif op == '3':
            cheltuieli = modificare(cheltuieli,undo_list,redo_list)
        elif op == 'a':
            handle_show_all(cheltuieli)
        elif op == 'b':
            break
        else:
            print('Comanda invalida, reincearca!')
    return cheltuieli


def run_operatiuni(cheltuieli,undo_list,redo_list):
    def handle_stergere_cheltuieli(cheltuieli,undo_list,redo_list):
       try:
            ap = int(input('Apartamentul cerut:'))
            new_list = copy.deepcopy(cheltuieli)
            undo_list.append(new_list)
            new_cheltuieli = stergere_cheltuieli(cheltuieli, ap)
            list = copy.deepcopy(new_cheltuieli)
            redo_list.append(list)
            return new_cheltuieli
       except ValueError as ve:
            print('Eroare:', ve, ',reincearca!')
            return cheltuieli

    def handle_cheltuieli_data(cheltuieli, undo_list,redo_list):
        try:
            data = datetime.strptime(input('Dati data de cautare (ZZ/LL/AAAA):'), "%d/%m/%Y")
            valoarea = float(input('Dati valoarea de adaugat:'))
            new_list = copy.deepcopy(cheltuieli)
            undo_list.append(new_list)
            new_cheltuieli = adaugare_valoare_pt_o_data(cheltuieli, valoarea, data)
            list = copy.deepcopy(new_cheltuieli)
            redo_list.append(list)
            return new_cheltuieli
        except ValueError as ve:
            print('Eroare:', ve, ',reincearca!')
            return cheltuieli

    def handle_cheltuiala_mare(cheltuieli):
        cheltuiala_mare_dict = cheltuiala_mare(cheltuieli)
        for type in cheltuiala_mare_dict:
            print('{type}: ')
            print(to_str(cheltuiala_mare_dict[type]))

    def handle_ordonare_descrescator(cheltuieli):
        for cheltuiala in ordonare_descrescator(cheltuieli):
            print(to_str(cheltuiala))

    def handle_suma_lunara_per_ap(cheltuieli):
        result = suma_lunara_per_ap(cheltuieli)
        for ap in result:
            print('apartamentul {ap}:')
            for month in result[ap]:
                print('{month} - {result[ap][month]}')

    while True:
        print('1. Stergere cheltuieli:')
        print('2. Af. cheltuielilor dupa adunarea unei valori:')
        print('3. Determinarea celei mai mari cheltuieli pt fiecare tip:')
        print('4. Afisare cheltuielilor descrescator dupa suma:')
        print('5. Afisarea sumelor lunar pt fiecare ap:')
        print('b. Back')
        op = input('Alegeti optiunea: ')
        if op == '1':
            cheltuieli = handle_stergere_cheltuieli(cheltuieli,undo_list,redo_list)
        elif op == '2':
            cheltuieli = handle_cheltuieli_data(cheltuieli,undo_list,redo_list)
        elif op == '3':
            handle_cheltuiala_mare(cheltuieli)
        elif op == '4':
            handle_ordonare_descrescator(cheltuieli)
        elif op == '5':
            handle_suma_lunara_per_ap(cheltuieli)
        elif op == 'b':
            break
        else:
            print('Comanda invalida, reincearca!')
    return cheltuieli

def run_undo(undo_list):
    if len(undo_list) > 0:
        return undo_list.pop()

def run_redo(redo_list):
    if len(redo_list) > 0:
        return redo_list.pop()

def undo(cheltuieli, undo_list):
    undone = run_undo(undo_list)
    if undone is not None:
        cheltuieli = undone
    return cheltuieli

def redo(cheltuieli, redo_list):
    undone = run_redo(redo_list)
    if undone is not None:
        cheltuieli = undone
    return cheltuieli


def run_console(cheltuieli, undo_list, redo_list):
    while True:
        print_menu()
        op = input('Alegeti optiunea: ')

        if op == '1':
            cheltuieli = run_crud(cheltuieli, undo_list, redo_list)
        elif op == '2':
            cheltuieli = run_operatiuni(cheltuieli, undo_list, redo_list)
        elif op == 'u':
            if len(undo_list) > 0:
                redo_list.append(copy.deepcopy(cheltuieli))
                cheltuieli = undo(cheltuieli, undo_list)
        elif op == 'r':
            if len(redo_list) > 0:
                undo_list.append(copy.deepcopy(cheltuieli))
            cheltuieli = redo(cheltuieli, redo_list)
        elif op == '3':
            cheltuieli = run_console2(cheltuieli)
        elif op == 'x':
            break
        else:
            print('Comanda invalida')
    return cheltuieli
