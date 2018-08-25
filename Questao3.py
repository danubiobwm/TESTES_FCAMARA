numero_horas_trabalhadas=int(input("Horas trabalhadas: "))
Salario=int(input("Salario Minimo: "))

valor_hora=Salario*10/100
salarioBruto=(numero_horas_trabalhadas*valor_hora)
salario_total=salarioBruto+valor_hora*3/10;

print("Salário a Receber: ", salario_total)