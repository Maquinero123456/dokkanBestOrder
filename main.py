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
    cprint("\nSearch characters codes at https://dokkan.fyi/characters\n", "green")

    cprint("Character to search:", "green")
    #Introduce character to search
    personajesABuscar= []
    while len(personajesABuscar)<6:
        cprint("Character number "+str(len(personajesABuscar)+1)+":", "green", end = " ")
        aux = input().strip()
        try:
            if(aux==""):
                cprint("Character cant be empty", "red")
            else:
                personajesABuscar.append(int(aux))
        except ValueError:
            cprint("You must introduce character code with just numbers", "red")

    #Introduce friend
    friend=""
    while(friend==""):
        cprint("Friend(Leave blank to repeat leader): ", "green", end = " ")
        aux = input().strip()
        try:
            if(aux==""):
                friend = personajesABuscar[0]
            else:
               friend = int(aux)
        except TypeError:
            print("You must introduce character code with just numbers or must be non empty")
    personajesABuscar.append(friend)

    #Search characters
    personajes = []
    search = characterSearch()
    try:
        for i in range(len(personajesABuscar)):
            personajes.append(search.buscarPersonaje(personajesABuscar[i]))
    except ValueError:
        cprint("Character "+str(i+1)+" doesn't exist or wrong code", "red")
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
