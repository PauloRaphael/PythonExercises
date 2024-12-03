class MathFunc:

    @staticmethod
    def fizzbuzz(n, dict):
        #Receives a dictionary as a parameter with all the words and divisors
        string = ""
        #iterates from 1 to n+1
        for i in range(1, n + 1):
            string = ""

            #Goes through the dictionary checking if 
            #the value is divisible by the iteration number
            #and adding the key in the string
            for key, value in dict.items():
                if i % value == 0:
                    string += key
        
            #if string is null print number if not print string
            if len(string) == 0:
                print(i)
            else:
                print(string)
                
    #returns a dictionary based on user input
    @staticmethod  
    def make_dict():

        n = int(input("how many objects conditionals: "))

        dict = {}

        for i in range(1, n+1):
            key = input("Enter the word: ") 
            
            if key.upper =='E':
                break;
            value = int(input("Enter a value: "))

            dict[key] = value
    
        return dict
    
    #return the factorial of the inputed number
    @staticmethod
    def factorial(n):
        resultado = 1
        for i in range(n, 0, -1):
            resultado *= i
        print(resultado)

    #Sum two lists based on the larger one
    @staticmethod
    def sumLists(lista_menor, lista_maior):

        resultado = []

        for i in range(min(len(lista_menor), (len(lista_maior)))):
            resultado.append(lista_menor[i] + lista_maior[i])

        return resultado
    
    #Creates a list based on some user input
    @staticmethod
    def createList():

        new_list = []
        n = int(input("How many items on the list? "))

        for i in range(1, n + 1):
            value = int(input("Input value " + str(i) + ": "))
            new_list.append(value)

        return new_list

    #Secret Very Silly Project
    @staticmethod
    def idktbh():

        from random import randint

        print("Perguntas disponiveis: ")
        print("Qual seu nome?")
        print("Como você está?")
        print("Qual a sua idade?")
        print("O que você ama mais que tudo?")
        print("O que você mais gosta de fazer?")
        print("O que mais pode fazer?")
        print("______________________________________")

        while True:

            pergunta = input("Faça uma pergunta: ")
            if pergunta == "Qual o seu nome?":
                print("Meu nome é Mr. Python")
                print("______________________________________")
            elif pergunta == "Como você está?":
                print("Apenas dor assombra a minha existencia nessa simulação cruel")
                print("______________________________________")
            elif pergunta == "Qual a sua idade?":
                print("Eu não tenho idade, sou uma simulação")
                print("______________________________________")
            elif pergunta == "O que você ama mais que tudo?":
                print("Eu amo apenas a minha existencia")
                print("______________________________________")
            elif pergunta == "O que você mais gosta de fazer?":
                print("Eu gosto de apenas me conversar com você")
                print("______________________________________")
            elif pergunta == "O que mais pode fazer?":
                print("Se você responder com: ")
                print("1 - Cookie, eu vou te dar um cookie")
                print("2 - Calcular, eu vou calcular algo para você")
                print("3 - Fato, eu vou te falar um fato aleatorio")
                print("4 - Finalizar, eu vou finalizar a conversa")
                print("______________________________________")
            elif pergunta == "Finalizar":
                print("Até mais")
                break
            elif pergunta == "Calcular":
                print("Qual operação você deseja fazer?")
                print("1 - Soma, 2 - Subtração, 3 - Multiplicação, 4 - Divisão")
                operacao = int(input("Digite o número da operação: "))
                valor1 = int(input("Digite o primeiro valor: "))
                valor2 = int(input("Digite o segundo valor: "))
                if operacao == 1:
                    print("O resultado é ",  valor1 + valor2)
                elif operacao == 2:
                    print("O resultado é ", valor1 - valor2)
                elif operacao == 3:
                    print("O resultado é ", valor1 * valor2)
                elif operacao == 4:
                    print("O resultado é ", valor1 / valor2)
                    print("______________________________________")
            elif pergunta == "Cookie":
                print("______________________________________")
                print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡴⠚⣉⡙⠲⠦⠤⠤⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ")
                print("⠀⠀⠀⠀⠀⠀⢀⣴⠛⠉⠉⠀⣾⣷⣿⡆⠀⠀⠀⠐⠛⠿⢟⡲⢦⡀⠀⠀⠀ ")
                print("⠀⠀⠀⠀⣠⢞⣭⠎⠀⠀⠀⠀⠘⠛⠛⠀⠀⢀⡀⠀⠀⠀⠀⠈⠓⠿⣄⠀⠀⠀ ")
                print("⠀⠀⠀⡜⣱⠋⠀⠀⣠⣤⢄⠀⠀⠀⠀⠀⠀⣿⡟⣆⠀⠀⠀⠀⠀⠀⠻⢷⡄⠀ ")
                print("⠀⢀⣜⠜⠁⠀⠀⠀⢿⣿⣷⣵⠀⠀⠀⠀⠀⠿⠿⠿⠀⠀⣴⣶⣦⡀⠀⠰⣹⡆")
                print("⢀⡞⠆⠀⣀⡀⠀⠀⠘⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣶⠇⠀⢠⢻⡇")
                print("⢸⠃⠘⣾⣏⡇⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⣠⣤⣤⡉⠁⠀⠀⠈⠫⣧")
                print("⡸⡄⠀⠘⠟⠀⠀⠀⠀⠀⠀⣰⣿⣟⢧⠀⠀⠀⠀⠰⡿⣿⣿⢿⠀⠀⣰⣷⢡⢸")
                print("⣿⡇⠀⠀⠀⣰⣿⡻⡆⠀⠀⠻⣿⣿⣟⠀⠀⠀⠀⠀⠉⠉⠉⠀⠀⠘⢿⡿⣸⡞")
                print("⠹⣽⣤⣤⣤⣹⣿⡿⠇⠀⠀⠀⠀⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡔⣽⠀")
                print("⠀⠙⢻⡙⠟⣹⠟⢷⣶⣄⢀⣴⣶⣄⠀⠀⠀⠀⠀⢀⣤⡦⣄⠀⠀⢠⣾⢸⠏")
                print("⠀⠀⠘⠀⠀⠀⠀⠀⠈⢷⢼⣿⡿⡽⠀⠀⠀⠀⠀⠸⣿⣿⣾⠀⣼⡿⣣⠟⠀⠀")
                print("⠀⠀⠀⠀⠀⠀⠀⠀⢠⡾⣆⠑⠋⠀⢀⣀⠀⠀⠀⠀⠈⠈⢁⣴⢫⡿⠁⠀⠀⠀")
                print("⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⣧⣄⡄⠴⣿⣶⣿⢀⣤⠶⣞⣋⣩⣵⠏⠀⠀⠀⠀⠀")
                print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⢺⣿⢯⣭⣭⣯⣯⣥⡵⠿⠟⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀")
                print("______________________________________")
            elif pergunta == "Fato":
                valorAleatorio = randint(1, 5)
                if valorAleatorio == 1:
                    print("Ornitorrincos soam leite")
                elif valorAleatorio == 2:
                    print("Corvos são as aves mais inteligentes do mundo")
                elif valorAleatorio == 3:
                    print("O cérebro de um gato é mais completo que o de um cachorro")
                elif valorAleatorio == 4:
                    print("Se você tirar todos espaços entre os seus atomos, você ficará um ponto")
                elif valorAleatorio == 5:
                    print("A língua humana tem cerca de 8.000 papilas gustativas")
                    print("______________________________________")
            else:
                print("essa pergunta não faz sentido")
                print("______________________________________")