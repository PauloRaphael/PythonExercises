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