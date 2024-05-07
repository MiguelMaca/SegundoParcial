class Nodo:
    def __init__(self, pregunta, si=None, no=None):
        self.pregunta = pregunta
        self.si = si
        self.no = no

def construir_arbol():
    # Construye el árbol de adivinanzas
    perro = Nodo("¿Es un perro?")
    gato = Nodo("¿Es un gato?")
    agua = Nodo("¿Es una bebida?", perro, gato)
    ropa = Nodo("¿Es ropa?", agua)
    arbol = Nodo("¿Es un árbol?", ropa)
    return arbol

def jugar(arbol):
    #El programa inicia con las preguntas preguntando si es o no, donde en caso si sea avanza al sigueinte nodo hasta
    #terminar el arbol, en caso no se se pasa a la funcion aprender.
    nodo_actual = arbol
    while True:
        respuesta = input(f"{nodo_actual.pregunta}  (sí/no): ").lower()
        if respuesta == "si":
            if nodo_actual.si is None:
                print("¡Adiviné!")
                break
            nodo_actual = nodo_actual.si
        elif respuesta == "no":
            if nodo_actual.no is None:
                aprender(nodo_actual)
                break
            nodo_actual = nodo_actual.no
        else:
            print("Por favor, responde sí o no.")

def aprender(nodo):
    #Funcion donde el programa aprende que objeto/animal/personaje esta incorrecto y los sutituye por el correcto
    #Nos pregunta por el nombre del objeto que no ha adivinado
    nueva_pregunta = input("¡No he adivinado! ¿Cuál es tu objeto/animal/personaje? ")
    nueva_respuesta = input(f"Por favor, ingresa una pregunta que distinga {nodo.pregunta.lower()} de {nueva_pregunta.lower()}: ")
    respuesta_usuario = input(f"Para {nueva_pregunta.lower()}, ¿la respuesta sería sí o no? ")
    nuevo_nodo = Nodo(nueva_pregunta)
    if respuesta_usuario.lower() == "si":
        nodo.si = nuevo_nodo
        nodo.no = Nodo(nodo.pregunta)
    else:
        nodo.si = Nodo(nodo.pregunta)
        nodo.no = nuevo_nodo

def reiniciar_juego():
    #Nos pregunta para reiniciar el juego en caso sea si se regresa un True o un False
    while True:
        respuesta = input("¿Quieres jugar de nuevo? (sí/no): ").lower()
        if respuesta == "si":
            return True
        elif respuesta == "no":
            return False
        else:
            print("Por favor, responde sí o no.")

def main():
    #Se inicia el programa y construye el arbol y en caso se termine el juego la opcion de reiniciarlo.
    arbol = construir_arbol()
    while True:
        jugar(arbol)
        if not reiniciar_juego():
            break


main()
