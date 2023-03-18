num  = 1
cuentas = {}
while num < 11:
    nombreCuenta = input("Ingrese el nombre de la cuenta numero " + str(num)+ " ")
    cuentas[nombreCuenta] = int(input("Ingrese el saldo de la cuenta numero " + str(num)+ " "))
    num += 1
    
cuentas = dict(sorted(cuentas.items(), key=lambda x: x[1], reverse=True))

for cuenta in cuentas:
    print(str(cuenta) + " = " + str(cuentas[cuenta]))
