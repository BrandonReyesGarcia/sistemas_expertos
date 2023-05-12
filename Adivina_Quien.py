import random

class Personaje:
    def __init__(self, nombre, genero, pelo, ojos, accesorios, barba=False):
        self.nombre = nombre
        self.genero = genero
        self.pelo = pelo
        self.ojos = ojos
        self.accesorios = accesorios
        self.barba = barba

personajes = [
    Personaje("Ana", "Femenino", "Corto", "Marrones", "Collar"),
    Personaje("Sofía", "Femenino", "Largo", "Azules", "Pendientes"),
    Personaje("Carlos", "Masculino", "Corto", "Marrones", "Gafas"),
    Personaje("Javier", "Masculino", "Largo", "Verdes", "Sombrero"),
    Personaje("Pedro", "Masculino", "Corto", "Azules", "Bigote", True),
    Personaje("Laura", "Femenino", "Largo", "Marrones", "Pelo recogido"),
    Personaje("Lucía", "Femenino", "Corto", "Verdes", "Pendientes"),
    Personaje("Pablo", "Masculino", "Largo", "Marrones", "Sombrero"),
    Personaje("Teresa", "Femenino", "Largo", "Azules", "Gafas"),
    Personaje("Juan", "Masculino", "Corto", "Verdes", "Bigote", True)
]

atributos = ["genero", "pelo", "ojos", "accesorios", "barba"]

def jugar():
    global personajes
    personaje_secreto = random.choice(personajes)

    print("¡Bienvenido al juego de Adivina Quién!")
    print("Tienes que adivinar quién es el personaje secreto.")
    print("Puedes hacer preguntas sobre los siguientes atributos: género, pelo, ojos, accesorios y barba (sí o no)")

    preguntas_restantes = 5

    while preguntas_restantes > 0:
        atributo = random.choice(atributos)
        print(f"\nTe quedan {preguntas_restantes} preguntas.")
        respuesta = input(f"¿Tiene el personaje {atributo} {getattr(personaje_secreto, atributo)}? ").lower()

        if respuesta == "si":
            personajes = [p for p in personajes if getattr(p, atributo) == getattr(personaje_secreto, atributo)]
        else:
            personajes = [p for p in personajes if getattr(p, atributo) != getattr(personaje_secreto, atributo)]

        preguntas_restantes -= 1

        if len(personajes) == 1:
            print(f"\n¡El personaje secreto es {personajes[0].nombre}!")
            return

    print("\nNo has podido adivinar el personaje secreto. ¡Suerte la próxima vez!")

jugar()
