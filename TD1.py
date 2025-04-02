liste = list()
f = open("frenchssaccent.dic",'r')
for ligne in f:
    liste.append(ligne[0:len(ligne)-1])
f.close()

#on part du mot du lexique et on regarde si on peut le former
def mot_le_plus_long(tirage,mots_possibles):
    mot_max = ''
   
    for mot in mots_possibles:
        if len(mot) > len(mot_max):
            lettres_disponibles = list(tirage) #copie de tirage
            peut_etre_forme = True 
        
            for lettre in mot:
                if lettre in lettres_disponibles: #on regarde si les lettres du mot sont dans notre liste
                    lettres_disponibles.remove(lettre) #si oui on enlève cette lettre de nos lettres diponibles
                
                else:
                    peut_etre_forme = False #si on ne peut pas former le mot car la lettre n'est pas dans notre liste, on arrete
                    break
        
            if peut_etre_forme: 
                mot_max = mot
    return mot_max

#tirage = ['a', 'r', 'b', 'g', 'e', 's', 'c', 'j']
#print(mot_le_plus_long(tirage,liste))

#pour comptabiliser les points on définit un dictionnaire
points_mot = {'a' : 1, 'b' : 3, 'c' : 3, 'd' : 2, 'e' : 1, 'f' : 4, 'g' : 2, 'h' : 4,
              'i' : 1, 'j' : 8, 'k' : 10, 'l' : 1, 'm' : 2, 'n' : 1, 'o' : 1, 'p': 3, 'q': 8,
              'r' : 1, 's' : 1, 't' : 1, 'u' : 1, 'v' : 4, 'w' : 10, 'x' : 10, 'y' : 10, 'z' : 10}
#compte le score d'un mot
def score(mot):
    score = 0
    for lettre in mot:
        score = score + points_mot[lettre]
    return score

#mot = 'apagnan'
#print(score(mot))
#print(score('lettre'))  
#print(score(''))      

#compte le score d'une liste de mot 
def max_score(liste_mot):
    max_score = 0
    m = ''
    for mot in liste_mot: 
        score_mot = score(mot)
        if score_mot > max_score:
            max_score = score_mot
            m = mot
    return max_score,m

#liste_mot = ['rte', 'ver', 'ce', 'etc', 'cet', 'ex', 'cr', 'et', 'ter', 'te', 'ct']
#print(max_score(liste_mot))        
  
#les programmes ci-dessous ne renvoient pas les mêmes valeurs. Je n'ai pas trouvé l'erreur, que je pense être dans le mot_score_max1
def mot_score_max2(tirage,mots_possibles):
    mot_max = ''
    s = score(mot_max)
    for mot in mots_possibles:
        if len(mot) > len(mot_max) and score(mot)>s:
            lettres_disponibles = list(tirage) #copie de tirage
            peut_etre_forme = True 
        
            for lettre in mot:
                if lettre in lettres_disponibles: #on regarde si les lettres du mot sont dans notre liste
                    lettres_disponibles.remove(lettre) #si oui on enlève cette lettre de nos lettres diponibles
                
                else:
                    peut_etre_forme = False #si on ne peut pas former le mot car la lettre n'est pas dans notre liste, on arrete
                    break
        
            if peut_etre_forme: 
                mot_max = mot
                s = score(mot_max)
    return mot_max,s

tirage = ['a', 'r', 'b', 'g', 'e', 's', 'c', 'j']
print(mot_score_max2(tirage,liste))




#on améliore le modèle en comptabilisant les points
def mot_score_max1(tirage,mots_possibles):
    M = list()
    #on forme la liste des mots que l'on peut former, M
    for mot in mots_possibles:
        lettres_disponibles = list(tirage)
        peut_etre_forme = True 
        
        for lettre in mot:
            if lettre in lettres_disponibles: #on regarde si les lettres du mot sont dans notre liste
                lettres_disponibles.remove(lettre) #on enlève cette lettre de nos lettres diponibles
                
            else:
                peut_etre_forme = False #si on ne peut pas former le mot, la lettre n'est pas dans notre liste, on arrete
                break
        
        if peut_etre_forme:
            M.append(mot)
    
    score_max,mot = max_score(M)
    return(score_max,mot)
    
    
tirage = ['a', 'r', 'b', 'g', 'e', 's', 'c', 'j']
print(mot_score_max1(tirage,liste))
    
    
    
    
    
    
    
    
    

