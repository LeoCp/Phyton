##########################################################
# questao002.py
#
# Leo Cp
#
# Programa para calcular a redução do tempo de vida de um 
# fumante. 
# Pergunte a quantidade de cigarros fumados por dia e 
# quantos anos ele já fumou. Considere que um fumante 
# perde 10 minutos de vida a cada cigarro, calcule 
# quantos dias de vida um fumante perderá. Exiba o 
# total de dias.
##########################################################
import os

print("--------------------------------------------------------------------------------");
print("                                Programa                                        ")
print("--------------------------------------------------------------------------------");

## perde10minuto -------- cadacigarro
##    x          ---------  a
quantDias = int(input("Qual é a quantidade de cigarros que você fuma por dia: "))

a = quantDias * 10 ## a = Quantos minutos perde em 1dia

quantAnos = int(input("Há quandos anos você fuma: "))

b = quantAnos * 365 ## b = quantos dias que ele fumou nesses anos

c = b * a ##Quannto minutos ele perde nos anos

d = c / 1440 ##Quantos dias ele perde


os.system("cls")
print("--------------------------------------------------------------------------------");
print("                                Relatório                                       ")
print("--------------------------------------------------------------------------------");


print("O total de dias que voce perdeu %d " %d)

os.system("pause")