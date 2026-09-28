#Pedir coeficientes a·x² + b·x + c = 0.
print("para calcular a·x² + b·x + c = 0 debe ingresar:")
a = float(input("Ingresar valor para a: "))
b = float(input("Ingresar valor para b: "))
c = float(input("Ingresar valor para c: "))
#Calcular a·x² + b·x + c = 0.
r1 = (-b + (b**2 -4 * a * c)** (1/2)) / 2*a
r2 = (-b - (b**2 -4 * a * c)** (1/2)) / 2*a
r3 = c / b
#Mostrar resultado a·x² + b·x + c = 0.
print(f"al ser una ecuación de segundo grado tiene 2 resultados si es más x = {r1} pero si es menos x = {r2} pero si a es 0 entonces {r3}")