from unicodedata import normalize

def remover_acentos(txt):
    return normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')

def remover_espaco(string):
    aux = string.split()
    aux = "".join(aux)
    return aux

def tratar():
    arq = open("paises.txt", "r")
    lista = arq.readlines()
    n = 0
    while n != len(lista):
        lista[n] = remover_espaco(remover_acentos(lista[n])) 
        n = n + 1
    return lista