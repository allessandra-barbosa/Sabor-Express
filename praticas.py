"""

print('# Exercicios modulo 01')

print('1. Python na Escola de Programação da Alura')


nome = 'Alessandra'
idade = '23'
print(f'2. Meu nome é {nome} e tenho {idade} anos')


print('''3. 
    A
    L
    U
    R
    A''')


pi = 3.14159
print(f'4. O valor arredondado de pi é: {pi:.2f}')


#------------------------------------------------------


print('# Exercicios modulo 02')

num_digitado = int(input('1. Digite um número: '))

if num_digitado % 2 == 0:
    print('O número digitado é par')
else:
    print('O número digitado é impar')


idade = int(input('Digite sua idade: '))

if idade >= 0 <= 12:
    print('Sua categoria é criança')
elif 12 < idade < 18:
    print('Sua categoria é adolecente')
else:
    print('Sua categoria é adulto')

"""

#------------------------------------------------------


print('# Exercicios modulo 02\n')

print('1. Crie uma lista\n')
lista_de_num = [1,2,3,4,5,6,7,8,9,10]
lista_de_nomes = ['maria','jose','marcio','marcia']
lista_ano = [2000, 2024]

print('2. Percorra a lista')
for numero in lista_de_num:
    print(numero)
    print()

print('3. Soma números ímpares')
soma_impares = 0
for i in range(1, 11, 2):
    soma_impares += i
print(soma_impares)
print()

print('4. Números de 1 a 10 em ordem decrescente')
for i in range(10, 0, -1):
    print(i)
    print()

print('5. Tabuada interativa')
numero_tabuada = int(input('Digite um número para a tabuada: '))
for i in range(1, 11):
    resultado = numero_tabuada * i
    print(f'{numero_tabuada} x {i} = {resultado}')
    print()

print('6. Soma de elementos')
lista_numeros = [10, 5, 8, 3, 7]
soma = 0

try:
    for numero in lista_numeros:
        soma += numero
    print(f'Soma dos elementos: {soma}')
except Exception as e:
    print(f'Ocorreu um erro: {e}')
    print()

print('7. Validação de lista vazia')
lista_valores = [15, 20, 25, 30]
soma_valores = 0

try:
    for valor in lista_valores:
        soma_valores += valor
    media = soma_valores / len(lista_valores)
    print(f'Média dos valores: {media}')
except ZeroDivisionError:
    print('A lista está vazia, não é possível calcular a média')
except Exception as e:
    print(f'Ocorreu um erro:{e}')