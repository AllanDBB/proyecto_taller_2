import math, random, copy

# Variables globales
nombres = ['Juan', 'José', 'Luis', 'Carlos', 'Alejandro', 'Miguel', 'Javier', 'Fernando', 'Andrés', 'Diego', 'Pedro', 'Daniel', 'Pablo', 'Santiago', 'Manuel', 'Ricardo', 'Gabriel', 'Héctor', 'Francisco', 'Jorge', 'Eduardo', 'Mario', 'Roberto', 'Alberto', 'Gonzalo' , 'María', 'Laura', 'Ana', 'Luz', 'Patricia', 'Elena', 'Sofía', 'Isabel', 'Carmen', 'Gabriela', 'Verónica', 'Claudia', 'Daniela', 'Adriana', 'Fabiola', 'Victoria', 'Natalia', 'Mónica', 'Alejandra', 'Silvia', 'Diana', 'Fernanda', 'Paula', 'Rosa', 'Estela']
nombres_lugares = ['Corcovado', 'Arenal', 'Tortuguero', 'Monteverde', 'Rincón de la Vieja', 'Manuel Antonio', 'Poás', 'Talamanca', 'Cahuita', 'Turrialba', 'Barva', 'Chirripó', 'Irazú', 'Tenorio', 'Pacuare', 'Celeste', 'Barú', 'Gandoca', 'Río Celeste', 'Osa', 'Cocos', 'Cerro Chato', 'Carara', 'Ara', 'Rincón de Osa', 'Miravalles', 'Río Pacuare', 'Savegre', 'Tortuguero', 'Naranjo', 'Carrillo', 'Negro', 'Aguilar', 'Fortuna', 'Veragua', 'Barreal', 'Rivas', 'Frijolar', 'Madre Selva', 'Sirena', 'Madrigal', 'Veragua', 'Rodeo', 'Cedral', 'Cedralito', 'Esperanza', 'Boca Tapada']
apellidos = ['González', 'Rodríguez', 'Gómez', 'Fernández', 'López', 'Díaz', 'Martínez', 'Pérez', 'García', 'Sánchez', 'Romero', 'Suárez', 'Torres', 'Rivera', 'Domínguez', 'Vásquez', 'Castillo', 'Rojas', 'Morales', 'Ortega', 'Gutiérrez', 'Reyes', 'Ramírez', 'Jiménez', 'Hernández', 'Álvarez', 'Moreno', 'Muñoz', 'Alonso', 'Silva', 'Valenzuela', 'Medina', 'Ramos', 'Paz', 'Benítez', 'Herrera', 'Aguilar', 'Mendoza', 'Guerrero', 'Flores', 'Pereira', 'Cabrera', 'Chávez', 'Campos', 'Ortiz', 'Vega', 'León', 'Pardo', 'Cortés']
lugares_naturales = ['Parque', 'Reserva', 'Bosque', 'Selva', 'Montaña', 'Cañón', 'Playa', 'Isla', 'Volcán', 'Parque Nacional', 'Reserva Natural', 'Bosque Nativo', 'Área Protegida', 'Santuario de Fauna y Flora', 'Refugio de Vida Silvestre', 'Área Silvestre Protegida', 'Humedal', 'Selva Virgen', 'Zona de Conservación', 'Biodiversidad', 'Área de Preservación Ambiental', 'Zona de Reserva', 'Zona de Vida Silvestre', 'Área de Conservación', 'Área de Importancia Ecológica', 'Área Natural Protegida', 'Parque Ecológico', 'Corredor Biológico', 'Zona de Reserva Forestal', 'Área de Vida Silvestre', 'Reserva de la Biosfera', 'Área de Protección de Flora y Fauna', 'Zona de Bosque Primario', 'Parque Natural Regional', 'Área de Regeneración Natural', 'Reserva de Recursos Naturales', 'Área de Bosque Virgen', 'Área de Restauración Ecológica', 'Área de Fauna Silvestre', 'Refugio de Biodiversidad', 'Hábitat Natural', 'Santuario de la Naturaleza', 'Área de Conservación de la Biodiversidad', 'Reserva Indígena', 'Área de Bosque Nativo', 'Área de Especies en Peligro', 'Área de Protección de Ecosistemas', 'Área de Bosque Tropical', 'Área de Protección de Recursos Naturales', 'Reserva Forestal Integral', 'Zona de Selva Protegida', 'Refugio de Aves', 'Reserva Marina', 'Área de Bosque Subtropical', 'Área de Recuperación Ambiental', 'Parque Natural Urbano']
posibles_respuestas = [
    'Sí, es posible.',
    'Sí, es posible. ¿Hay algo más en lo que pueda ayudarte?',
    'No, eso no es posible.',
    'No, eso no es posible. ¿Puedo ayudarte con algo más?',
    'Tal vez en ciertas circunstancias.',
    'Tal vez en ciertas circunstancias. ¿Necesitas más detalles?',
    'Depende de varios factores.',
    'Depende de varios factores. ¿Puedo proporcionarte más información?',
    'Eso está fuera de mi área de conocimiento.',
    'Eso está fuera de mi área de conocimiento. ¿Hay algo más que pueda hacer por ti?',
    '¡Por supuesto!',
    '¡Por supuesto! ¿Hay algo más que te gustaría preguntar?',
    'Lo siento, no tengo suficiente información para responder.',
    'Lo siento, no tengo suficiente información para responder. ¿Puedo ayudarte con algo más?',
    'Es probable.',
    'Es probable. ¿Hay algo más en lo que pueda ayudarte?',
    'Es poco probable.',
    'Es poco probable. ¿Necesitas más información sobre algo más?',
    'No estoy seguro, ¿podrías darme más detalles?',
    'No estoy seguro, ¿podrías darme más detalles? Estoy aquí para ayudar.',
    '¡Claro que sí!',
    '¡Claro que sí! ¿Puedo hacer algo más por ti?',
    'No, definitivamente no.',
    'No, definitivamente no. ¿Necesitas ayuda con algo más?',
    'Posiblemente, pero no puedo asegurarlo.',
    'Posiblemente, pero no puedo asegurarlo. ¿Hay algo más que pueda hacer por ti?',
    'Esa es una pregunta interesante. ¿Qué piensas tú?',
    'Esa es una pregunta interesante. ¿Qué piensas tú? ¿Necesitas más ayuda?',
    'Necesitaría más contexto para responder correctamente.',
    'Necesitaría más contexto para responder correctamente. ¿Puedes proporcionar más detalles?',
    '¡Absolutamente!',
    '¡Absolutamente! ¿Puedo ayudarte con algo más?',
    'No puedo responder eso.',
    'No puedo responder eso. ¿Hay algo más en lo que pueda ayudarte?',
    'Es difícil decirlo sin más información.',
    'Es difícil decirlo sin más información. ¿Puedo ayudarte con otra cosa?',
    'Es posible, pero no puedo confirmarlo con certeza.',
    'Es posible, pero no puedo confirmarlo con certeza. ¿Necesitas más información?',
    '¿Podrías reformular la pregunta, por favor?',
    '¿Podrías reformular la pregunta, por favor? Estoy aquí para ayudar.',
]

