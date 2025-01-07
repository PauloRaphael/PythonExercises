# Python Exercises 🐍

This is a small collection of Python exercises I've completed, suggested by friends and coworkers. Here, I aimed to reinforce my knowledge of Python's syntax and nuances, as well as practice basic logic and simple algorithms.  

Each exercise is designed to address a specific concept, making this collection a handy resource for learning and reviewing Python.

## 🚀 Exercises

### FizzBuzz 🔢

> “FizzBuzz is a common coding task given during interviews that tasks candidates to write a solution that prints integers one-to-N, labeling any integers divisible by three as “Fizz,” integers divisible by five as “Buzz,” and integers divisible by both three and five as “FizzBuzz.””  
> — [Builtin](https://builtin.com/software-engineering-perspectives/fizzbuzz)

In my solution, I added a twist by implementing a **`Create_Dict`** function. This function generates a dictionary that maps words to divisors, making the challenge more complex and scalable.  

📂 **You can check my solution here:** [Exercises/FizzBuzz.py](Exercises/FizzBuzz.py)

---

### Factorial 🧮

This is a straightforward exercise: code a function that returns the factorial of any given number.  

I recommend solving this using recursion to explore how functions can call themselves and simplify logic.  

📂 **You can check my solution here:** [Exercises/Factorial.py](Exercises/Factorial.py)

---

### SumLists ➕

This exercise involves creating a function that takes two lists as input and sums their values, element by element, based on the size of the larger list. It also appends any remaining values from the longer list to the result.  

#### Example:

```python
ListA = [5, 6, 9]
ListB = [2, 4, 6, 9]

ListC = SumLists(ListA, ListB)  
# ListC = [6, 10, 15, 9]
```

The function handles mismatched list sizes gracefully, ensuring no values are lost. 

In my solution i also created a function that returns a list based on user input, this could be a way to improve the dificulty of the challenge and make it more fun :)

📂 **You can check my solution here:** [Exercises/SumLists.py](Exercises/SumLists.py)

---

## 💡 How to Use

This repository includes a **command-line menu** in the `Main.py` file that allows you to select which exercise to run.

### Steps to Use:

1. **Clone the repository**:  
   ```bash
   git clone https://github.com/PauloRaphael/PythonExercises.git
   cd PythonExercises
   ```

2. **Run the menu**:  
   Execute the following command to launch the menu:  
   ```bash
   python Main.py
   ```

3. **Select an exercise**:  
   Follow the on-screen prompts to choose an exercise to execute.

### Alternative:

You can also open the project directory in your preferred IDE and run the `Main.py` file directly.

---

## 🤝 Contributions

This is a personal project, but I'm open to suggestions! Feel free to create issues or submit pull requests if you have ideas for new exercises or improvements.

---

Enjoy exploring the code, and happy learning! 🚀
