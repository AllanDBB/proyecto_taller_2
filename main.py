import random, copy

# Clase para darle color a los textos en la terminal
class Color:
    RESET = "\033[0m"
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"

# Variables globales
nombres = ['Juan', 'José', 'Luis', 'Carlos', 'Alejandro', 'Miguel', 'Javier', 'Fernando', 'Andrés', 'Diego', 'Pedro', 'Daniel', 'Pablo', 'Santiago', 'Manuel', 'Ricardo', 'Gabriel', 'Héctor', 'Francisco', 'Jorge', 'Eduardo', 'Mario', 'Roberto', 'Alberto', 'Gonzalo' , 'María', 'Laura', 'Ana', 'Luz', 'Patricia', 'Elena', 'Sofía', 'Isabel', 'Carmen', 'Gabriela', 'Verónica', 'Claudia', 'Daniela', 'Adriana', 'Fabiola', 'Victoria', 'Natalia', 'Mónica', 'Alejandra', 'Silvia', 'Diana', 'Fernanda', 'Paula', 'Rosa', 'Estela']
nombres_lugares = ['Corcovado', 'Arenal', 'Tortuguero', 'Monteverde', 'Rincón de la Vieja', 'Manuel Antonio', 'Poás', 'Talamanca', 'Cahuita', 'Turrialba', 'Barva', 'Chirripó', 'Irazú', 'Tenorio', 'Pacuare', 'Celeste', 'Barú', 'Gandoca', 'Río Celeste', 'Osa', 'Cocos', 'Cerro Chato', 'Carara', 'Ara', 'Rincón de Osa', 'Miravalles', 'Río Pacuare', 'Savegre', 'Tortuguero', 'Naranjo', 'Carrillo', 'Negro', 'Aguilar', 'Fortuna', 'Veragua', 'Barreal', 'Rivas', 'Frijolar', 'Madre Selva', 'Sirena', 'Madrigal', 'Veragua', 'Rodeo', 'Cedral', 'Cedralito', 'Esperanza', 'Boca Tapada']
apellidos = ['González', 'Rodríguez', 'Gómez', 'Fernández', 'López', 'Díaz', 'Martínez', 'Pérez', 'García', 'Sánchez', 'Romero', 'Suárez', 'Torres', 'Rivera', 'Domínguez', 'Vásquez', 'Castillo', 'Rojas', 'Morales', 'Ortega', 'Gutiérrez', 'Reyes', 'Ramírez', 'Jiménez', 'Hernández', 'Álvarez', 'Moreno', 'Muñoz', 'Alonso', 'Silva', 'Valenzuela', 'Medina', 'Ramos', 'Paz', 'Benítez', 'Herrera', 'Aguilar', 'Mendoza', 'Guerrero', 'Flores', 'Pereira', 'Cabrera', 'Chávez', 'Campos', 'Ortiz', 'Vega', 'León', 'Pardo', 'Cortés']
lugares_naturales = ['Parque', 'Reserva', 'Bosque', 'Selva', 'Montaña', 'Cañón', 'Playa', 'Isla', 'Volcán', 'Parque Nacional', 'Reserva Natural', 'Bosque Nativo', 'Área Protegida', 'Santuario de Fauna y Flora', 'Refugio de Vida Silvestre', 'Área Silvestre Protegida', 'Humedal', 'Selva Virgen', 'Zona de Conservación', 'Biodiversidad', 'Área de Preservación Ambiental', 'Zona de Reserva', 'Zona de Vida Silvestre', 'Área de Conservación', 'Área de Importancia Ecológica', 'Área Natural Protegida', 'Parque Ecológico', 'Corredor Biológico', 'Zona de Reserva Forestal', 'Área de Vida Silvestre', 'Reserva de la Biosfera', 'Área de Protección de Flora y Fauna', 'Zona de Bosque Primario', 'Parque Natural Regional', 'Área de Regeneración Natural', 'Reserva de Recursos Naturales', 'Área de Bosque Virgen', 'Área de Restauración Ecológica', 'Área de Fauna Silvestre', 'Refugio de Biodiversidad', 'Hábitat Natural', 'Santuario de la Naturaleza', 'Área de Conservación de la Biodiversidad', 'Reserva Indígena', 'Área de Bosque Nativo', 'Área de Especies en Peligro', 'Área de Protección de Ecosistemas', 'Área de Bosque Tropical', 'Área de Protección de Recursos Naturales', 'Reserva Forestal Integral', 'Zona de Selva Protegida', 'Refugio de Aves', 'Reserva Marina', 'Área de Bosque Subtropical', 'Área de Recuperación Ambiental', 'Parque Natural Urbano']
posibles_respuestas = [
    '¡Claro que sí, es posible! El futuro está lleno de posibilidades brillantes. ¿Hay algo más en lo que pueda ayudarte a construir un mañana más sustentable y lleno de energía renovable?',
    '¡Por supuesto! ¿Qué tal si exploramos juntos cómo hacerlo posible? El sol brilla para todos, después de todo. ¿Hay algo más que te gustaría preguntar sobre este tema o cualquier otro?',
    'Es probable que en un mundo impulsado por la innovación y la colaboración, veamos soluciones sorprendentes. ¿Te gustaría ser parte de la creación de un futuro más verde y lleno de esperanza?',
    '¡Absolutamente! En un mundo donde la comunidad se une para resolver los desafíos, ¡casi todo es posible! ¿Puedo ayudarte con algo más para hacer de nuestro mundo un lugar más brillante?',
    'Es posible, pero necesitamos unirnos para hacerlo realidad. ¿Qué ideas tienes para contribuir al cambio? Juntos podemos hacer cosas extraordinarias.',
    '¡Por supuesto que sí! El futuro es lo que hacemos de él, y juntos podemos hacerlo más brillante y sostenible. ¿Cómo podemos trabajar juntos para hacerlo posible?',
    'Definitivamente es una posibilidad emocionante. Imagina un mundo donde la tecnología y la naturaleza coexisten en armonía. ¿Qué papel te gustaría desempeñar en esa visión?',
    'Absolutamente, pero depende de nosotros convertir esa posibilidad en realidad. ¿Qué acciones podemos tomar hoy para hacer que ese futuro sea más probable?',
    'Es posible, pero solo si abrazamos la creatividad y la colaboración. ¿Estás listo para ser parte de la solución?',
    'Sí, definitivamente es posible. ¿Qué ideas tienes para hacer que esa posibilidad se convierta en una realidad palpable?',
    '¡Claro que sí! En un mundo impulsado por la innovación y la compasión, ¡casi cualquier cosa es posible! ¿Cómo podemos empezar a construir ese mundo hoy mismo?',
    'Por supuesto que sí, pero necesitaremos pensar de manera creativa y actuar con determinación para hacerlo realidad. ¿Qué primer paso podemos dar juntos?',
    'Es posible, pero solo si nos comprometemos a hacer cambios significativos en la forma en que vivimos y trabajamos. ¿Estás dispuesto a dar el primer paso hacia ese futuro?',
    '¡Absolutamente! El futuro está lleno de infinitas posibilidades, y depende de nosotros elegir el camino que lleva hacia un mundo más sostenible y equitativo. ¿Cómo podemos empezar a caminar en esa dirección hoy mismo?',
    'Sin duda es una posibilidad emocionante. ¿Qué acciones podemos tomar ahora mismo para hacer que esa posibilidad sea más probable?',
    'Sí, es posible, pero solo si nos comprometemos a trabajar juntos y a tomar medidas concretas para hacerlo realidad. ¿Cómo podemos colaborar para hacer que eso suceda?',
    'Por supuesto que sí. El futuro está lleno de oportunidades para la innovación y el progreso. ¿Qué papel te gustaría desempeñar en la construcción de ese futuro?',
    'Definitivamente es una posibilidad, pero necesitaremos pensar de manera creativa y actuar con determinación para hacerla realidad. ¿Qué acciones podemos tomar hoy para comenzar ese proceso?',
    '¡Claro que sí! El futuro está lleno de posibilidades emocionantes, y depende de nosotros aprovecharlas al máximo. ¿Cómo podemos empezar a convertir esa posibilidad en realidad hoy mismo?',
    'Sí, es posible, pero solo si nos comprometemos a trabajar juntos y a tomar medidas concretas para hacerlo realidad. ¿Qué primer paso podemos dar en esa dirección?',
    'Absolutamente, pero necesitaremos unir fuerzas y trabajar juntos para hacerlo realidad. ¿Cómo podemos empezar a construir ese futuro hoy mismo?',
    'Sin duda es una posibilidad emocionante. ¿Qué acciones podemos tomar ahora mismo para hacer que esa posibilidad sea más probable?',
    'Es posible, pero solo si nos comprometemos a hacer cambios significativos en la forma en que vivimos y trabajamos. ¿Estás dispuesto a dar el primer paso hacia ese futuro?',
    '¡Absolutamente! El futuro está lleno de infinitas posibilidades, y depende de nosotros elegir el camino que lleva hacia un mundo más sostenible y equitativo. ¿Cómo podemos empezar a caminar en esa dirección hoy mismo?',
    'Sí, es posible, pero solo si nos comprometemos a trabajar juntos y a tomar medidas concretas para hacerlo realidad. ¿Qué acciones podemos tomar hoy para comenzar ese proceso?'
]
datos_curiosos_solarpunk = [
    'En el solarpunk, la energía solar y otras fuentes renovables son predominantes y se utilizan para alimentar la sociedad.',
    'Las comunidades solarpunk a menudo promueven la autosuficiencia y la descentralización, fomentando la producción local de alimentos y bienes.',
    'La arquitectura solarpunk incorpora diseños eco-amigables, como edificios con jardines verticales y techos verdes.',
    'Los transportes solarpunk suelen ser eléctricos o alimentados por energía solar, y se fomenta el uso de la bicicleta y el transporte público.',
    'La moda solarpunk se caracteriza por prendas de vestir hechas con materiales sostenibles y tecnología portátil que genera energía.',
    'En el solarpunk, la tecnología se utiliza para empoderar a las comunidades y mejorar la calidad de vida, en lugar de centrarse únicamente en el lucro.',
    'El solarpunk promueve la conservación del medio ambiente y la biodiversidad, así como la restauración de ecosistemas degradados.',
    'Se fomenta la participación ciudadana y la democracia directa en las decisiones que afectan a la comunidad en el solarpunk.',
    'El arte solarpunk celebra la belleza de la naturaleza y la intersección entre la tecnología y el medio ambiente de manera armoniosa.',
    'El solarpunk se inspira en movimientos como el ecologismo, el anarquismo y el futurismo, entre otros, para crear visiones utópicas de un futuro sostenible.'
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
    print("\n" * 50)

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
    elif len(areas_verdes[area]) <= 1:
        print(f"¡Hola {nombre}! Bienvenido al área verde {areas_verdes[area][0]}")
        print(f"En este lugar, {Color.RED}no hay personas para conocer.{Color.RESET}")
        return None
    else:
        return visitar_area_aux(area, nombre, areas_verdes)

def visitar_area_aux(area, nombre, areas_verdes):
    
    #Función auxiliar

    print(f"¡Hola {nombre}! Bienvenido al área verde {Color.GREEN}{areas_verdes[area][0]}{Color.RESET}")
    print(f"En este lugar, encontrarás a las siguientes personas:")
    imprimir = areas_verdes[area][1:]
    enlistar(imprimir, 1)
    print(f"¿Te gustaría hacer algo más en este lugar?")
    print(f"1. Conocer a una persona.")
    print(f"2. Volver al menú principal.")
    opcion = input()
    
    if opcion == "1":
        print(f"Por favor, elige una persona para conocer: (Escribe el número de la opción empezando en 0)")
        persona = input()
        persona = convertir_a_entero(persona)
        print(f"¡Excelente elección! Has escogido conocer a {areas_verdes[area][1:][persona]}")
        limpiar_pantalla()
        print(f"¿Qué te gustaría preguntarle a {areas_verdes[area][1:][persona]}?")
        pregunta = input()
        print(random.choice(posibles_respuestas) + "\n" * 5)
        return visitar_area(area, nombre, areas_verdes)
    elif opcion == "2":
        limpiar_pantalla()
        return None

def enlistar(lista, caso=0):
    #E: una lista de listas a imprimir por elemento
    #S: cada elemento de la lista
    #R: la entrada debe ser una lista de listas

    if type(lista)!=list:
        return f"Error1 | {errores['Error1']}"

    else:
        return enlistar_aux(lista, 0, len(lista), caso)
    
def enlistar_aux(lista, ini, fin, caso):
    #funcion auxiliar

    if ini==fin:
        return None
    else:
        if caso==0:
            print(f"{ini}. {lista[ini][0]}")
        else:
            print(f"{ini}. {lista[ini]}")
        return enlistar_aux(lista, ini+1, fin, caso)

    
#Para imprimir los ascii art
def imprimir_personas():
    print("""                                                                                                                                                                                                                                         
                                                                                        
  ....     -@@@*.     .:..     *@@@=     ..:.     .%@@#.     ....    .-@@@*.     ...    
 .#@@@:. .#@@@@@@.  .+@@@%.  .@@@@@@%.  .#@@@=. .-@@@@@@.  .-@@@@:. .#@@@@@%.  .*@@@.   
  .-@@@%..%@@@@@@..=@@@@@@@*..@@@@@@@..+@@@@@@@:.=@@@@@@: .@@@@@@@%..%@@@@@@..=@@@%.    
    .*@@@*.*@@@%..@@@@. .%@@@-.%@@@*.:@@@%. -@@@%.-@@@@:.@@@@= .#@@@*.#@@@#.:@@@@:      
      .#@@@%%%%%%@@@=.    -@@@@%%%%%@@@@-    .*@@@#%%%%%@@@*.    .%@@@%%%%%%@@@=.       
       .:@@@@@@@@@*.       .-@@@@@@@@@-.       .@@@@@@@@@@..      .:@@@@@@@@@#.         
         .@@@@@@@@.          -@@@@@@@%          .@@@@@@@@.          -@@@@@@@@           
         .@@@@@@@@.          -@@@@@@@%          .@@@@@@@@.          -@@@@@@@@           
         .@@@@@@@@.          -@@@@@@@%          .@@@@@@@@.          -@@@@@@@@           
         .@@@@@@@@.          -@@@@@@@%          .@@@@@@@@.          -@@@@@@@@           
         .@@@@@@@@.          -@@@@@@@@          .@@@@@@@@.          -@@@@@@@@           
         .@@@%@@@@.          -@@@#@@@@          .@@@@#@@@.          -@@@#@@@@           
         .@@@*%@@@.          -@@@+@@@@          .@@@@*@@@.          -@@@+%@@@           
         .@@@*%@@@.          -@@@+@@@@          .@@@@*@@@.          -@@@+%@@@           
         .@@@*%@@@.          -@@@+@@@@          .@@@@*@@@.          -@@@+%@@@           
         .@@@*%@@@.          -@@@+@@@@          .@@@@*@@@.          -@@@+%@@@           
         .@@@*%@@@.          -@@@+@@@@          .@@@@*@@@.          -@@@+%@@@           
         .@@@+#@@@.          -@@@=@@@%.         .@@@@+@@@.          :@@@+%@@%.          
          ........           ..:. ....           .... ...            ........           
                                                                                        
                                                                     """)
    return None
            
def imprimir_areas_verdes():
    print("""
            * *    
           *    *  *
      *  *    *     *  *
     *     *    *  *    *
 * *   *    *    *    *   *
 *     *  *    * * .#  *   *
 *   *     * #.  .# *   *
  *     "#.  #: #" * *    *
 *   * * "#. ##"       *
   *       "###
             "##
              ##.
              .##:
              :###
              ;###
            ,####.
/\/\/\/\/\/.######.\/\/\/\/\
  """)
    return None

def imprimir_salida():
    print("""                                     
 ____            _                     ____                    _    
/ ___|    ___   | |   __ _   _ __     |  _ \   _   _   _ __   | | __
\___ \   / _ \  | |  / _` | | '__|    | |_) | | | | | | '_ \  | |/ /
 ___) | | (_) | | | | (_| | | |       |  __/  | |_| | | | | | |   < 
|____/   \___/  |_|  \__,_| |_|       |_|      \__,_| |_| |_| |_|\_\
          
             _ __    ___     ___  | | __  ___                                   
            | '__|  / _ \   / __| | |/ / / __|                                      
            | |    | (_) | | (__  |   <  \__ \                                  
            |_|     \___/   \___| |_|\_\ |___/   """)
    return None

def imprimir_dato():
    print("""
     .-.                                    ,-.
  .-(   )-.                              ,-(   )-.
 (     __) )-.                        ,-(_      __)
  `-(       __)                      (_    )  __)-'
    `(____)-',                        `-(____)-'
  - -  :   :  - -
      / `-' \
    ,    |   .
         .                         _
                                  >')
               _   /              (\\         (W)
              =') //               = \     -. `|'
               ))////)             = ,-      \(| ,-
              ( (///))           ( |/  _______\|/____
~~~~~~~~~~~~~~~`~~~~'~~~~~~~~~~~~~\|,-'::::::::::::::
            _                 ,----':::::::::::::::::
         {><_'c   _      _.--':::::::::::::::::::::::
__,'`----._,-. {><_'c  _-':::::::::::::::::::::::::::
:.:.:.:.:.:.:.\_    ,-'.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:
.:.:.:.:.:.:.:.:`--'.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.
.....................................................
  """)

def imprimir_instrucciones():
    # Ház las instrucciones del juego, lo que teníamos antes con todo lo que puedes hacer, usa bastantes cpolores :)
    limpiar_pantalla()
    print(f'''
    {Color.BOLD}Instrucciones:{Color.RESET}
    {Color.GREEN}SolarPunk{Color.RESET} es un juego de simulación en el que puedes explorar un mundo sostenible y lleno de energía renovable.
    En este mundo, la naturaleza y la tecnología se han fusionado para crear un entorno equitativo y lleno de vida.
    Aquí tienes algunas cosas que puedes hacer en el juego:
    - Crear áreas verdes y llenarlas de plantas, árboles y vida silvestre.
    - Conocer a personas que viven en las áreas verdes y aprender sobre sus historias y experiencias.
    ¡Diviértete explorando y creando en el mundo {Color.GREEN}SolarPunk{Color.RESET}!''')
    return None

def inicio(setup=[True, True, True, True], nombre="", areas_verdes=[], posibles_areas=[], posibles_nombres=[], nombres_areas = []):

    if setup[0]:

        if setup[1]:
            limpiar_pantalla()
            print(f'''
                ¡Bienvenido a un mundo {Color.GREEN}SolarPunk {Color.RESET}!
                En este mundo, la naturaleza ha recuperado su lugar y la humanidad ha aprendido a convivir con ella.
                La tecnología y la naturaleza se han fusionado para crear un mundo más sostenible y equitativo.     
                ''')
            
            print(f"Para empezar, ¿Cuál es tu nombre de jugador?")
            nombre = input(Color.BOLD + "Escribe aquí: " + Color.RESET)

            limpiar_pantalla()
              
        if setup[2] == True:
            print(f"¡Excelente {nombre}! Para comenzar {Color.GREEN}¿cuántas áreas verdes deseas generar?{Color.RESET}")
            cantidad = input()
            cantidad = convertir_a_entero(cantidad)

            if cantidad<=0:
                print('Debes ingresar un numero entero positivo mayor que cero')
                return inicio([True, False, True, True], nombre, areas_verdes, posibles_areas, posibles_nombres, nombres_areas)
            else:
                # Generación de las áreas verdes.
                posibles_areas = generar_nombres(1)
                lista_resultante = escoger_cantidad(cantidad, posibles_areas)
                areas_verdes = lista_resultante[0]
                nombres_areas = copy.deepcopy(areas_verdes) 

                posibles_areas = lista_resultante[1]        

                limpiar_pantalla()
                print(f"¡Excelente elección! Tus áreas verdes son:")
                enlistar(areas_verdes)
                imprimir_areas_verdes()

        if setup[3]:
            
            print(f"Ahora, ¿cuántas personas deseas generar? Para empezar")
            cantidad = input()
            cantidad = convertir_a_entero(cantidad)

            if cantidad<=0:
                print('Debes ingresar un numero entero positivo mayor que cero')
                return inicio([True, False, False, True], nombre, areas_verdes, posibles_areas, posibles_nombres, nombres_areas)
            
            else:
                # Generación de los nombres de las personas.
                posibles_nombres = generar_nombres(0)
                lista_resultante2 = escoger_cantidad(cantidad, posibles_nombres)
                nombres_personas = lista_resultante2[0]
                posibles_nombres = lista_resultante2[1]
                anadir_random_a_lista(areas_verdes, nombres_personas)
                
                print(f"¡Excelente elección! Tus personas son:")
                enlistar(nombres_personas)
                imprimir_personas()
                print(f"Se agregaran estas personas a tus {Color.GREEN}áreas verdes{Color.RESET}... ¡Ve a saludarlos!")
                
                return inicio([False, False, False, False], nombre, areas_verdes, posibles_areas, posibles_nombres, nombres_areas)

    else:
        print(f"\n ¡Hola {nombre}! ¿En qué puedo ayudarte hoy?")
        print(f"1. Imprimir instrucciones.")
        print(f"2. Escoger área verde a visitar.")
        print(f"3. Generar más personas.")
        print(f"4. Dato curioso Solarpunk")
        print(f"5. Salir.")

        opcion = input()

        if opcion == "1":
            imprimir_instrucciones()
            return inicio([False, False, False, False], nombre, areas_verdes, posibles_areas, posibles_nombres, nombres_areas)
        
        elif opcion == "2":
            limpiar_pantalla()
            print(f"¡Excelente elección! Tus áreas verdes son:")
            enlistar(nombres_areas)
            print(f"Por favor, elige un área verde para visitar: (Escribe el número de la opción empezando en 0)")

            area = input()
            area = convertir_a_entero(area)
            limpiar_pantalla()
            print(f"¡Excelente elección! Has escogido visitar el área verde: {areas_verdes[area][0]}")
            visitar_area(area, nombre, areas_verdes)
            
            return inicio([False, False, False, False], nombre, areas_verdes, posibles_areas, posibles_nombres, nombres_areas)
        
        elif opcion == "3":
            limpiar_pantalla()
            print(f"¿Cuántas personas deseas generar?")
            cantidad = input()
            cantidad = convertir_a_entero(cantidad)

            if cantidad<=0:
                print('Debes ingresar un numero entero positivo mayor que cero')
                return inicio([False, False, False, False], nombre, areas_verdes, posibles_areas, posibles_nombres, nombres_areas)

            else:
                lista_resultante2 = escoger_cantidad(cantidad, posibles_nombres)
                posibles_nombres = lista_resultante2[1]

                print(f"¡Excelente elección! Tus personas son:")
                enlistar(lista_resultante2[0])
                print(f"Se agregaran estas personas a tus {Color.GREEN}áreas verdes{Color.RESET}... ¡Ve a saludarlos!")
                
                areas_verdes = anadir_random_a_lista(areas_verdes, lista_resultante2[0])
                nombres_areas = copy.deepcopy(areas_verdes)
                return inicio([False, False, False, False], nombre, areas_verdes, posibles_areas, posibles_nombres, nombres_areas)
            
        elif opcion=="4":
            limpiar_pantalla()
            dato=random.randint(0,len(datos_curiosos_solarpunk)-1)
            print(Color.BOLD + datos_curiosos_solarpunk[dato] + Color.RESET)
            imprimir_dato()
            return inicio([False, False, False, False], nombre, areas_verdes, posibles_areas, posibles_nombres, nombres_areas)
            
        elif opcion == "5":
            print(f"¡Hasta luego {nombre}!")
            imprimir_salida()
            return None
        
        else:
            return inicio([False, False, False, False], nombre, areas_verdes, posibles_areas, posibles_nombres, nombres_areas)
        
inicio()

