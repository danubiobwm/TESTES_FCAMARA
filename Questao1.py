

ano = 2005
salario = 1000
ano_atual = 2007
percentual = 1.5
novo_salario = salario + (salario * percentual) / 100

for ano in range(ano_atual):
    percentual = 2 * percentual
    novo_salario = novo_salario + (novo_salario * percentual) / 100
    print("Seu novo salario: ",novo_salario)
    break


