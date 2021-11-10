from datetime import datetime

from Domain.cheltuiala import to_str, create_cheltuiala
from Logic.crud import add_cheltuiala,delete_cheltuiala
from Logic.operatiuni import ordonare_descrescator

def print_meniu():
    print('Citeste stringul cu operatiuni separate prin virgula')
    print('Adaugare,<id>,<nr_apartamente>,<suma>,<data>,<tipul>')
    print('Stergere,<id> - este pentru stergere')
    print('Showall - pentru afisare')
    print('Ordonare - ordonare descarescator dupa pret')
    print('Stop - iesire')


def run_console2(cheltuieli):
    def handle_show_all(cheltuieli_to_show):
        for cheltuiala in cheltuieli_to_show:
            print(to_str(cheltuiala))
        if len(cheltuieli_to_show) == 0:
            print('Lista este goala!')

    x = True

    while x:
        print_meniu()
        str = input('Dati stringul:')
        new_str = str.split(';')
        for c in new_str:
            comanda = c.split(',')
            if comanda[0] == 'Adaugare':
                try:
                    id = int(comanda[1])
                    nr_apartament = int(comanda[2])
                    suma = int(comanda[3])
                    data = datetime.strptime(comanda[4], "%d/%m/%Y")
                    tipul = int(comanda[5])
                    if tipul > 3 or tipul < 1:
                        raise ValueError('Tip nesuportat')
                    else:
                        tipul = tipul - 1

                    cheltuiala = create_cheltuiala(id, nr_apartament, suma, data, tipul)
                    add_cheltuiala(cheltuieli, cheltuiala)

                    print('Cheltuiala a fost adaugata')
                except Exception as ve:
                    print('Eroare:', ve, ',reincearca!')


            elif comanda[0] == 'Stergere':
                try:
                    id = int(comanda[1])
                    cheltuieli = delete_cheltuiala(cheltuieli, id)
                    print('Cheltuiala a fost stearsa!')
                except ValueError as ve:
                    print('Eroare:', ve, ', reincearca!')

            elif comanda[0] == 'Showall':
                handle_show_all(cheltuieli)

            elif comanda[0] == 'Ordonare':
                for cheltuiala in ordonare_descrescator(cheltuieli):
                    print(to_str(cheltuiala))

            elif comanda[0] == 'Stop':
                x = False