errores = {
        'Error1':'El tipo de entrada es incorrecto',
        'Error2':'La entrada no es un número!',
        'Error3':'La entrada no está en el rango.'
          }

def limpiar_pantalla():
    '''
    Limpia la pantalla de la terminal.
    '''
    print("\n" * 100)

def convertir_a_entero(arr):
    '''
    Entrada: Debe ser una cadena.
    Salida: Debe ser un número o un error.
    Restricciones: La entrada debe ser únicamente una cadena, la cadena no debe ser vacía.
    '''
    if type(arr) != str:
        return f"Error1 | {errores['Error1']}"
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
        return f"Error1 | {errores['Error1']}"
    
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
        return f"Error1 | {errores['Error1']}"
    
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

def escoger_cantidad(cantidad, arr):
    #E: un número y una lista
    #S: una lista con la cantidad de elementos que se pidieron, con randoms de la lista y la lista sin esos elementos
    #R: la cantidad debe ser un número y la lista debe ser una lista

    if type(cantidad) != int:
        return f"Error1 | {errores['Error1']}"
    elif type(arr) != list:
        return f"Error1 | {errores['Error1']}"
    else:
        return escoger_cantidad_aux(cantidad, arr, [], arr)

def escoger_cantidad_aux(cantidad, arr, salida, original):
    #Función auxiliar de escoger_cantidad

    if cantidad == 0:
        return [salida, original]
    else:
        indice = random.randint(0, len(arr) - 1)
        salida.append(arr[indice])
        arr.pop(indice)
        return escoger_cantidad_aux(cantidad - 1, arr, salida, original)

def anadir_random_a_lista(lista1, lista2):
    #E: Dos listas.
    #S: Lista1 con los elementos de lista2
    #R: Ambas entradas deben ser listas.

    if type(lista1) != list:
        return f"Error1 | {errores['Error1']}"
    elif type(lista2) != list:
        return f"Error1 | {errores['Error1']}"
    else:
        return anadir_random_a_lista_aux(lista1, lista2, 0, len(lista2))

def anadir_random_a_lista_aux(lista1, lista2, indx, fin):
    #Funcion auxiliar

    if indx == fin:
        return lista1
    else:
        indice_aleatorio = random.randint(0, len(lista1) - 1)
        lista1[indice_aleatorio] = lista1[indice_aleatorio] + lista2[indx]
        return anadir_random_a_lista_aux(lista1, lista2, indx + 1, fin)
    
