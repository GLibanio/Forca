from palavraForca import palavra

letra_usadas = []
chance = 3
ganhou = False

while True:
    for letra in palavra:
        if letra.lower() in letra_usadas:
            print(letra, end = " ")
        else:
            print("_", end = " ")


    print(f"Você tem {chance} chance")
    tentativa = input("Escolha uma letra!")
    letra_usadas.append(tentativa.lower())


    if tentativa.lower() not in palavra.lower():
        chance -= 1
    
    ganhou = True

    for letra in palavra:
        if letra.lower() not in letra_usadas:
            ganhou = False


    if chance <= 0 or ganhou:
        if ganhou:
            print(f"Você acertou a palavra: {palavra}")
            break
        else:
            print(f"Você errou! A palavra era: {palavra}")
            break