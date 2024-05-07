nombres = ['Juan', 'José', 'Luis', 'Carlos', 'Alejandro', 'Miguel', 'Javier', 'Fernando', 'Andrés', 'Diego', 'Pedro', 'Daniel', 'Pablo', 'Santiago', 'Manuel', 'Ricardo', 'Gabriel', 'Héctor', 'Francisco', 'Jorge', 'Eduardo', 'Mario', 'Roberto', 'Alberto', 'Gonzalo' , 'María', 'Laura', 'Ana', 'Luz', 'Patricia', 'Elena', 'Sofía', 'Isabel', 'Carmen', 'Gabriela', 'Verónica', 'Claudia', 'Daniela', 'Adriana', 'Fabiola', 'Victoria', 'Natalia', 'Mónica', 'Alejandra', 'Silvia', 'Diana', 'Fernanda', 'Paula', 'Rosa', 'Estela']
nombres_lugares = ['Corcovado', 'Arenal', 'Tortuguero', 'Monteverde', 'Rincón de la Vieja', 'Manuel Antonio', 'Poás', 'Talamanca', 'Cahuita', 'Turrialba', 'Barva', 'Chirripó', 'Irazú', 'Tenorio', 'Pacuare', 'Celeste', 'Barú', 'Gandoca', 'Río Celeste', 'Osa', 'Cocos', 'Cerro Chato', 'Carara', 'Ara', 'Rincón de Osa', 'Miravalles', 'Río Pacuare', 'Savegre', 'Tortuguero', 'Naranjo', 'Carrillo', 'Negro', 'Aguilar', 'Fortuna', 'Veragua', 'Barreal', 'Rivas', 'Frijolar', 'Madre Selva', 'Sirena', 'Madrigal', 'Veragua', 'Rodeo', 'Cedral', 'Cedralito', 'Esperanza', 'Boca Tapada']
apellidos = ['González', 'Rodríguez', 'Gómez', 'Fernández', 'López', 'Díaz', 'Martínez', 'Pérez', 'García', 'Sánchez', 'Romero', 'Suárez', 'Torres', 'Rivera', 'Domínguez', 'Vásquez', 'Castillo', 'Rojas', 'Morales', 'Ortega', 'Gutiérrez', 'Reyes', 'Ramírez', 'Jiménez', 'Hernández', 'Álvarez', 'Moreno', 'Muñoz', 'Alonso', 'Silva', 'Valenzuela', 'Medina', 'Ramos', 'Paz', 'Benítez', 'Herrera', 'Aguilar', 'Mendoza', 'Guerrero', 'Flores', 'Pereira', 'Cabrera', 'Chávez', 'Campos', 'Ortiz', 'Vega', 'León', 'Pardo', 'Cortés']
lugares_naturales = ['Parque', 'Reserva', 'Bosque', 'Selva', 'Montaña', 'Cañón', 'Playa', 'Isla', 'Volcán', 'Parque Nacional', 'Reserva Natural', 'Bosque Nativo', 'Área Protegida', 'Santuario de Fauna y Flora', 'Refugio de Vida Silvestre', 'Área Silvestre Protegida', 'Humedal', 'Selva Virgen', 'Zona de Conservación', 'Biodiversidad', 'Área de Preservación Ambiental', 'Zona de Reserva', 'Zona de Vida Silvestre', 'Área de Conservación', 'Área de Importancia Ecológica', 'Área Natural Protegida', 'Parque Ecológico', 'Corredor Biológico', 'Zona de Reserva Forestal', 'Área de Vida Silvestre', 'Reserva de la Biosfera', 'Área de Protección de Flora y Fauna', 'Zona de Bosque Primario', 'Parque Natural Regional', 'Área de Regeneración Natural', 'Reserva de Recursos Naturales', 'Área de Bosque Virgen', 'Área de Restauración Ecológica', 'Área de Fauna Silvestre', 'Refugio de Biodiversidad', 'Hábitat Natural', 'Santuario de la Naturaleza', 'Área de Conservación de la Biodiversidad', 'Reserva Indígena', 'Área de Bosque Nativo', 'Área de Especies en Peligro', 'Área de Protección de Ecosistemas', 'Área de Bosque Tropical', 'Área de Protección de Recursos Naturales', 'Reserva Forestal Integral', 'Zona de Selva Protegida', 'Refugio de Aves', 'Reserva Marina', 'Área de Bosque Subtropical', 'Área de Recuperación Ambiental', 'Parque Natural Urbano']


