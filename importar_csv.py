import csv

#Configurar arxiu csv
def config_csv(arxiu, linia):
    with open(arxiu, newline="\n", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile, delimiter=":")
        for i,valor in enumerate(reader):
            if i == linia:
                return valor


#Imprimir info d'arxiu csv
def importar_csv(arxiu, linia):
    with open(arxiu, newline="\n", encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile, delimiter=":")
        dades = []
        for i,valor in enumerate(reader):
            if i < linia: 
                dades.append(valor)
        return dades