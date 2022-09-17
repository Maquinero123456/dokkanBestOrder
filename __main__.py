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

    #Search characters
    personajes = []
    search = characterSearch()

    cprint("Personajes a buscar:", "green")
    #Introduce character to search
    while len(personajes)<6:
        if(len(personajes)==0):
            cprint("Personaje "+str(len(personajes)+1)+"(Lider):", "green", end = " ")
        else:
            cprint("Personaje "+str(len(personajes)+1)+":", "green", end = " ")
        aux = input().strip()
        try:
            if(aux==""):
                cprint("No puede estar vacio", "red")
            else:
                personaje = search.buscarPersonaje(int(aux))
                if personaje in personajes:
                    raise AttributeError("")
                personajes.append(personaje)
                cprint(personajes[len(personajes)-1][0], "yellow")
        except ValueError:
            cprint("Solo introducir numeros", "red")
        except TypeError:
            cprint("Personaje "+aux+" no existe o id mal", "red")
        except AttributeError:
            cprint("Personaje repetido", "red")

    #Introduce friend
    while len(personajes)<7:
        cprint("Amigo(Deja en blanco para repetir lider): ", "green", end = " ")
        aux = input().strip()
        try:
            if(aux==""):
                personajes.append(personajes[0])
            else:
               personajes.append(search.buscarPersonaje(int(aux)))
            cprint(personajes[6][0], "yellow")
        except TypeError:
            cprint("Solo introducir numeros", "red")
        except TypeError:
            cprint("Personaje "+aux+" no existe o id mal", "red")

    #Show searched characters
    cprint("\nPERSONAJES:", "green")
    for i in range(len(personajes)):
        cprint(str(i+1)+".", "green", end = " ")
        print(personajes[i][0])

    #Create perfect team
    timoOptimizar = teamOptimizer(personajes)
    optimizado = timoOptimizar.optimizador()
    #Show perfect team
    cprint("\nEQUIPO PERFECTO:", "green")
    for i in range(len(optimizado)):
        cprint(str(i+1)+".", "green", end = " ")
        print(optimizado[i][0])

    cprint("\nPresiona enter para cerrar...", "green", end=" ")
    input()
    exit(0)

if __name__ == "__main__":
    main()
