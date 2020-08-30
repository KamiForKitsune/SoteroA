# SECCION DE LABORATORIO: O-C-5
# PROFESOR DE LABORATORIO: CARLOS VERA
# PROFESOR DE TEORIA: CAMILA MARQUEZ
# INTEGRANTES:
# 1.
# NOMBRE:Ismael Orrego Contador
# RUT: 20.295.679-3
# CARRERA: Ingenieria Civil Mecanica

# DESCRIPCION DEL PROGRAMA:

# IMPORTACIONES:
import time
# Modulo time:
# Modulo que permite trabajar con el tiempo

from random import randint
# Funcion randint:
# Funcion que selecciona un numero aleatorio entre dos numeros separados por una coma, contando los extremos.


# CONSTANTES:
# En este codigo no utilice ninguna constante, ya que incluso las listas que contien los atributos fijos del heroe-
# -cambiaran dependiendo el cual se utilice, y de la misma forma ocurre con el enemigo.
GUERRERO = [12, 30, 5000, 14, 20, 0, 0, 0, 2, 8, 0, 0, 1, 3, 1]
MAGO = [6, 2, 2, 12, 10, 20, 40, 0, 1, 4, 4, 12, 1, 4, 1]
CLERIGO = [8, 2, 4, 12, 12, 0, 20, 40, 1, 6, 0, 0, 1, 3, 1]

KOBOLD = [4, 2, 2, 12, 20, 0, 0, 4, 1, 6, 0, 0, 1, 1, 1, "KOBOLD"]
GOBLIN = [6, 4, 1, 12, 0, 0, 0, 0, 1, 4, 0, 0, 1, 2, 1, "GOBLIN"]
GUERRERO_ORCO = [12, 2, 5, 14, 0, 0, 0, 0,
                 1, 8, 0, 0, 1, 3, 1, "GUERRERO_ORCO"]

visualizarRonda = True
# DEFINICION DE FUNCIONES:

# Funcion introduccion:
# Funcion que entrega un texto informativo con las instrucciones del juego.
# Salida: Un string.


def introduccion():
    print("||€~BIENVENIDO AL JUEGO DE COMBATE ENTRE PERSONAJES~€|| \n||Los personajes disponibles son: <1=Guerrero, 2=Mago y 3=Clerigo> || \n||El numero de enemigos a combatir sera elegido aleatoriamente por la computadora entre 1 y 3, y los enemigos disponibles son: Kobold, Goblin y Guerrero orco||")

# Funcion timer:
# Funcion que permite esperar una cantidad x de segundos, antes de ejecutar la siguiente linea del programa, y asi poder leer detenidamente cada linea.
# Salida:un string indicando los segundos transcurridos en forma de "Ticks".


def timer():
    ticks = 0
    while ticks <= 3:
        #print(ticks, "tick")
        time.sleep(1)
        ticks += 1

# Funcion eleccionHeroe:
# Funcion que permite al usuario seleccionar un heroe para combatir entre 3 disponibles, ademas de indicar las estadisticas de los mismos, y comprobar que la entrada sea un numero entre 1 y 3.
# Entrada: Un numero
# Salida: un string que indica el heroe elegido, y una lista de numeros con las estadisticas del Heroe.


def eleccionHeroe():
    print("||¡Eliga su heroe para combatir al enemigo!|| \n\n||.-1=Guerrero, atributos:||\n||Puntos de vida=12, velocidad=3, ataque=5, defensa=14|| \n||umbralDeHechizo=20, probabilidadDeHechizoAtaque=0, probabilidadDeHechizoDefensa=0, probabilidadDeHechizoCuracion=0|| \n||dañoMinimo=2, dañoMaximo=8, dañoHechizoMinimo=0 y dañoHechizoMaximo=0||\n\n||.-2=Mago, atributos:||\n||Puntos de vida=6, velocidad=2, ataque=2, defensa=12|| \n||umbralDeHechizo=10, probabilidadDeHechizoAtaque=20, probabilidadDeHechizoDefensa=40, probabilidadDeHechizoCuracion=0|| \n||dañoMinimo=1, dañoMaximo=4, dañoHechizoMinimo=4 y dañoHechizoMaximo=12||\n\n||.-3=Clerigo, atributos:||\n||Puntos de vida=8, velocidad=2, ataque=4, defensa=12|| \n||umbralDeHechizo=12, probabilidadDeHechizoAtaque=0, probabilidadDeHechizoDefensa=20, probabilidadDeHechizoCuracion=40|| \n||dañoMinimo=1, dañoMaximo=6, dañoHechizoMinimo=0 y dañoHechizoMaximo=0||")
    continuar = True
    while continuar:
        eleccionHeroe = input("Eleccion: ")
        if not eleccionHeroe.isdigit():
            print("Error. Por favor ingrese un numero valido. ")
        elif int(eleccionHeroe) < 1 or int(eleccionHeroe) > 3:
            print("Error. Por favor ingrese un numero entre 1 y 3. ")
        else:
            continuar = False
    eleccionHeroe = int(eleccionHeroe)
    if eleccionHeroe == 1:
        print("El heroe elegido es: Guerrero nivel 1")
        heroe = GUERRERO
    if eleccionHeroe == 2:
        print("El heroe elegido es: Mago nivel 1")
        heroe = MAGO
    if eleccionHeroe == 3:
        print("El heroe elegido es: Clerigo nivel 1")
        heroe = CLERIGO
    return heroe

