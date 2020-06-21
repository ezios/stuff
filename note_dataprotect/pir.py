### PIR private information retrieval POC . 2 serveurs

import random
import string

def randomIndex(ListSize,interval):
    randomlist = []
    for i in range(ListSize):
        n = random.randint(interval[0],interval[1])
        randomlist.append(n)
    return randomlist


def listxor(liste):
    xored = liste[0]
    for i in range(1,len(liste)):
        xored=xored^liste[i]
    return xored



###Client
# deux ensembles de meme taille   
# E1 est identique à E2 à la différence qu'il contient l'élément i à rechercher, ici i =54  
E1 = randomIndex(ListSize=30,interval=(0,99))

E2 = [elements for elements in E1]
E2.append(54)
print("E1 : {} \nE2 {} : ".format(E1,E2))
print("élément à chercher : ",string.printable[54])

# L'envoi des éléments vers les serveurs se fait de manière aléatoire
#L'inconnu résidera dans le fait que les deux serveurs S1 et S2 ne communiquent pas..
random.shuffle(E1)
random.shuffle(E2)
E3 = E1 + E2
print("Ordre d'envoi aléatoire: ",E3)
lim = len(E3)
to_s1 = E3[0:int(lim/2)]
to_s2 = E3[int(lim/2):lim]

print("éléments envoyés à S1: ",to_s1)
print("éléments envoyés à S2: ",to_s2)
#Serveur1
#Supposons que la base de donnée est l'ensemble des caractères imprimables 
#On recherche tout les éléments d'index : les index envoyés par le client"""
databaseserv1 = list(string.printable)
current_request = []
for request_index in to_s1:
    #ord sert à transformer la lettre en entier 
    current_request.append(ord(databaseserv1[request_index]))
#On fait un xor de tout les éléments
Serv1Response= listxor(current_request)



###Serveur2
#meme procedure que pour le serveur1
databaseserv2 = list(string.printable)
current_request = []
for request_index in to_s2:
    current_request.append(ord(databaseserv2[request_index]))

Serv2Response = listxor(current_request)

### le client reçoit les deux réponse et fait un xor entre les deux réponses pour trouver la réponse
print("Réponse serveur 1 : ",Serv1Response)
print("Réponse serveur 2 : ",Serv2Response)
response = Serv2Response ^ Serv1Response
print("Réponse calculée par le client: ",chr(response))
