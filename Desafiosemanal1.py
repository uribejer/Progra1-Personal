import random

def imprimir_matriz_calificaciones(matriz_calificaciones):
    cont = 0
    for fila in matriz_calificaciones:
        cont = cont + 1
        print("Estudiante ", cont)
        print(fila)

def promedio_calificaciones(matriz_calificaciones):
    cont = 0
    for fila in matriz_calificaciones:
        cont = cont + 1
        suma = 0
        for calificacion in fila:
            suma = suma + calificacion
        promedio = suma / len(fila)
        print("El promedio de calificaciones del estudiante ", cont, " es: ", promedio)

# Definir el número de estudiantes y materias
num_estudiantes = 5 # cantidad de filas
num_materias = 3 # cantidad de columnas
matriz_calificaciones = []
# Aca llenamos la matriz con calificaciones aleatroias
for x in range(num_estudiantes):
# Creamos una lista vacia para las calificaciones de los estudiantes
    calificaciones_estudiante = []

# Agregamos las calificaciones aleatorias para cada materia
for y in range(num_materias):
	calificacion = random.randint(1, 10)
	calificaciones_estudiante.append(calificacion)


# A las calificaciones a la matriz de estudiantes
matriz_calificaciones.append(calificaciones_estudiante)
imprimir_matriz_calificaciones(matriz_calificaciones)
promedio_calificaciones(matriz_calificaciones)
# Aca se imprimirian las calificaciones