

x = [2, 4, 5, 6, 7, 8, 9, 10, 11 ,12]

def square(array):
    y =[]
    for i in array:
        y.append(i**2)
    return y




def filterOddNumbers(array):
    y = []
    for i in array:
        if i%2 == 0:
            y.append(i)

    return y
 


def sumOfArray(array):
    y = 0
    for i in array:
        y += i
    return y 


print(sumOfArray(x))