# Funcion eleccionEnemigo:
# Funcion que elije aleatoriamente un enemigo entre 1 a 3 enemigos de los disponibles.
# salida: un string que indica los enemigos escogidos y sus caracteristicas, ademas de una lista de las mismas.


def eleccionEnemigo():
    cantidadEnemigos = randint(1, 3)
    listaEnemigos = []
    while len(listaEnemigos) < cantidadEnemigos:
        numEnemigo = len(listaEnemigos)+1
        eleccionEnemigo = randint(1, 3)
        if eleccionEnemigo == 1:
            print("El enemigo numero", numEnemigo,
                  "elegido por la computadora es un Kobold")
            #print("El enemigo numero", numEnemigo, "elegido por la computadora es un: Kobold, y sus atributos en nivel 1 son:\n||Puntos de vida=4, velocidad=2, ataque=2, defensa=12|| \n||umbralDeHechizo=20, probabilidadDeHechizoAtaque=0, probabilidadDeHechizoDefensa=0, probabilidadDeHechizoCuracion=4|| \n||dañoMinimo=1, dañoMaximo=6, dañoHechizoMinimo=0 y dañoHechizoMaximo=0||")
            enemigo = KOBOLD[:]
            listaEnemigos.append(enemigo)
        elif eleccionEnemigo == 2:
            print("El enemigo numero", numEnemigo,
                  "elegido por la computadora es un Goblin")
            #print("El enemigo numero", numEnemigo, "elegido por la computadora es un: Goblin, y sus atributos en nivel 1 son:\n||Puntos de vida=6, velocidad=4, ataque=1, defensa=12|| \n||umbralDeHechizo=0, probabilidadDeHechizoAtaque=0, probabilidadDeHechizoDefensa=0, probabilidadDeHechizoCuracion=0|| \n||dañoMinimo=1, dañoMaximo=4, dañoHechizoMinimo=0 y dañoHechizoMaximo=0||")
            enemigo = GOBLIN[:]
            listaEnemigos.append(enemigo)
        elif eleccionEnemigo == 3:
            print("El enemigo numero", numEnemigo,
                  "elegido por la computadora es un Guerrero Orco")
            #print("El enemigo numero", numEnemigo, "elegido por la computadora es un: Guerrero orco, y sus atributos en nivel 1 son:\n||Puntos de vida=12, velocidad=2, ataque=5, defensa=14|| \n||umbralDeHechizo=0, probabilidadDeHechizoAtaque=0, probabilidadDeHechizoDefensa=0, probabilidadDeHechizoCuracion=0|| \n||dañoMinimo=1, dañoMaximo=8, dañoHechizoMinimo=0 y dañoHechizoMaximo=0||")
            enemigo = GUERRERO_ORCO[:]
            listaEnemigos.append(enemigo)
    return listaEnemigos

# Funcion checkearFincombate:
# Funcion que determina si el combate ha acabado, analizando la vida de los luchadores en cada turno.
# Salida: Un string que indica que el combate se ha acabado, y quien es el ganador.


def checkearFincombate(vidaHeroe, vidaEnemigo):
    if vidaHeroe <= 0:
        print("El HEROE ha muerto, y el ganador es el ENEMIGO")
        print("||La batalla ha terminado||")
        return True
    if vidaEnemigo <= 0:
        print("El ENEMIGO ha muerto, y el ganador es el HEROE")
        print("||La batalla ha terminado||")
        return True
    return False


def checkearVidaEnemigos(listaGauges, enemigos, heroe):
    i = 0
    while i < len(enemigos):
        if enemigos[i][0] <= 0:
            if (listaGauges[i+1] != "derrotado"):
                listaGauges[i+1] = "derrotado"
                if visualizarRonda:
                    print(
                        "El enemigo", enemigos[i][15], "ha muerto, quedando fuera de la ronda...")
                    time.sleep(2)
        i += 1

    enemigosVivos = True

    i = 0
    enemigosDerrotados = 0
    while i < len(enemigos):
        if listaGauges[i+1] == "derrotado":
            enemigosDerrotados += 1
        i += 1
    if enemigosDerrotados == len(enemigos):
        enemigosVivos = False

    return [listaGauges, enemigosVivos]


