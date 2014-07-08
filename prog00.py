
########################################################
# prog00.py
#
# Leo Cp
#
# Programa que pede dois números inteiros e imprime 
# a soma desses dois números
#######################################################
import os

print("--------------------------------------------------------------------------------");
print("                                Programa00                                      ")
print("--------------------------------------------------------------------------------");


num1 = int(input("Digite o primeiro numero: ")) 
num2 = int(input("Digite o segundo numero:  "))

soma = num1 + num2

os.system("cls")
print("--------------------------------------------------------------------------------");
print("                                Relatório                                       ")
print("--------------------------------------------------------------------------------");


print ("A soma é: %d " %soma)
print("\n")
os.system("pause")

