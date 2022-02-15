class Diak:
    def __init__(self, id, nev, szul_ev):
        self.id = int(id)
        self.nev = nev
        self.szul_ev = int(szul_ev)


def legidosebb_diak_neve(diakok_listaja):
    mini = 0
    for i in range(1, len(diakok_listaja)):
        if diakok_listaja[i].szul_ev < diakok_listaja[mini].szul_ev:
            mini = i
    return diakok_listaja[mini].nev


def osztaly_atlageletkora(diakok_listaja):
    sum = 0
    for d in diakok_listaja:
        sum += (2022 - d.szul_ev)
    return sum / len(diakok_listaja)