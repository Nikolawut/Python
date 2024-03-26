num = int(input())
first = num // 10
second = num % 10

if first > second:
    print("Razlika prve i druge cifre je:", first - second)
elif first < second:
    print("Zbir prve i druge cifre je:", first + second)
else:
    print("Proizvod prve i druge cifre je:", first * second)