# Funcion balanceoNiveles:
# Funcion que recibe los atributos del heroe y de todos los enemigos, y balancea sus niveles segun el nivel-
# actual del heroe.
# Salida: una lista con los atributos de los enemigos balanceados.
def balanceoNiveles(heroe, listaEnemigos):
    nivelHeroe = heroe[12]

    i = 0
    while i < len(listaEnemigos):
        if nivelHeroe > 1:
            nivelMinimo = int((nivelHeroe - 3) / len(listaEnemigos))
            if nivelMinimo < 1:
                nivelMinimo = 1

            listaEnemigos[i][12] = randint(
                nivelMinimo, int((nivelHeroe+3)/(len(listaEnemigos))))
        i = i+1

    z = 0
    while z < len(listaEnemigos):
        if listaEnemigos[z][12] > 1:
            if listaEnemigos[z][13] == 1:
                t = 0
                while t < len(listaEnemigos[z]):
                    if t == 1 or t == 4 or t == 5 or t == 6 or t == 7 or t == 12 or t == 13 or t == 14 or t == 15:
                        t = t+1
                    else:
                        listaEnemigos[z][t] += round((listaEnemigos[z]
                                                      [t]*800000)/1000000)*(listaEnemigos[z][12]-1)
                        t = t+1
            if listaEnemigos[z][13] == 2:
                f = 0
                while f < len(listaEnemigos[z]):
                    if f == 1 or f == 4 or f == 5 or f == 6 or f == 7 or f == 12 or f == 13 or f == 14 or f == 15:
                        f = f+1
                    else:
                        listaEnemigos[z][f] += round((listaEnemigos[z]
                                                      [f]*1000000)/1000000)*(listaEnemigos[z][12]-1)
                        f = f+1
            if listaEnemigos[z][13] == 3:
                e = 0
                while e < len(listaEnemigos[z]):
                    if e == 1 or e == 4 or e == 5 or e == 6 or e == 7 or e == 12 or e == 13 or e == 14 or e == 15:
                        e = e+1
                    else:
                        listaEnemigos[z][e] += round((listaEnemigos[z]
                                                      [e]*1250000)/1000000)*(listaEnemigos[z][12]-1)
                        e = e+1

        z = z+1

    return listaEnemigos

# Funcion Carga de gauges:
# Funcion que carga los gauges del heroe y los enemigos
# salida: una lista con los gauges modificados


def cargaGauges(listaGauges, heroe, balanceEnemigos):
    global visualizarRonda

    if visualizarRonda:
        print("---------------------")

    listaGauges[0] += heroe[1]
    if visualizarRonda:
        print("Barra de accion HEROE nivel",
              heroe[12], ":", "⬛"*listaGauges[0], listaGauges[0])
    i = 1
    while i < len(listaGauges):
        if listaGauges[i] != "derrotado":
            listaGauges[i] = listaGauges[i]+balanceEnemigos[i-1][1]
            if visualizarRonda:
                print("Barra de accion enemigo", i, ":", balanceEnemigos[i-1][15], "nivel", balanceEnemigos[i-1][12], "Es: ", "⬛"*listaGauges[i],
                      listaGauges[i])
        i = i+1
    if visualizarRonda:
        print("---------------------")

    return listaGauges


