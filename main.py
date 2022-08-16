from characterSearch import characterSearch
from teamOptimizer import teamOptimizer
#BUSCAR CODIGOS DE PERSONAJES EN https://dokkan.fyi/characters
def main(): 
    
    personajesABuscar= []
    while len(personajesABuscar)<6:
        personajesABuscar.append(input("Personaje a buscar numero "+str(len(personajesABuscar)+1)+":"))

    personajesABuscar.append(input("Personaje amigo: "))
    personajes = []

    search = characterSearch()

    for i in range(len(personajesABuscar)):
        personajes.append(search.buscarPersonaje(personajesABuscar[i]))
    print("PERSONAJES:")
    for i in range(len(personajes)):
        print(str(i)+". "+personajes[i][0])
    print("EQUIPO PERFECTO:")
    timoOptimizar = teamOptimizer(personajes)
    optimizado = timoOptimizar.optimizador()
    for i in range(len(optimizado)):
        print(str(i)+". "+optimizado[i][0])
    

if __name__ == "__main__":
    main()
