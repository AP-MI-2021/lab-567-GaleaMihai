import json

def write_file(cheltuieli, filename='cheltuieli.txt'):
    with open(filename, 'w') as f:
        json.dump(cheltuieli, f)

def load_file(filename='cheltuieli.txt'):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except:
        return []