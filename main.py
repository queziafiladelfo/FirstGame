print("#------------------------------------#")
print("   Bem vindo ao meu primeiro jogo!!!")
print("#------------------------------------#")
name = input("    Qual é o seu nome? ")
age = int(input("    Qual a sua idade? "))
print("#------------------------------------#")

print("Olá, ", name)

if age >= 18:
    print ("Você tem idade suficiente para jogar!")

    wants_to_play = input("Deseja continuar?(sim/nao): ").lower()
    if wants_to_play == "sim":
        print(" ")
        print("          ##################")
        print("          |VAMOS COMEÇAR!!!|")
        print("          ##################")
        print(" ")

        left_or_rigth = input("Faça sua escolha ....ESQUERDA ou DIREITA? ")
    else:
        print(" ")
        print("          ##################")
        print("          |.......BYE......|")
        print("          ##################")
        print(" ") 
        
else:
    print ("Você não tem idade suficiente para jogar.")
