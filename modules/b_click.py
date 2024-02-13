data_mass = []

def download_on_click():
    with open("./db/data.txt", "r") as db:
        lines = db.readlines()
        for line in lines:
            el = line.strip().split()
            el = [e for e in el]#tuple(e for e in el)
            data_mass.append(el)