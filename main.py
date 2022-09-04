from characterSearch import characterSearch
from teamOptimizer import teamOptimizer
from termcolor import colored, cprint
import signal
import sys

def signal_handler(sig, frame):
    cprint('\nSaliendo...', "red")
    sys.exit(0)

def main():
    signal.signal(signal.SIGINT, signal_handler)
    cprint("Busca los codigos de personajes en https://dokkan.fyi/characters\n", "green")

    cprint("Personajes a buscar:", "green")
    #Introduce character to search
    personajesABuscar= []
    while len(personajesABuscar)<6:
        if(len(personajesABuscar)==0):
            cprint("Personaje "+str(len(personajesABuscar)+1)+"(Lider):", "green", end = " ")
        else:
            cprint("Personaje"+str(len(personajesABuscar)+1)+":", "green", end = " ")
        aux = input().strip()
        try:
            if(aux==""):
                cprint("No puede estar vacio", "red")
            else:
                personajesABuscar.append(int(aux))
        except ValueError:
            cprint("Solo introducir numeros", "red")

    #Introduce friend
    friend=""
    while(friend==""):
        cprint("Amigo(Deja en blanco para repetir lider): ", "green", end = " ")
        aux = input().strip()
        try:
            if(aux==""):
                friend = personajesABuscar[0]
            else:
               friend = int(aux)
        except TypeError:
            cprint("Solo introducir numeros", "red")
    personajesABuscar.append(friend)

    #Search characters
    personajes = []
    search = characterSearch()
    try:
        for i in range(len(personajesABuscar)):
            personajes.append(search.buscarPersonaje(personajesABuscar[i]))
    except ValueError:
        cprint("Personaje "+str(i+1)+" no existe o id mal", "red")
        quit()

    #Show searched characters
    cprint("PERSONAJES:", "green")
    for i in range(len(personajes)):
        cprint(str(i+1)+".", "green", end = " ")
        print(personajes[i][0])

    #Create perfect team
    timoOptimizar = teamOptimizer(personajes)
    optimizado = timoOptimizar.optimizador()
    #Show perfect team
    cprint("EQUIPO PERFECTO:", "green")
    for i in range(len(optimizado)):
        cprint(str(i+1)+".", "green", end = " ")
        print(optimizado[i][0])

if __name__ == "__main__":
    main()
