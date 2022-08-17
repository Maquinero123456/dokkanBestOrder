from characterSearch import characterSearch
from teamOptimizer import teamOptimizer

#Search characters codes at https://dokkan.fyi/characters

def main(): 

    #Introduce character to search
    personajesABuscar= []
    while len(personajesABuscar)<6:
        aux = input("Character number "+str(len(personajesABuscar)+1)+":").strip()
        try:
            if(aux==""):
                print("Character cant be empty")
            else:
                personajesABuscar.append(int(aux))
        except ValueError:
            print("You must introduce character code with just numbers")

    #Introduce friend
    friend=""
    while(friend==""):
        aux = input("Friend(Leave blank to repeat leader): ").strip()
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
        print("Character "+str(i+1)+" doesn't exist or wrong code")
        quit()

    #Show searched characters
    print("PERSONAJES:")
    for i in range(len(personajes)):
        print(str(i+1)+". "+personajes[i][0])

    #Create perfect team
    timoOptimizar = teamOptimizer(personajes)
    optimizado = timoOptimizar.optimizador()
    #Show perfect team
    print("EQUIPO PERFECTO:")
    for i in range(len(optimizado)):
        print(str(i+1)+". "+optimizado[i][0])

if __name__ == "__main__":
    main()