def visitar_area(area, nombre, areas_verdes):
    #E: Un número, una cadena y una lista.
    #S: None
    #R: El número debe ser un número, la cadena debe ser una cadena y la lista debe ser una lista.

    if type(area) != int:
        return f"Error1 | {errores['Error1']}"
    elif type(nombre) != str:
        return f"Error1 | {errores['Error1']}"
    elif type(areas_verdes) != list:
        return f"Error1 | {errores['Error1']}"
    else:
        return visitar_area_aux(area, nombre, areas_verdes)

def visitar_area_aux(area, nombre, areas_verdes):
    #Función auxiliar

    print(f"¡Hola {nombre}! Bienvenido al área verde {areas_verdes[area][0]}")
    print(f"En este lugar, encontrarás a las siguientes personas:")
    print(areas_verdes[area][1:])
    print(f"¿Te gustaría hacer algo más en este lugar?")
    print(f"1. Conocer a una persona.")
    print(f"2. Volver al menú principal.")
    opcion = input()
    
    if opcion == "1":
        print(f"Por favor, elige una persona para conocer: (Escribe el número de la opción empezando en 0)")
        persona = input()
        persona = convertir_a_entero(persona)
        print(f"¡Excelente elección! Has escogido conocer a {areas_verdes[area][1:][persona]}")
        print(f"¿Qué te gustaría preguntarle a {areas_verdes[area][1:][persona]}?")
        pregunta = input()
        print(random.choice(posibles_respuestas))
        return visitar_area(area, nombre, areas_verdes)
    elif opcion == "2":
        return None

def inicio(setup=True, nombre="", areas_verdes=[], posibles_areas=[], posibles_nombres=[], nombres_areas = []):

    if setup:

        print(f'''
            ¡Bienvenido a un mundo SolarPunk!
            En este mundo, la naturaleza ha recuperado su lugar y la humanidad ha aprendido a convivir con ella.
            La tecnología y la naturaleza se han fusionado para crear un mundo más sostenible y equitativo.     
            ''')
        
        print(f"Para empezar, ¿Cuál es tu nombre de jugador?")
        nombre = input()

        print(f"¡Hola {nombre}! ¿Cuántas áreas verdes deseas generar?")
        cantidad = input()

        cantidad = convertir_a_entero(cantidad)

        # Generación de las áreas verdes.
        posibles_areas = generar_nombres(1)
        lista_resultante = escoger_cantidad(cantidad, posibles_areas)
        areas_verdes = lista_resultante[0]
        nombres_areas = copy.deepcopy(areas_verdes) 

        posibles_areas = lista_resultante[1]        

        print(f"¡Excelente elección! Tus áreas verdes son:")
        print(areas_verdes)

        print(f"Ahora, ¿cuántas personas deseas generar? Para empezar")
        cantidad = input()
        cantidad = convertir_a_entero(cantidad)

        # Generación de los nombres de las personas.
        posibles_nombres = generar_nombres(0)
        lista_resultante2 = escoger_cantidad(cantidad, posibles_nombres)
        nombres_personas = lista_resultante2[0]
        posibles_nombres = lista_resultante2[1]
        
        print(f"¡Excelente elección! Tus personas son:")
        print(nombres_personas)
        print(f"Se agregaran estas personas a tus áreas verdes...")

        areas_verdes = anadir_random_a_lista(areas_verdes, nombres_personas)
        print(areas_verdes)
        
        return inicio(False, nombre, areas_verdes, posibles_areas, posibles_nombres, nombres_areas)

    else:
        print(f"¡Hola {nombre}! ¿En qué puedo ayudarte hoy?")
        print(f"1. Imprimir instrucciones.")
        print(f"2. Escoger área verde a visitar.")
        print(f"3. Salir.")

        opcion = input()

        if opcion == "1":
            print(f'''
                ¡Instrucciones!
                En este juego, tendrás la oportunidad de visitar diferentes áreas verdes y conocer a las personas que las habitan.
                Para empezar, elige una de las siguientes opciones:
                1. Imprimir instrucciones.
                2. Escoger área verde a visitar.
                3. Salir.
            ''')
            return inicio(False, nombre, areas_verdes, posibles_areas, posibles_nombres)
        
        elif opcion == "2":
            print(f"¡Excelente elección! Tus áreas verdes son:")
            print(nombres_areas)
            print(f"Por favor, elige un área verde para visitar: (Escribe el número de la opción empezando en 0)")

            area = input()
            area = convertir_a_entero(area)
            
            print(f"¡Excelente elección! Has escogido visitar el área verde: {areas_verdes[area][0]}")
            visitar_area(area, nombre, areas_verdes)
            
            return inicio(False, nombre, areas_verdes, posibles_areas, posibles_nombres)
        
        elif opcion == "3":
            print(f"¡Hasta luego {nombre}!")
            return None
        
inicio()