def ataqueHeroe(heroe, enemigo):
    contadorCriticos = 0
    contadorFallos = 0

    vidaEnemigo = enemigo[0]
    vidaHeroe = heroe[0]
    defensaHeroe = heroe[3]
    defensaEnemigo = enemigo[3]
    probHechizoHeroe = randint(1, 100)
    numeroHechizo = randint(1, 20)

    if probHechizoHeroe <= heroe[5] and numeroHechizo >= heroe[4]:
        numeroHechizo2 = randint(1, 20)
        if numeroHechizo2 >= enemigo[3]:
            if numeroHechizo2 == 20:
                if visualizarRonda:
                    print("¡¡El HEROE LANZA UN ATAQUE MAGICO CRITICO!!")
                dañoHechizo = (randint(heroe[10], heroe[11]))*1.5
                if visualizarRonda:
                    print("El daño causado por el hechizo es", dañoHechizo)
                vidaEnemigo -= dañoHechizo
                if visualizarRonda:
                    print(
                        "El ataque del HEROE disminuye la vida del enemigo", enemigo[15], "a:", vidaEnemigo)
                contadorCriticos += 1
            elif numeroHechizo2 == 1:
                if visualizarRonda:
                    print("EL ATAQUE MAGICO HA FALLADO")
                dañoPropio = randint(1, 3)
                if visualizarRonda:
                    print("El HEROE se causa daño a si mismo de:",
                          dañoPropio, "puntos")
                vidaHeroe -= dañoPropio
                if visualizarRonda:
                    print("La vida del HEROE baja a:", vidaHeroe)
                contadorFallos += 1
            elif numeroHechizo2 >= enemigo[3] and numeroHechizo2 != 20 and numeroHechizo2 != 1:
                daño = randint(heroe[10], heroe[11])
                if visualizarRonda:
                    print("El HEROE realiza un hechizo de ataque magico normal")
                vidaEnemigo -= daño
                if visualizarRonda:
                    print("El hechizo causa:", daño, "puntos de daño",
                          "dejando la vida del enemigo", enemigo[15], "en:", vidaEnemigo)
        else:
            if visualizarRonda:
                print(
                    "El ataque magico no ha surtido efecto debido a la defensa del oponente")

    elif probHechizoHeroe <= heroe[5] and not numeroHechizo >= heroe[4]:
        if visualizarRonda:
            print(
                "El hechizo no ha podido lanzarse debido a que no se ha superado el umbral de hechizo")

    elif heroe[5] < probHechizoHeroe <= heroe[6] and numeroHechizo >= heroe[4]:
        numeroHechizo2 = randint(1, 20)
        if numeroHechizo2 == 20:
            if visualizarRonda:
                print("EL HEROE LANZA UN HECHIZO DE DEFENSA CRITICO!!")
            defensaHeroe += 2
            if visualizarRonda:
                print(
                    "como resultado, el HEROE aumenta su defensa en 2, dejando su defensa en:", defensaHeroe)
            contadorCriticos += 1
        elif numeroHechizo2 == 1:
            if visualizarRonda:
                print("EL HECHIZO DE DEFENSA HA FALLADO")
            defensaEnemigo += 1
            if visualizarRonda:
                print("como resultado, aumenta en 1 la defensa del enemigo",
                      enemigo[15])
                print("la defensa del ENEMIGO aumenta a:", defensaEnemigo)
            contadorFallos += 1
        elif numeroHechizo2 != 20 and numeroHechizo != 1:
            if visualizarRonda:
                print("Heroe lanza hechizo de defensa")
            defensaHeroe += 1
            if visualizarRonda:
                print("La defensa del HEROE aumenta en 1, quedando en:", defensaHeroe)
    elif heroe[5] < probHechizoHeroe <= heroe[6] and not numeroHechizo >= heroe[4]:
        if visualizarRonda:
            print(
                "El hechizo no ha podido lanzarse debido a que no se ha superado el umbral de hechizo")

    elif heroe[6] < probHechizoHeroe <= heroe[7] and numeroHechizo >= heroe[4]:
        numeroHechizo2 = randint(1, 20)
        if numeroHechizo2 == 20:
            if visualizarRonda:
                print("EL HEROE LANZA UN HECHIZO DE CURACION CRITICO!!")
            vidaHeroe += 4
            if vidaHeroe > heroe[0]:
                vidaHeroe = heroe[0]
            if visualizarRonda:
                print("como resultado, el HEROE aumenta su vida en 4 puntos")
                print("la vida actual del HEROE queda en:", vidaHeroe)
            contadorCriticos += 1
        elif numeroHechizo2 == 1:
            if visualizarRonda:
                print("EL HECHIZO DE CURACION HA FALLADO")
            vidaEnemigo += 4
            if vidaEnemigo > enemigo[0]:
                vidaEnemigo = enemigo[0]
            if visualizarRonda:
                print("como consecuencia, el HEROE aumenta la vida del enemigo",
                      enemigo[15], "en 4 puntos")
                print("la vida del enemigo es:", vidaEnemigo)
            contadorFallos += 1
        elif numeroHechizo2 != 20 and numeroHechizo2 != 1:
            if visualizarRonda:
                print("El HEROE lanza hechizo de curacion normal")
            numeroCuracion = randint(1, 8)
            vidaHeroe += numeroCuracion
            if vidaHeroe > heroe[0]:
                vidaHeroe = heroe[0]
            if visualizarRonda:
                print("Como resultado la vida del HEROE aumenta en:",
                      numeroCuracion, "quedando su vida en:", vidaHeroe)
    elif heroe[6] < probHechizoHeroe <= heroe[7] and not numeroHechizo >= heroe[4]:
        if visualizarRonda:
            print(
                "El hechizo no ha podido lanzarse debido a que no se ha superado el umbral de hechizo")

    elif probHechizoHeroe > heroe[7] and probHechizoHeroe <= 100:
        numeroAtaque = randint(1, 20)
        ataqueFisico = heroe[2]+numeroAtaque
        if visualizarRonda:
            print("El HEROE se avalanza para realizar un ataque físico")
        if ataqueFisico >= enemigo[3]:
            if numeroAtaque == 20:
                if visualizarRonda:
                    print(
                        "El HEROE RELIZA UN ATAQUE FÍSICO DESGARRADOR, GOLPE CRITICO!!")
                daño = (randint(heroe[8], heroe[9]))*2
                vidaEnemigo -= daño
                if visualizarRonda:
                    print("El HEROE quita", daño,
                          "puntos de vida al enemigo", enemigo[15], "dejando su vida en:", vidaEnemigo)
                contadorCriticos += 1
            elif numeroAtaque == 1:
                if visualizarRonda:
                    print("EL GOLPE HA FALLADO")
                dañoPropio = randint(1, 3)
                if visualizarRonda:
                    print("Como resultado, el HEROE hace",
                          dañoPropio, "puntos de daño a sí mismo")
                vidaHeroe -= dañoPropio
                if visualizarRonda:
                    print("La vida del HEROE queda en:", vidaHeroe)
                contadorFallos += 1
            elif ataqueFisico >= enemigo[3] and numeroAtaque != 20 and numeroAtaque != 1:
                if visualizarRonda:
                    print("El HEROE realiza un ataque fisico normal")
                daño = randint(heroe[8], heroe[9])
                vidaEnemigo -= daño
                if visualizarRonda:
                    print("El ataque del HEROE hace", daño,
                          "puntos de daño sobre el enemigo", enemigo[15], "dejando su vida en:", vidaEnemigo)
        else:
            if visualizarRonda:
                print("El ataque no ha surtido efecto debido a la defensa del oponente")

    enemigo[0] = vidaEnemigo
    heroe[0] = vidaHeroe
    enemigo[3] = defensaEnemigo
    heroe[3] = defensaHeroe

    return[heroe, enemigo, contadorCriticos, contadorFallos]


