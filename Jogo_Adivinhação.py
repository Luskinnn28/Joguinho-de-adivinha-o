import random

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

numero_secreto = round(random.randrange(1,7))

total_de_tentativas = 5
rodada = 1


while(rodada <= total_de_tentativas):

    print("Tentativa {} de {}".format(rodada, total_de_tentativas))

    chute =int( input("Digite seu chute entre 1 e 5"))
    print("Voce digitou", chute)




    if(chute < 1 or chute > 7):
        print("Leia o que se pede")
        continue


    acertou = numero_secreto == chute
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if (acertou):
        print("Você acertou!")
        break
    else:
        if (maior):
            print("Você errou! O seu chute foi maior que o número secreto.")
        elif (menor):
            print("Você errou! O seu chute foi menor que o número secreto.")

        rodada += 1


