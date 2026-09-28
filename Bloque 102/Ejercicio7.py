#Introducir segundos.
s = int(input("Ingresar segundos a calcular a h,min,s: "))

#calcular h, min,s.
h = s // 3600
min = s % 3600 // 60
seg = s % 3600 % 60

#mostrar h, min, s.

print(f"{s}segundos son {h} horas {min} minutos y {seg} segundos")