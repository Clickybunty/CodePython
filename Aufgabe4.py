import random

def RandomFunc():
    RandNumber=(random.randint(1, 10))
    return RandNumber

def sum_of_squares(n):
    i = 0
    Summ = 0
    List = []    
    while i < n:
        List.append(int(i) + 1)
        i=i+1
          
    for i in List:
        Quadrat = i * i
        Summ += Quadrat
    return Summ

n = RandomFunc()
Sum = sum_of_squares(n)
print(f"Die Summe der Quadrate der ersten {n} natürlichen Zahlen ist: {Sum}")