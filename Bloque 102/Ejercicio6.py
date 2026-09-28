#pedir salario bruto.
salario_bruto = float(input("Salario Buto: "))
IRPF = int(input("Introducir IRPF: "))
#calcular salario
salario_neto = salario_bruto - (salario_bruto * IRPF / 100)
#mostrar salario
print(f"El salario neto es {salario_neto}")