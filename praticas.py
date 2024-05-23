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