def ataqueEnemigo(heroe, enemigo):
    vidaEnemigo = enemigo[0]
    vidaHeroe = heroe[0]
    defensaHeroe = heroe[3]
    defensaEnemigo = enemigo[3]
    probHechizoEnemigo = randint(1, 100)
    numeroHechizoE = randint(1, 20)
    if probHechizoEnemigo <= enemigo[5] and numeroHechizoE >= enemigo[4]:
        numeroHechizo2E = randint(1, 20)
        if numeroHechizo2E >= heroe[3]:
            if numeroHechizo2E == 20:
                print("¡¡El enemigo", enemigo[15],
                      "LANZA UN ATAQUE MAGICO CRITICO!!")
                dañoHechizoE = (randint(enemigo[8], enemigo[9]))*1.5
                print("El daño causado por el hechizo es", dañoHechizoE)
                vidaHeroe -= dañoHechizoE
                print(
                    "El ataque del enemigo", enemigo[15], "disminuye la vida del HEROE a:", vidaEnemigo)
            elif numeroHechizo2E == 1:
                print("EL ATAQUE MAGICO HA FALLADO")
                dañoPropioE = randint(1, 3)
                print("El enemigo", enemigo[15], "se causa daño a si mismo de:",
                      dañoPropioE, "puntos")
                vidaEnemigo -= dañoPropioE
                print("La vida del enemigo",
                      enemigo[15], "baja a:", vidaEnemigo)
            elif numeroHechizo2E >= heroe[3] and numeroHechizo2E != 20 and numeroHechizo2E != 1:
                dañoE = randint(enemigo[8], enemigo[9])
                print("El enemigo",
                      enemigo[15], "realiza un hechizo de ataque magico normal")
                vidaHeroe -= dañoE
                print("El hechizo causa:", dañoE, "puntos de daño",
                      "dejando la vida del HEROE en:", vidaHeroe)
        else:
            print(
                "El ataque magico no ha surtido efecto debido a la defensa del oponente")

    elif probHechizoEnemigo <= enemigo[5] and not numeroHechizoE >= enemigo[4]:
        print("El hechizo no ha podido lanzarse debido a que no se ha superado el umbral de hechizo")

    elif enemigo[5] < probHechizoEnemigo <= enemigo[6] and numeroHechizoE >= enemigo[4]:
        numeroHechizo2E = randint(1, 20)
        if numeroHechizo2E == 20:
            print("EL enemigo", enemigo[15],
                  "LANZA UN HECHIZO DE DEFENSA CRITICO!!")
            defensaEnemigo += 2
            print(
                "como resultado, el enemigo", enemigo[15], "aumenta su defensa en 2, dejando su defensa en:", defensaEnemigo)
        elif numeroHechizo2E == 1:
            print("EL HECHIZO DE DEFENSA HA FALLADO")
            defensaHeroe += 1
            print("como resultado, aumenta en 1 la defensa del HEROE")
            print("la defensa del HEROE aumenta a:", defensaHeroe)
        elif numeroHechizo2E != 20 and numeroHechizo2E != 1:
            print("el enemigo", enemigo[15], "lanza hechizo de defensa")
            defensaEnemigo += 1
            print("La defensa del enemigo",
                  enemigo[15], "aumenta en 1, quedando en:", defensaEnemigo)

    elif enemigo[5] < probHechizoEnemigo <= enemigo[6] and not numeroHechizoE >= enemigo[4]:
        print("El hechizo no ha podido lanzarse debido a que no se ha superado el umbral de hechizo")

    elif enemigo[6] < probHechizoEnemigo <= enemigo[7] and numeroHechizoE >= enemigo[4]:
        numeroHechizo2E = randint(1, 20)
        if numeroHechizo2E == 20:
            print("EL enemigo", enemigo[15],
                  "LANZA UN HECHIZO DE CURACION CRITICO!!")
            print("como resultado, el enemigo",
                  enemigo[15], "aumenta su vida en 4 puntos")
            vidaEnemigo += 4
            if vidaEnemigo > enemigo[0]:
                vidaEnemigo = enemigo[0]
            print("la vida actual del enemigo",
                  enemigo[15], "queda en:", vidaEnemigo)
        elif numeroHechizo2E == 1:
            print("EL HECHIZO DE CURACION HA FALLADO")
            print("como consecuencia, el enemigo",
                  enemigo[15], "aumenta la vida del HEROE en 4 puntos")
            vidaHeroe += 4
            if vidaHeroe > heroe[0]:
                vidaHeroe = heroe[0]
            print("la vida del HEROE actual es:", vidaHeroe)
        elif numeroHechizo2E != 20 and numeroHechizo2E != 1:
            print("El enemigo", enemigo[15],
                  "lanza hechizo de curacion normal")
            numeroCuracion = randint(1, 8)
            vidaEnemigo += numeroCuracion
            if vidaEnemigo > enemigo[0]:
                vidaEnemigo = enemigo[0]
            print("Como resultado la vida del enemigo", enemigo[15], "aumenta en:",
                  numeroCuracion, "quedando su vida en:", vidaEnemigo)

    elif enemigo[6] < probHechizoEnemigo <= enemigo[7] and not numeroHechizoE >= enemigo[4]:
        print("El hechizo no ha podido lanzarse debido a que no se ha superado el umbral de hechizo")

    elif probHechizoEnemigo > enemigo[7] and probHechizoEnemigo <= 100:
        numeroAtaqueE = randint(1, 20)
        ataqueFisicoE = enemigo[2]+numeroAtaqueE
        print("El enemigo", enemigo[15],
              "se avalanza para realizar un ataque físico")
        if ataqueFisicoE >= heroe[3]:
            if numeroAtaqueE == 20:
                print(
                    "El enemigo", enemigo[15], "REALIZA UN ATAQUE FÍSICO DESGARRADOR, GOLPE CRITICO!!")
                dañoE = (randint(enemigo[8], enemigo[9]))*2
                vidaHeroe -= dañoE
                print("El enemigo", enemigo[15], "quita", dañoE,
                      "puntos de vida al HEROE, dejando su vida en:", vidaHeroe)
            elif numeroAtaqueE == 1:
                print("EL GOLPE HA FALLADO")
                dañoPropioE = randint(1, 3)
                print("Como resultado, el enemigo", enemigo[15], "hace",
                      dañoPropioE, "puntos de daño a sí mismo")
                vidaEnemigo -= dañoPropioE
                print("La vida del enemigo",
                      enemigo[15], "queda en:", vidaEnemigo)
            elif ataqueFisicoE >= heroe[3] and numeroAtaqueE != 20 and numeroAtaqueE != 1:
                print("El enemigo", enemigo[15],
                      "realiza un ataque fisico normal")
                dañoE = randint(enemigo[8], enemigo[9])
                vidaHeroe -= dañoE
                print("El ataque del enemigo", enemigo[15], "hace", dañoE,
                      "puntos de daño sobre el HEROE, dejando su vida en:", vidaHeroe)
        else:
            print("El ataque no ha surtido efecto debido a la defensa del oponente")

    enemigo[0] = vidaEnemigo
    heroe[0] = vidaHeroe
    enemigo[3] = defensaEnemigo
    heroe[3] = defensaHeroe

    return[heroe, enemigo]


