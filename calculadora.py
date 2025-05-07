#Menu
print("-----------Tabela de Operações------------")
print("1 - Somar")
print("2 - Subtrair")
print("3 - Multiplicar")
print("4 - Dividir")
print("--------------------------------------------")

#entrada de um dos valores do menu
escolha = int(input('Escolha uma das operações: '))

#Repete o código enquanto a escolha for menor que 1, ou maior que 4
while escolha < 1 or escolha > 4:
    print("Valor invalido")
    escolha = int(input('Escolha uma das operações: '))

#Valores a calcular
valor1 = int(input('Digite um valor: '))
valor2 = int(input('Digite outro valor: '))


#Trata divisão por zero
while valor2 == 0 and escolha == 4:
    print('Não é possivel pazer divisão por zero, por favor, digite outro valor.')
    valor2 = int(input('Digite outro valor diferente de zero: '))

#Operações
soma = valor1 + valor2
sub = valor1 - valor2
mul = valor1 * valor2
div = valor1 / valor2


#Condições para cada valor
if escolha == 1:
    print('{} + {} = {}'.format(valor1, valor2, soma))
elif escolha == 2:
    print('{} - {} = {}'.format(valor1, valor2, sub))
elif escolha == 3:
    print('{} * {} = {}'.format(valor1, valor2, mul))
elif escolha == 4:
    print('{} / {} = {}'.format(valor1, valor2, div))




