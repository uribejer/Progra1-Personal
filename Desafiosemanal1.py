import random

def mostrar_matriz(matriz_calificaciones, n, m):
    # Encabezado de MATERIAS
    print(" "*14, end="")
    for j in range(1, m+ 1):
        print(" "*4, "Materia", j, end="")
    print()

    # Encabezados de ESTUDIANTES
    i = 0
    for fila in (matriz_calificaciones):
        print("Estudiante: ", (i + 1), end="")
        for calificacion in fila:
            print(" "*10, calificacion, end=" ")
        print()
        i = i + 1

def promedio_calificaciones(matriz_calificaciones):
    i = 0
    for fila in matriz_calificaciones:
        suma = 0
        j = 0
        while j < len(fila):
            suma += fila[j]
            j = j + 1
        promedio = suma / len(fila)
        print("El promedio de calificaciones del Estudiante: ", (i + 1), " es: ", (promedio))
        i += 1

def calcular_promedio_materias(matriz_calificaciones):
    num_materias = len(matriz_calificaciones[0])
    for j in range(num_materias):
        suma = 0
        for fila in matriz_calificaciones:
            suma = suma + fila[j]
        promedio = suma / len(matriz_calificaciones)
        print("El promedio de calificaciones en la Materia", (j + 1), " es: ", (promedio))


# Definir el número de estudiantes y materias
n = int(input("Ingrese el nro de estudiantes: "))  # seria nuestra cantidad de filas
m = int(input("Ingrese el nro de materias: "))     # seria nuestra cantidad de columnas

matriz_calificaciones = []

# Llenar la matriz con calificaciones aleatorias 
for x in range(n):
    calificaciones_estudiante = []
    for y in range(m):
        calificacion = random.randint(1, 10)
        calificaciones_estudiante.append(calificacion)
    matriz_calificaciones.append(calificaciones_estudiante)

# Mostrar la matriz con encabezados
mostrar_matriz(matriz_calificaciones, n, m)
print()
print("PROMEDIO CALIFCIACIONES PARA CADA ESTUDIANTE")
# Imprimir los promedios de calificaciones por estudiante
print()
promedio_calificaciones(matriz_calificaciones)
print()
print("PROMEDIO CALIFCIACIONES PARA CADA MATERIA")
print()
# Calcular y mostrar los promedios de calificaciones por materia
calcular_promedio_materias(matriz_calificaciones)