def experienciaYEstadisticas(heroe, balanceEnemigos, vida, contadorCriticos, contadorFallos):
    i = 0
    while i < len(balanceEnemigos):
        if balanceEnemigos[i][13] == 1:
            Experiencia = (4*(balanceEnemigos[i][12])**3)/5
            balanceEnemigos[i][14] = Experiencia
        elif balanceEnemigos[i][13] == 2:
            Experiencia = (balanceEnemigos[i][12])**3
            balanceEnemigos[i][14] = Experiencia
        elif balanceEnemigos[i][13] == 3:
            Experiencia = (5*(balanceEnemigos[i][12])**3)/4
            balanceEnemigos[i][14] = Experiencia
        i = i+1
    sumaExp = 0
    k = 0
    while k < len(balanceEnemigos):
        sumaExp += balanceEnemigos[k][14]
        k = k+1
    j = 0
    sumaNivelesOp = 0
    while j < len(balanceEnemigos):
        sumaNivelesOp += balanceEnemigos[j][12]
        j = j+1
    contadorCriticos = contadorCriticos
    contadorFallos = contadorFallos
    if (contadorCriticos-contadorFallos) > 0:
        factorCrit = 1.5
    elif (contadorCriticos-contadorFallos) == 0:
        factorCrit = 1.0
    elif (contadorCriticos-contadorFallos) < 0:
        factorCrit = 0.75
    factorDaño = vida[0]/vida[1]
    nivelPersonaje = heroe[12]
    experienciaObtenida = (
        (sumaExp*(sumaNivelesOp/nivelPersonaje)*factorCrit*(1+factorDaño)))/7
    return experienciaObtenida


