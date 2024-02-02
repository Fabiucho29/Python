# Fabio Carrozza. C.I: 30714977.  Carnet: 20241110142

# Input
DD = str(67.23)

# Separar el input
entera, decimal = DD.split(".")

# Se empieza a convertir el input
grados = int(entera)

# Se trabaja con la parte decimal
x = int(decimal) / 100

# se convierte a minutos
y = str(x * 60)

minutos, resto = y.split(".")

# Se trabaja con los segundos
resto = int(resto) / 10

segundos = round((resto * 60))

# Se unen todos los valores para expresar el valor final
DMS = str(grados) + "°" + str(minutos) + "'" + str(segundos) + '"'

# Se expresa la respuesta
print(f"{DD} a grados, minutos, segundos es igual a {DMS}")