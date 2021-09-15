import remover_acentos
import random

def sortear_pais():
    pais = random.choice(remover_acentos.tratar())
    aux = ""
    for i in range(0, len(pais)):
        aux += pais[i].lower()
    return aux
