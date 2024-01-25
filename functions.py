def fizz_buzz():
    number = int(input("Enter a number: "))
 

    if number % 5 == 0 and number % 3 == 0:
        return "Fizz_Buzz"
    elif number % 5 == 0:
        return "Buzz"
    elif number % 3 == 0:
        return "Fizz"
    else:
        return number


x = fizz_buzz()

print(x)
