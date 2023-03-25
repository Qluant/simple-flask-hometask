operations = "-+*:"



def factor(number: int = 1, count: int = 1):
    for i in range(1, count+1):
        number *= i
    return number