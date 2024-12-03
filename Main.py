import Functions as fc

while True:
    letra = input("Choose the function: Factorial[F] || FizzBuzz[B] || sumLists[S]: ")[0].upper()

    match letra:
        case "F":
            n = int(input("Input a number: "))
            fc.factorial(n)
        case "B":
            my_dict = fc.make_dict()
            n = int(input("Input how many iterations: "))
            fc.fizzbuzz(n, my_dict)
        case "S":
            print("First List: ")
            first_list = fc.createList()
            print("Second List: ")
            seccond_list = fc.createList()
            print(fc.sumLists(first_list, seccond_list))