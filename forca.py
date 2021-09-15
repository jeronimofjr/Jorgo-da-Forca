import pais
import board

def inicio():
    print("*********************************")
    print("***Bem-vindo ao jogo da Força!***")
    print("*********************************\n")
    print(board.board(0))

def jogada(chutes):
    chute = input("Digite uma letra: ")
    chutes.append(chute)
    return chute, chutes


def palavra(): 
    return pais.sortear_pais()

def forca(palavra_secreta): 
    return ['_' for _ in palavra_secreta]

def jogo():
    chutes = []
    tentativas = 0
    inicio()
    palavra_secreta = palavra()
    letras_acertadas = forca(palavra_secreta)
    while True:
        print(" ".join(letras_acertadas))
        print("")
        aux = jogada(chutes)
        
        chute = aux[0]
        chutes = aux[1]
        if chute not in palavra_secreta:
            tentativas += 1
            print(board.board(tentativas))
        else:
            for i in range(0, len(palavra_secreta)):
                if chute == palavra_secreta[i]:
                    letras_acertadas[i] = chute
       
        if tentativas == 6:
            print('\nDerrota! Você perdeu!\nA palavra certa era:', palavra_secreta, '\n')
            return -1
        elif "_" not in letras_acertadas: 
            print(" ".join(letras_acertadas), '\n\nVitória! Você Ganhou!\n')
            return 1
def main():
    v = 0
    d = 0
    while True:
        resultado = jogo()
        if resultado:
            v += 1
        else:
            d += 1
        op = input("Você deseja continuar? s/n ")
        if op == "n":
            print("\nPlacar:\nVitórias:", v)
            print("Derrotas:", d, "\n")
            break
main()