def evolucionAtributosH(heroe, experienciaObtenida):
    heroe[14] += round(experienciaObtenida)
    nivelActual = heroe[12]
    if heroe[13] == 3:
        heroe[12] = round(((heroe[14]*4)/5)**(1/3))
        if heroe[12] > nivelActual:
            print(
                "El nivel del heroe aumenta debido a la victoria, el nivel actual del heroe es:", heroe[12])
            j = 0
            while j < len(heroe):
                if j == 1 or j == 4 or j == 5 or j == 6 or j == 7 or j == 12 or j == 13 or j == 14:
                    j = j+1
                else:
                    heroe[j] += round((heroe[j]*1250000)/1000000)*(heroe[12]-1)
                    j = j+1
    elif heroe[13] == 4:
        heroe[12] = round(((heroe[14]*4)/7)**(1/3))
        if heroe[12] > nivelActual:
            print(
                "El nivel del heroe aumenta debido a la victoria en la ronda, el nivel actual del heroe es:", heroe[12])
            k = 0
            while k < len(heroe):
                if k == 1 or k == 4 or k == 5 or k == 6 or k == 7 or k == 12 or k == 13 or k == 14:
                    k = k+1
                else:
                    heroe[k] += round((heroe[k]*1750000)/1000000)*(heroe[12]-1)
                    k = k+1
    return heroe


def ataqueYGauges(listaGauges, enemigos, heroe):
    gauges = listaGauges[:]
    listaEnemigos = enemigos[:]
    listaHeroe = heroe[:]
    criticosYFallos = [0, 0]

    i = 0
    while i < len(gauges):
        if gauges[i] != "derrotado":
            if gauges[i] >= 10:
                if i == 0:
                    if visualizarRonda:
                        print("HEROE realiza su accion")
                    enemigo = randint(0, len(enemigos)-1)
                    while listaGauges[enemigo+1] == "derrotado":
                        enemigo = randint(0, len(enemigos)-1)
                    ataque = ataqueHeroe(listaHeroe, listaEnemigos[enemigo])
                    enemigos = ataque[1]
                    heroe = ataque[0]
                    gauges[0] = 0
                    criticosYFallos[0] = ataque[2]
                    criticosYFallos[1] = ataque[3]

                    vidaEnemigos = checkearVidaEnemigos(
                        gauges[:], listaEnemigos[:], heroe[:])
                    gauges = vidaEnemigos[0]
                    if visualizarRonda:
                        time.sleep(3)
                else:
                    if visualizarRonda:
                        print("El enemigo",
                              listaEnemigos[i-1][15], "realiza su accion")
                    ataqueE = ataqueEnemigo(listaHeroe[:], listaEnemigos[i-1])
                    listaEnemigos[i-1] = ataqueE[1]
                    listaHeroe = ataqueE[0]
                    gauges[i] = 0
                    if listaHeroe[0] <= 0:
                        i = 10
                    if visualizarRonda:
                        time.sleep(3)
        i = i+1

    return [gauges, listaEnemigos, listaHeroe, criticosYFallos]


