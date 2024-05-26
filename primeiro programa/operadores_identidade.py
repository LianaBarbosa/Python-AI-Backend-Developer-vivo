# is-usado para saber se ocupam a mesma posição e memória
curso = "curso de python"
nome_curso = curso
saldo, limite = 200, 200

curso is nome_curso

curso is not nome_curso

saldo is limite

saldo = 1000
limite = 500

print(saldo is limite)
print(saldo is not limite)
