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