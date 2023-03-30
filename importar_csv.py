import csv

#Configurar arxiu csv
def config_csv(arxiu, i):
    with open(arxiu, newline="\n", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile, delimiter=":")
        for linia,valor in enumerate(reader):
            if linia == i:
                return valor


#Imprimir info d'arxiu csv
def importar_csv(arxiu):
    with open(arxiu, newline="\n", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile, delimiter=":")
        dades = []
        for i,valor in enumerate(reader):
            dades.append(valor)
        return dades