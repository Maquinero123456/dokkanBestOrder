import itertools

class teamOptimizer:
    def __init__(self, team):
        self.team = team
        self.links = self.checkLinks(team)

    def optimizador(self):
        teamList = list(self.team)
        leader = teamList[0]
        friend = teamList[6]
        slice = teamList[1:6]
        permutaciones = list(itertools.permutations(slice))
        for i in range(len(permutaciones)):
            rotacion = []
            rotacion+= [leader]
            rotacion+= permutaciones[i]
            rotacion+= [friend]
            links = self.checkLinks(rotacion)
            a, b = 0,0
            for i in range(len(links)):
                if(links[i]>self.links[i]):
                    a+=1
                elif(self.links[i]>links[i]):
                    b+=1

            if a > b :
                self.team = rotacion
                self.links = links


        return self.team

    def checkLinks(self, team : list) -> list:
        personajesList = team
        teamLinks = (self.linkComparator(personajesList[0][1], personajesList[1][1], personajesList[4][1]))
        teamLinks+=(self.linkComparator(personajesList[2][1], personajesList[3][1], personajesList[5][1]))
        teamLinks+=(self.linkComparator(personajesList[0][1], personajesList[1][1], personajesList[6][1]))
        teamLinks+=(self.linkComparator(personajesList[2][1], personajesList[3][1], personajesList[4][1]))
        teamLinks+=(self.linkComparator(personajesList[0][1], personajesList[1][1], personajesList[5][1]))
        teamLinks+=(self.linkComparator(personajesList[2][1], personajesList[3][1], personajesList[6][1]))
        return teamLinks

    def linkComparator(self, links1 : list, links2:list, links3:list) -> list:
        links = []
        a = 0
        if len(links1)>len(links2):
            for i in range(len(links1)):
                for j in range(len(links2)):
                    if links1[i] == links2[j]:
                        a+=1
        else:
            for i in range(len(links2)):
                for j in range(len(links1)):
                    if links1[j] == links2[i]:
                        a+=1
        links.append(a)
        a = 0
        if len(links2)>len(links3):
            for i in range(len(links2)):
                for j in range(len(links3)):
                    if links2[i] == links3[j]:
                        a+=1
        else:
            for i in range(len(links3)):
                for j in range(len(links2)):
                    if links2[j] == links3[i]:
                        a+=1
        links.append(a)
        return links