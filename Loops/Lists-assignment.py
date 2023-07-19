#Homework Assignment #5: Basic Loops

#Solution for creating a number btn 1 and 100 
for number in range(1,101):
    if number % 15 == 0:
        print("FizzBuzz")
    elif number % 5 == 0:
        print("Buzz")
    elif number % 3 == 0:
        print("Fizz")
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                break
            else:
                print("prime")
