from numpy import*

def egalite(position1, position2):
        return ((position1[0] + position1[1]) == (position2[0] + position2[1]))

def sequencePlusProbable(sequenceB):#elle définit la séquence la plus probable à partir
                                     # de la séquence biaisée.
        listeP = []
        for k in range(0, len(sequenceB)):
            listeP.append(sequenceB[k][0][0])
        return listeP
        
def conversion(position):
        return position[0] + position[1] - 3
        
class Gabriel:
    
    nbreDeNote = 7 # bon, il y'a 7 notes, de do à si.
    
    classeDequivalence = {} # là je définis les classes d'équivalence, c'est à dire les notes
    for k in range(1,8):    # et les différentes façons de les jouer.
        classeDequivalence[k] = []
    for k in range(1,8):
        for j in range(1,6):
                if 4 <= k+j < 11:
                    classeDequivalence[ (k + j - 3 )] += [[k,j]] 
    
    def __init__(self, sequenceR, sequenceB, memoire, sequenceJ, etat):
        self.sequenceReelle = sequenceR    # la vraie séquence de notes
        self.sequenceBiaisee = sequenceB   # les séquences qu'il perçoit avec probabilité                                  #( c'est une liste de liste de couple (position, proba))
        self.memoire = memoire             # sa mémoire
        self.sequenceJouee = sequenceJ     # ce qu'il nous joue, avec vide c'est le repos
        self.etat = etat                   # un booléen qui nous dit si c'est bon ou pas
    
    def actualiser(self):                   # on actualise la valeur du booléen
         self.etat = (self.sequenceJouee == self.sequenceReelle)
        
    
    def premiereErreure(self):             # retourne le rang de la première erreure.
        k = 0
        while(k < len(self.sequenceReelle)):
            if (egalite(self.sequenceReelle[k], self.sequenceJouee[k])):
                 k += 1
            else :
                break
        return k
        
    
    
    def apprentissage(self) :
        self.sequenceJouee = sequencePlusProbable(self.sequenceBiaisee)
        self.actualiser()
        if not(self.etat):
            k = self.premiereErreure()
            del self.sequenceBiaisee[k][0]
            if (egalite(self.sequenceReelle[k], self.sequenceBiaisee[k][0][0])):
                memoire[conversion(self.sequenceBiaisee[k][0][0])]           [conversion(self.sequenceReelle[k])] += 1
            print("j'ai corrigé une bêtise que j'ai faite à la ", k, "ième note")
            self.apprentissage()

l1 = [[4,4]]
l2 = [[([4,3],90),([4,4],10)]]
memoire = eye(7,7)
x = Gabriel(l1, l2, memoire, [[4,3]], False)
x.apprentissage()

