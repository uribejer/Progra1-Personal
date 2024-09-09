def agregar_libros (tabla, cant_datos_agregar):
    i = 1
    for i in range (cant_datos_agregar):
        seccion = []
        ID = int(input("Ingrese el ID:"))
        seccion.append(ID)
        nombre = (input("Ingrese el titulo del libro:"))
        seccion.append(nombre)
        descripcion = (input("Ingrese la descripcion del libro:"))
        seccion.append(descripcion)
        precio = int(input("Ingrese el precio de libro:"))
        seccion.append(precio)
        
        tabla.append(seccion)  
    return tabla
        
def conversion_datos (tabla_actualizada):
    for libro in tabla_actualizada:
        for dato in libro:
            if dato == libro[1]:
                libro[1] = dato.upper()        
    return tabla_actualizada

def recortar_datos(tabla_actualizada):
    cant_caracteres = 0
    for libro in tabla_actualizada:
        for dato in libro:
            if dato == libro[2]:
                largo_caracteres = len(dato)
                descripcion = libro[2]
                if largo_caracteres > 20:
                    libro[2] = descripcion[:10]
    return tabla_actualizada

def eliminar_dato(tabla_actualizada):
    for libro in tabla_actualizada:
        print(f"{libro[0]:<10}, {libro[1]}, {libro[2]:>30}, {libro[3]:>23}")
    cuantos_libros_eliminar = int(input("Cuanto libros quiere eliminar? "))
    while cuantos_libros_eliminar > 0:
        libro_a_eliminar = int(input("Que libro quiere eliminar (ingrese su ID)? "))
        for libro in tabla_actualizada:
            if libro[0] == libro_a_eliminar:
                tabla_actualizada.remove(libro)
                cuantos_libros_eliminar = cuantos_libros_eliminar -1
                print(f"El libro con ID {libro_a_eliminar} fue eliminado")
    return  tabla_actualizada
         
tabla = [
    [2, 'El Alquimista','Muy buen libro', 88.5],
    [4, 'El Principito', 'Libro de descente', 92.0],
    [5, 'Un mundo feliz','Espectacular', 85.0],
    [1, 'A sangre fría', 'Libro increible', 90.5],
    [9, 'Los Miserables','Libro mediocre', 87.0], 
    [10, 'Don Quijote', 'Particular', 87.0]  
]

cant_datos_agregar = int(input("Cuantos libros quiere agregar? "))

tabla_actualizada = agregar_libros (tabla, cant_datos_agregar)

tabla_actualizada = conversion_datos(tabla_actualizada)

tabla_actualizada = recortar_datos(tabla_actualizada)

tabla_actualizada = eliminar_dato(tabla_actualizada)

tabla_ordenada = sorted(tabla_actualizada, key=lambda libro: (libro[0], -libro[3]))

# Imprimir encabezado con formato de f-strings
print(f"{'ID':<14} {'TITULO':<30} {'DESCRIPCION':<30} {'PROMEDIO':>7}")
print('-' * 96)

for libro in tabla_ordenada:
    print(f"{libro[0]:<10}, {libro[1]}, {libro[2]:>30}, {libro[3]:>23}")
   