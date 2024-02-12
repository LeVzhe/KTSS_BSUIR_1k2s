data_mass = []
tst = []

def download_on_click():
    with open("./db/data.txt", "r") as db:
        lines = db.readlines()
        for line in lines:
            el = line.strip().split()
            el = tuple(e for e in el)
            data_mass.append(el)
        tst.append(data_mass)