import Exercises.FizzBuzz as fb
import Exercises.Factorial as fc
import Exercises.SumLists as sl

while True:
    letra = input("Choose the function: Factorial[F] || FizzBuzz[B] || sumLists[S]: ")[0].upper()

    match letra:
        case "F":
            n = int(input("Input a number: "))
            fc.factorial(n)
        case "B":
            my_dict = fc.make_dict()
            n = int(input("Input how many iterations: "))
            fb.fizzbuzz(n, my_dict)
        case "S":
            print("First List: ")
            first_list = sl.createList()
            print("Second List: ")
            seccond_list = sl.createList()
            print(sl.sumLists(first_list, seccond_list))