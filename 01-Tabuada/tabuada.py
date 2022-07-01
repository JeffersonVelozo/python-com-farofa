numero = int(input("Digite um número para saber a sua tabuada: "))

for i in range(11):
    r = numero * i
    print(str(numero) + " x " + str(i) + " = " + str(r))