#operadores lógicos
#comparação logica alternandocom de comparação

saldo = 1000
saque = 200
limite = 100

# and (e) todas devem ser verdadeiras
saldo >= saque and saque <= limite



#or (ou) uma só tem que ser verdadeira
saldo >= saque and saque <= limite

#negação, not falso é true,
not 1000>1500
#() do mesmo jeito que os aritmeticos precedencia tambem se aplica em str
saldo =1000
saque = 250
limite = 200
conta_especial = True

exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
#true

#este é mais compreensivel
exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque )
#true

conta_normal_com_saldo_suficiente = (saldo >= saque and saque <= limite)
conta_especial_com_saldo_suficiente = (conta_especial and saldo >= saque)

exp_3 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print(f"exp_3 {exp_3}")
# and tudo tem que ser true pra dar true
print(True and True)
print(True and False)
print(False and False)

# or basta um ser true para dar true
print(True or True)
print(True or False)
print(False or False)



