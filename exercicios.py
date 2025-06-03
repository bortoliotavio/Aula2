import math


# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.

# numero_1 = int(input("Insira um numero inteiro: "))
# numero_2 = int(input("Insira outro numero inteiro: "))
# resultado = numero_1 + numero_2
# print(f"A soma dos dois numeros é: {resultado}")

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.

# numero = int(input("Insira um digito para que ele possa ser utilizado de exemplo:"))
# total = numero % 5

# print(f"O restante da divisão do numero inserido por 5 é igual: {total}")

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.

# numero_1 = int(input("Insira o primeiro numero da multiplicação: "))
# numero_2 = int(input("Insira o segundo numero da multiplicação: "))
# total = numero_1 * numero_2

# print(f"O total da multiplicação é de: {total}")

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

# numero_1 = int(input("Insira o primeiro numero para a divisão: "))
# numero_2 = int(input("Insira o outro numero para a divisão: "))
# total = numero_1 // numero_2

# print(f"O total da inteiro da divisão é igual a: {total}")

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

# numero = int(input("Insira o numero para a potencia ao quadrado: "))
# total = numero ** 2

# print(f"O total do numero inserido ao quadrado é: {total}")

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.

# numero_1 = float(input("Insira o primeiro valor(pode decimal): "))
# numero_2 = float(input("Insira o segundo valor(pode decimal): "))
# total = numero_1 + numero_2

# print(f"O total da soma é igual a: {total}")


# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.

# numero_1 = float(input("Insira o primeiro valor(pode decimal): "))
# numero_2 = float(input("Insira o segundo valor(pode decimal): "))
# total = numero_1 / numero_2

# print(f"A media é igual a: {total}")

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).

# numero_1 = float(input("Insira o primeiro valor(pode decimal): "))
# numero_2 = float(input("Insira o valor que deseja colocar a potencia no primeiro valor(pode decimal): "))
# total = numero_1 ** numero_2

# print(f"A potencia de {numero_1} a {numero_2} é igual a: {total}")

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.

# temperatura_c = float(input("Insira a temperatura em Celsius: "))
# temperatura_f = (temperatura_c * 9/5) + 32

# print(f"A temperatura em Fahrenheit é igual a: {temperatura_f}")

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

# raio = float(input("Insira o raio do círculo para calcular a área: "))
# area = math.pi * raio ** 2

# print(f"A área do círculo é igual á: {area}")

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.

# string = input("Digite uma palavra ou frase para ser convertida para maiuscula: ")
# stringupper = string.upper()

# print(f"e assim ficou a string maiuscula: {stringupper}")


# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.

# string = input("Digite seu nome completo: ")
# stringlower = string.lower()

# print(f"Seu nome completo minusculo: {stringlower}")

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.

# string = input("Digite seu nome completo: ")
# string_limpa = string.strip()

# print(f"Sua frase limpa ficaria:{string_limpa}")

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.

# data = input("Digite uma data no seguinte formato 'dd/mm/aaaa': ")
# data_lista = data.split("/")

# print(f"Você digitou dia: {data_lista[0]} do mes: {data_lista[1]} do ano: {data_lista[2]}")
 
# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.

# string_1 = input("Digite a primeira parte da frase para concatenação: ")
# string_2 = input("Digite a segunda parte da frase para concatenação: ")

# concatenada = string_1 + string_2

# print(f"sua string concatenada fica assim: {concatenada}")

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.


# bool_1 = True
# bool_2 = True

# result = bool_1 and bool_2

# print("O resultado da expressão logica AND é igual: ", result)


# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.

# bool_1 = True
# bool_2 = True
# result = bool_1 or bool_2

# print("O resultado da expressão logica OR é igual: ", result)

# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.

# bool_1 = True
# result = not bool_1

# print("O resultado da expressão logica not é igual: ", result)

# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.

# numero_1 = float(input("Insira o primeiro valor(pode decimal): "))
# numero_2 = float(input("Insira o valor que deseja confirmar se é igual o primeiro: "))
# resultado = (numero_1 == numero_2)

# print("O resultado da expressão logica equal é igual: ", result)


# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

# numero_1 = float(input("Insira o primeiro valor(pode decimal): "))
# numero_2 = float(input("Insira o valor que deseja confirmar se não é igual o primeiro: "))
# resultado = (numero_1 != numero_2)

# print("O resultado da expressão logica not equal é igual: ", result)

# #### try-except e if

# 21: Conversor de Temperatura
# 22: Verificador de Palíndromo
# 23: Calculadora Simples
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação

