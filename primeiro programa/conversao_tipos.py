#conversão de variaveis exemplo int para float:
preco = 10
print(preco)

preco = float(preco)
print(preco)

preco = 10/2
print( preco)


#float para int
preco=10.30
print(preco)

preco = int(preco)
print(preco)

#conversão por divisão
preco = 10
print(preco)
#gera float
print(preco/2)
#divisão de numero inteiro com outro numero inteiro com // gera um int
print(preco//2)

#numero para string
preco= 10.50
idade = 28
# o str construtor passe para o construtor o valor que quer que converta (formula geral)
print(str(preco))
print(str(idade))

#concatenar string com variaveis
texto = f"idade: {idade} preco {preco}"
print(texto)

#formula geral de string para num

preco ="10.50"
idade = 28

print(float(preco))
print(int(idade))

# nem sempre isso é válido exemplo texto para float
#preco = python
#print(float(preco))

#exercicios
print(int(1.9))

print(int(2.97348728))

print(int("10"))
print(float(10.10))
print(float(100))

#type pergunta
valor = 10
valor_str = str(valor)
print(type(str(10.10)))

#deu float
print(100/2)

#deu int // retorne ineiro sem ponto flutuante
print(100//2)
