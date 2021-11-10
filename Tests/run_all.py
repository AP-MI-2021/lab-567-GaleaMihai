from Tests.test_crud import test_add_cheltuiala,test_delete_cheltuiala
from Tests.test_operatiuni import test_stergere_cheltuieli,test_adaugare_valoare_pt_o_data

def run_all_tests():
     test_add_cheltuiala()
     test_delete_cheltuiala()
     test_stergere_cheltuieli()
     test_adaugare_valoare_pt_o_data()
