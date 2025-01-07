
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