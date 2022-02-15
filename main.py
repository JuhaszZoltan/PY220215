import modul as m

osztaly = [
    m.Diak(1, 'Para Zita',    2005),
    m.Diak(2, 'Viz Elek',     2004),
    m.Diak(3, 'Fütty Imre',   2002),
    m.Diak(4, 'Végh Béla',    2006),
    m.Diak(5, 'Lapos Elemér', 2005)]

# egy_db_diak = m.Diak(107, 'Alap Béla', 1986)
# print(f'{egy_db_diak.nev} {2022-egy_db_diak.szul_ev} éves')
# print(f'{osztaly[0].nev} {2022 - osztaly[0].szul_ev} éves')

print(f'legidősebb diák: {m.legidosebb_diak_neve(osztaly)}')
print(f'a diákok átlagéletkora: {m.osztaly_atlageletkora(osztaly)}')