errores = {
        'Error1':'El tipo de entrada es incorrecto',
        'Error2':'La entrada no es un número!',
        'Error3':'La entrada no está en el rango.'
          }

def convertir_a_entero(arr):
    '''
    Entrada: Debe ser una cadena.
    Salida: Debe ser un número o un error.
    Restricciones: La entrada debe ser únicamente una cadena, la cadena no debe ser vacía.
    '''
    if type(arr) != str:
        return "Error 01 | La entrada debe ser una cadena"
    elif arr == "":
        return -1
    else:
        return convertir_a_entero_aux(arr, 0, 0)

def convertir_a_entero_aux(arr, idx, resultado):
    '''
    Función auxiliar de convertir_a_entero
    '''
    if idx == len(arr):
        return resultado
    else:
        if arr[idx] >= '0' and arr[idx] <= '9':
            resultado = resultado * 10 + int(arr[idx])
            return convertir_a_entero_aux(arr, idx + 1, resultado)
        else:
            return -1

def generar_nombres(caso):

    global errores
    global nombres
    global nombres_lugares
    global apellidos
    global lugares_naturales

    '''
    nota importante: Santa """""ROSA""""" no es el nombre de una persona.
    Descricpión: Está función va a generar un nombre compuesto de dos partes.
    E: El tipo de caso del nombre.
    S: Un nombre
    R: el caso debe de ser un número entre las opciones

    Funciones dependientes: generar_nombres_aux.
    '''

    if type(caso) != int:
        return f"Error1 | {errores['Error1']}"

    elif caso < 0 or caso > 1:
        return f"Error3 | {errores['Error3']}"

    else:
        if caso == 1:
            return intercalar_listas(lugares_naturales, nombres_lugares)
        else:
            return intercalar_listas(nombres, apellidos)

def intercalar_elemento(elemento, lista):
    
    #E: elemento a intercalar y una lista con la cual intercalarlo
    #S: lista de listas con el elemento a intercalar y cada uno de los elementos de la lista
    #R: la lista debe ser una lista
    
    if type(lista)!=list:
        return 'Error 01: la entrada debe ser una lista'
    
    else:
        return intercalar_elemento_aux(elemento, lista, 0, len(lista), [])
    
def intercalar_elemento_aux(elemento, lista, indice, fin, salida):
    
    #Funcion auxiliar
    
    if indice==fin:
        return salida
    
    else:
        return intercalar_elemento_aux(elemento, lista, indice+1, fin, salida+[[elemento + " " + lista[indice]]])

def intercalar_listas(lista1, lista2):
    
    #E: dos listas a intercalar
    #S: una lista de listas donde hay un elemento de cada lista para cada elemento de cada lista
    #R: ambas entradas sean listas
    
    if type(lista1)!=list:
        return 'Error 01: la entrada no es una lista'
    
    elif type(lista2)!=list:
        return 'Error 02: la entrada no es una lista'
    
    else: 
        return intercalar_listas_aux(lista1, lista2, 0, len(lista1), [])
    
def intercalar_listas_aux(lista1, lista2, indice, fin, salida):
    
    #Funcion auxiliar de intercalar
    
    if indice==fin:
        return salida
    
    else:
        return intercalar_listas_aux(lista1, lista2, indice+1, fin, salida + intercalar_elemento(lista1[indice],lista2))
