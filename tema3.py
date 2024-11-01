meniu = ['papanasi'] * 10 + ['ceafa'] * 3 + ["guias"] * 6
preturi = [["papanasi", 7], ["ceafa", 10], ["guias", 5]]
studenti = ["Liviu", "Ion", "George", "Ana", "Florica"]  # coada FIFO
comenzi = ["guias", "ceafa", "ceafa", "papanasi", "ceafa"]  # coada FIFO
tavi = ["tava"] * 7  # stiva LIFO
istoric_comenzi = []
comenzi_guias = []
comenzi_ceafa = []
comenzi_papanasi = []
while len(studenti) > 0:
    if len(comenzi) > 0:
        if len(tavi) > 0:
            student = studenti.pop(0)
            comanda = comenzi(0)
            tavi.pop()
            istoric_comenzi.append(comanda)
            print(student, "a comandat", comanda)
            if comanda == "guias":
                comenzi_guias.append(comanda)
            elif comanda == "ceafa":
                comenzi_ceafa.append(comanda)
            elif comanda == "papanasi":
                comenzi_papanasi.append(comanda)
print("S-au comandat", len(comenzi_guias), "guias,", len(comenzi_ceafa), "ceafa,", len(comenzi_papanasi), "papanasi.")
print("Mai sunt", len(tavi), "tavi.")
print("Mai este ceafa:", meniu.count("ceafa") > len(comenzi_ceafa))
print("Mai sunt papanasi:", meniu.count("papanasi") > len(comenzi_papanasi))
print("Mai este guias:", meniu.count("guias") > len(comenzi_guias))
total_incasari = 0
for pret in preturi:
    produs = pret[0]
    valoare = pret[1]
    if produs == "papanasi":
        total_incasari += valoare * len(comenzi_papanasi)
    if produs == "ceafa":
        total_incasari += valoare * len(comenzi_ceafa)
    if produs == "guias":
        total_incasari += valoare * len(comenzi_guias)
produse_ieftine =[]
for produs in preturi:
    if produs[1] <= 7:
        produse_ieftine.append(produs)
print("Cantina a incasat:", total_incasari, "lei.")
print("Produse care costa cel mult 7 lei:", produse_ieftine)