def elejirVisualizar():
    global visualizarRonda

    print('Ingrese "1" para visualizar la ronda, o "2" para ir directamente a los resultados.')
    continuar = True
    while continuar:
        visualizar = input("Eleccion: ")
        if not visualizar.isdigit():
            print("Error. Por favor ingrese un numero valido. ")
        elif int(visualizar) < 1 or int(visualizar) > 2:
            print("Error. Por favor ingrese un numero entre 1 y 2. ")
        else:
            continuar = False
    visualizar = int(visualizar)

    if visualizar == 1:
        visualizarRonda = True
    else:
        visualizarRonda = False

# Funcion combate:
# Funcion que genera el flujo del combate, añadiendo intervalos de tiempo y turnos de ataque.
# Entrada: listas de enteros, una con los atributos del Heroe y otra con los del enemigo.
# Salida: string indicador de barra de carga para cada personaje, ademas de su accion cuando sea pertinente.
# En este ciclo es donde se encuentra el iterador para cargar los gauges de ambos personajes, dentro de esta funcion-
# invocamos las funciones de ataque definidas para cada personaje anteriormente, cuando sea pertinente(gauge del heroe o enemigo sean mayores o iguales a 10).
# Ademas de lo anterior, al inicio de la funcion "Combate", definimos las estadisticas que necesitan utilizar las funciones y el ciclo while principal,
# para que puedan ser modificadas por las funciones, como lo son la vida y defensa de ambos personajes.


def combate(heroe, balanceEnemigos):
    estadisticasIniciales = heroe[:]

    contadorCriticos = 0
    contadorFallos = 0

    enemigosVivos = True

    listaGauges = [0]
    i = 0
    while i < len(balanceEnemigos):
        listaGauges.append(0)
        i = i+1

    i = 0

    elejirVisualizar()

    while heroe[0] > 0 and enemigosVivos:
        listaGauges = cargaGauges(
            listaGauges, heroe, balanceEnemigos)
        time.sleep(1)
        resultadoAtaque = ataqueYGauges(listaGauges, balanceEnemigos, heroe)

        listaGauges = resultadoAtaque[0]
        balanceEnemigos = resultadoAtaque[1]
        heroe = resultadoAtaque[2]

        contadorCriticos += resultadoAtaque[3][0]
        contadorFallos += resultadoAtaque[3][1]

        checkVidas = checkearVidaEnemigos(
            listaGauges[:], balanceEnemigos, heroe)

        listaGauges = checkVidas[0]
        enemigosVivos = checkVidas[1]

        i += 1

    if heroe[0] <= 0:
        print("El heroe ha muerto.")
    elif enemigosVivos == False:
        print("El heroe ha derrotado a todos los enemigos.")
        vida = [estadisticasIniciales[0], heroe[0]]
        print(vida)
        xp = experienciaYEstadisticas(
            heroe, balanceEnemigos, vida, contadorCriticos, contadorFallos)
        print("La experiencia obtenida al vencer la ronda es:", round(xp))
        time.sleep(2)
        print(heroe)

        cambioEstadisticasH = evolucionAtributosH(estadisticasIniciales, xp)
        heroe = cambioEstadisticasH
        print(heroe)

    return(heroe)


def juegazo(heroe):
    continuar = True
    while continuar:
        numeroRondas = input("Ingrese el numero de rondas: ")
        if not numeroRondas.isdigit():
            print("Error. Por favor ingrese un numero valido. ")
        elif int(numeroRondas) < 1:
            print("Error. Por favor ingrese un numero entero positivo.")
        else:
            continuar = False
    numeroRondas = int(numeroRondas)

    i = 1
    while i < numeroRondas+1:
        print("||Preparando enemigos||")
        timer()
        enemigos = eleccionEnemigo()
        enemigos = balanceoNiveles(heroe, enemigos)
        timer()
        print("||Iniciando procesos...||")
        print("La ronda", i, "comenzara en 5 ticks")
        timer()
        print("¡¡¡||COMIENZA LA BATALLA||!!!!")
        heroe = combate(heroe, enemigos)
        i = i+1


# --- Bloque Principal ---
introduccion()
# ENTRADA:
heroe = eleccionHeroe()
timer()
# PROCESAMIENTO-SALIDA:
juegazo(heroe)
