import random

difi = int(input("Escolha o nível (1)noob = 16 chutes, (2)intermediario = 10 chutes,  (3)veterano = 4 chutes, ou (4)impossível = 1 chute"))

if difi == 1:
    chutes = 16
    jogadas = 0
    sorteio = random.randint(0, 70)
elif difi == 2:
    chutes == 10
    jogadas = 0
    sorteio = random.randint(0, 85)
elif difi == 3:
    
    chutes = 4
    jogadas = 0
    sorteio = random.randint(0, 100)
elif difi == 4:
    chutes = 1
    jogadas = 0
    sorteio = random.randint(0, 150)
else:
    print("Digite um número de 1 a 4.")


while chutes > 0:
    num = int(input("Chute um número: "))

    if num < sorteio:
        print("O número é maior.")
    elif num > sorteio:
        print("O número é menor.")
    else:
        print("Você acertou o número!")
        break
        
    chutes -= 1
    jogadas += 1

    if chutes == 0:
        print(f"Você perdeu. O número correto era {sorteio}.")
        break

print(f"Total de jogadas: {jogadas}")


