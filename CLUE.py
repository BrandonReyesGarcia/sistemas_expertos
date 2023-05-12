import random

personas = ["mario", "luigi", "capi", "toad", "princesa"]
armas = ["banana", "tortuga", "estrella", "pulpo", "bomba"]
lugares = ["pista", "arcoiris", "castillo", "bosque", "ciudad"]

locacion = random.choice(lugares)
personaje = random.choice(personas)
arma_final = random.choice(armas)

asignaciones = {}

for lugar in lugares:

    persona, arma = random.sample(personas, 1)[0], random.sample(armas, 1)[0]
    asignaciones[lugar] = {"persona": persona, "arma": arma}
    personas.remove(persona)
    armas.remove(arma)

for i in range(5):
    print("\n¿Qué evidencia quieres revisar?")
    print("1. Evidencia de una persona")
    print("2. Evidencia de un lugar")
    print("3. Evidencia de un arma")
    opcion = input("Ingresa tu elección (1, 2 o 3): ")

    if opcion == "1":
        print("\n¿A que personage quieres interrogar?")
        print("1. mario")
        print("2. luigi")
        print("3. capi")
        print("4. toad")
        print("5. princesa")
        persona_elegida = input("Ingresa el nombre de la persona que quieres investigar: ").lower()
            
        
        if persona_elegida == personaje:

            for clave in asignaciones:
                if asignaciones[clave]['persona'] == persona_elegida:
                    print(f"{persona_elegida} se encuentra en:")
                    print("--", clave)
            print(f" A {personaje} no se le vio por ninguna parte.")
        else:
            for clave in asignaciones:
                if asignaciones[clave]['persona'] == persona_elegida:
                    print(f"{persona_elegida} se encuentra en:")
                    print("--", clave)

    elif opcion == "2":
        print("\n¿De que lugar quieres saber?")
        print("1. pista")
        print("2. arcoiris")
        print("3. castillo")
        print("4. bosque")
        print("5. ciudad")
        lugar_elegido = input("Ingresa el nombre del lugar que quieres investigar: ").lower()
        if lugar_elegido == locacion:
            for habitacion, datos in asignaciones.items():
                if habitacion == lugar_elegido:
                    print("El arma en la habitación", habitacion, "es:", datos['arma'])
                    print("Se detectó que las cámaras de seguridad en ese lugar fueron apagadas poco antes del crimen.")
        else:
            for habitacion, datos in asignaciones.items():
                if habitacion == lugar_elegido:
                    print("El arma en la habitación", habitacion, "es:", datos['arma'])
                    print(" No se encontraron pruebas adicionales en el lugar.")

    elif opcion == "3":
        print("\n¿Sobre que arma quieres saber?")
        print("1. banana")
        print("2. tortuga")
        print("3. estrella")
        print("4. pulpo")
        print("5. bomba")
        arma_elegida = input("Ingresa el nombre del arma que quieres revisar: ").lower()
        if arma_elegida == arma_final:                                 
            for clave in asignaciones:
                if asignaciones[clave]['arma'] ==  arma_elegida:
                    print(f"El arma {arma_elegida} desaparecio de")
                    print("--", clave)
            
        else:   
             for clave in asignaciones:
                if asignaciones[clave]['arma'] ==  arma_elegida:
                    print(f"El arma {arma_elegida} desaparecio de")
                    print("--", clave)
                    print(f"No hay evidencia que sugiera que {arma_elegida} fue utilizada en el crimen.")

print("\n¿Quieres hacer una suposición final?")
print("1. Sí")
print("2. No")
opcion_final = input()

if opcion_final == '1':
    print("\n¿Quién cometió el crimen?")
    respuesta_personaje = input().lower()
    print("\n¿En qué locación ocurrió el crimen?")
    respuesta_locacion = input().lower()
    print("\n¿Qué arma se utilizó en el crimen?")
    respuesta_arma = input().lower()
    
    if respuesta_personaje == personaje and respuesta_locacion == locacion and respuesta_arma == arma_final:
        print("¡Felicidades! ¡Has resuelto el crimen!")
    else:
        print("Lo siento, esa no es la solución correcta.")
