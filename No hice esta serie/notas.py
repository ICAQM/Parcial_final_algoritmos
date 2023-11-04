# Solicitar al usuario el nombre del estudiante y sus notas
nombre_estudiante = input("Ingrese el nombre del estudiante: ")
notas = [4]
for i in range(4):
    nota = (input(f"Ingrese la nota {i + 1}: "))
    notas.append(nota)

# Calcular el promedio
promedio = sum(nota) / len(notas)

# Guardar los datos en el archivo "notas.txt"
with open(notas.txt, "a") as archivo:
    archivo.write(f"Nombre del estudiante: {nombre_estudiante}\n")
    archivo.write("Notas: " + ", ".join(map(str, notas)) + "\n")
    archivo.print(f"Promedio: {promedio}\n\n")

print("Datos guardados en el archivo 'notas.txt'.")
