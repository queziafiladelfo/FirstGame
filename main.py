print("#------------------------------------#")
print("   Bem vindo ao meu primeiro jogo!!!")
print("#------------------------------------#")
name = input("    Qual é o seu nome? ")
age = int(input("    Qual a sua idade? "))
print("#------------------------------------#")

print("Olá, ", name)

if age >= 18:
    print("Você tem idade suficiente para jogar!")

    vida = 10

    wants_to_play = input("Deseja continuar?(sim/nao): ").lower()
    if wants_to_play == "sim":
        print(" ")
        print("          ##################")
        print("          |VAMOS COMEÇAR!!!|")
        print("          ##################")
        print(" ")

        print("# ", name, " você está começando com ", vida, " de vida #")
        print(" ")

        left_or_rigth = input("Faça sua escolha ....ESQUERDA ou DIREITA? ").lower()
        print(" ")

        if left_or_rigth == "esquerda":
            print(
                "Legal, você escolheu o caminho da esquerda e chegou a um lago. O que quer fazer agora?"
            )
            ans = input("Nadar ou contornar o lago? (nadar/contornar): ").lower()

            if ans == "contornar":
                print(" ")
                print(
                    "Você escolheu contornar o lago e chegou ao outro lado em segurança."
                )
                print("Parabéns!!! Voce venceu....")
            elif ans == "nadar":
                print(" ")
                print(
                    "Você escolheu nadar para chegar ao outro lado, mas ficou sem fôlego e voltou na metade do caminho."
                )

                vida -= 5
                
                print(" ")  
                print("Você perdeu 5 de vida e está com ", vida,
                      " de vida restantes.")
                              
                ans = input("Deseja tentar novamente? (sim/nao): ").lower()
                if ans == "sim":

                    print(" ")                   
                    print("Ao voltar você notou uma casa perto do rio.")
                    ans = input(
                        "Deseja ir a casa ou tentar nadar de novo? (casa/nadar): ").lower()

                   
                    if ans == "casa":
                        print(" ")
                        print("Você escolheu ir para a casa e passar a noite.")
                        print("Ao amanhecer o dono da casa foi seu guia e te levou pelo caminho certo.")
                        print("Parabéns!!! Voce venceu....")                       
                    else:
                        print(" ")
                        print("Voce escolheu tentar nadar novamente e se afogou.")
                        vida -= 5
                        print("# Voce agora esta com ", vida, " de vida #")
                        print("Voce perdeu...")
     

                else:
                    print(" ")
                    print("Voce escolheu não tentar novamente")
                    print("Voce perdeu...")

            else:
                print("Você perdeu =/ ....")

        else:
            print("Você se perdeu....")
    else:
        print(" ")
        print("          ##################")
        print("          |.......BYE......|")
        print("          ##################")
        print(" ")

else:
    print("Você não tem idade suficiente para jogar.")
