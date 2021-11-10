from Tests.run_all import run_all_tests
from UI.console import run_console
from Logic.file_ops import load_file
from UI.newfile import run_console2

def main():
    cheltuieli=load_file()
    undo_list=[]
    redo_list=[]

    cheltuieli=run_console(cheltuieli,undo_list,redo_list)
    cheltuieli=run_console2(cheltuieli)
run_all_tests()
main()

