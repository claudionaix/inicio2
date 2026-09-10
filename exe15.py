#lendo os valores de entrada
salario_atual = float(input("valor do salário (R$): "))
reajuste = float(input("reajuste salarial em (%): "))

#calculando o valor
aumento = salario_atual * (reajuste / 100)
novo_salario = salario_atual + aumento

#exibindo os resultados
print ("valor do aumento", aumento)
print ("novo salario", novo_salario)