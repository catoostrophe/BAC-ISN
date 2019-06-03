import time
from random import *
from turtle import *
from tkinter import *
from tkinter.font import Font
from playsound import playsound
from PIL import ImageTk, Image

#PARTIE I - ENCHAINEMENT DES DIFFÉRENTS MINI-JEUX

#Enchainent du MORPION et PFC


def suite_PFC():
    global fenetre_PFC

    fenetre_PFC = Tk()  #création de la fenêtre

    fenetre_PFC.geometry('300x150')

    fenetre_PFC.title("Je m'ennuie.")  #titre

    myFont = Font(family="comic Sans MS", size=12)

    fenetre_PFC.label = Label(
        fenetre_PFC,
        text="Veux-tu jouer aux pierre,\nfeuille, ciseaux avec moi?",
        font=myFont).pack()

    fenetre_PFC.oui = Button(
        fenetre_PFC,
        text="oui",
        command=pierrefeuilleciseaux,
        width=10,
        height=1,
        bd=1,
        cursor="heart",
        activebackground="hot pink",
        font=myFont).pack(
            padx=15, side=LEFT)  #enchaine le pierre feuille ciseaux

    fenetre_PFC.non = Button(
        fenetre_PFC,
        text="non",
        state=DISABLED,
        width=10,
        height=1,
        bd=1,
        cursor="pirate",
        bg="red3",
        font=myFont).pack(
            padx=15, side=RIGHT)

    fenetre_PFC.mainloop()


#Echainement PFC et MASTERMIND


def suite_MM():
    print()
    print(
        "Oh oh! Vous avez trouvé un fichier avec un mot de passe! Heureusement que le hackeur a une mémoire nulle et a laissé des indices! Êtes vous prêt(e)?"
    )
    print()
    continuer = input("Écrivez 'oui' si vous êtes prêt(e) sinon 'non': ")
    if continuer == "non":
        print()
        print(
            "De peur, vous vous retirez. Votre ordinateur est maintenant complètement hacké. C'est dommage."
        )
        defaite()
    elif continuer == "oui":
        mastermind()  #initialise le MM
    else:
        print()
        print("Savez-vous lire?")
        print()
        suite_MM()


#Enchainement MM et PENDU


def suite_PENDU():
    print()
    print(
        "Vous y êtes presque! Il ne reste qu'à trouver le mot de passe final pour supprimer le fichier! Allez-vous y réussir?"
    )
    print()
    continuer = input("Écrivez 'oui' si vous êtes prêt(e) sinon 'non': ")
    if continuer == "non":
        print()
        print(
            "Oh! D'où vous refusez, si proche de votre objectif! Je vous oblige à jouer."
        )
        jeudupendu()  #initialise le PENDU
    elif continuer == "oui":
        jeudupendu()  #initialise le PENDU
    else:
        print()
        print("Savez-vous lire?")
        print()
        suite_PENDU()


#FONCTIONS VICTOIRE


def victoire():
    global sup1

    sup1 = Tk()

    sup1.geometry('300x150')

    sup1.title("Vous y êtes presque... :(")

    myFont = Font(family="comic sans MS", size=12)

    sup1.label = Label(
        sup1, text="Voulez-vous supprimer ce fichier?", font=myFont).pack()

    sup1.oui = Button(
        sup1,
        text="oui",
        command=supprimer2,
        width=10,
        height=1,
        bd=1,
        cursor="pirate",
        bg="red3",
        activebackground="red3",
        font=myFont).pack(
            padx=15, side=LEFT)

    sup1.non = Button(
        sup1,
        text="non",
        command=quit,
        width=10,
        height=1,
        bd=1,
        cursor="heart",
        activebackground="hot pink",
        font=myFont).pack(
            padx=15, side=RIGHT)

    sup1.mainloop()


def supprimer2():
    sup1.destroy()

    global sup2

    sup2 = Tk()

    sup2.geometry('400x150')

    sup2.title("Vraiment?")

    myFont = Font(family="comic sans MS", size=12)

    sup2.label = Label(
        sup2, text="Voulez-vous vraiment supprimer ce fichier?",
        font=myFont).pack()

    sup2.oui = Button(
        sup2,
        text="oui",
        command=supprimer3,
        width=10,
        height=1,
        bd=1,
        cursor="pirate",
        bg="red3",
        activebackground="red3",
        font=myFont).pack(
            padx=15, side=LEFT)

    sup2.non = Button(
        sup2,
        text="non",
        command=quit,
        width=10,
        height=1,
        bd=1,
        cursor="heart",
        activebackground="hot pink",
        font=myFont).pack(
            padx=15, side=RIGHT)

    sup2.mainloop()


def supprimer3():
    sup2.destroy()

    global sup3

    sup3 = Tk()

    sup3.geometry('500x150')

    sup3.title("Vraiment? :(")

    myFont = Font(family="comic sans MS", size=12)

    sup3.label = Label(
        sup3,
        text="Êtes vous 100% certain de vouloir supprimer ce fichier?",
        font=myFont).pack()

    sup3.oui = Button(
        sup3,
        text="oui",
        command=supprimer4,
        width=10,
        height=1,
        bd=1,
        cursor="pirate",
        bg="red3",
        activebackground="red3",
        font=myFont).pack(
            padx=15, side=LEFT)

    sup3.non = Button(
        sup3,
        text="non",
        command=quit,
        width=10,
        height=1,
        bd=1,
        cursor="heart",
        activebackground="hot pink",
        font=myFont).pack(
            padx=15, side=RIGHT)

    sup3.mainloop()


def supprimer4():

    sup3.destroy()

    global vicdef

    vicdef = Tk()

    vicdef.geometry('450x200')

    myFont = Font(family="comic sans MS", size=12)

    vicdef.title("Bravo!")

    vicdef.label = Label(
        vicdef,
        text=
        "Le fichier a efficacement été supprimé. \n Le hackeur est impressioné. \n Il vous envoie un message: 'À la prochaine mon coeur. ;)'",
        font=myFont).pack()

    vicdef.rejouer = Button(
        vicdef,
        text="REJOUER",
        command=recommencer,
        width=15,
        height=1,
        bd=1,
        cursor="heart",
        activebackground="hot pink",
        font=myFont).pack(
            padx=15, side=LEFT)

    vicdef.quitter = Button(
        vicdef,
        text="QUITTER",
        command=quit,
        width=15,
        height=1,
        bd=1,
        cursor="pirate",
        bg="red3",
        activebackground="red3",
        font=myFont).pack(
            padx=15, side=RIGHT)

    vicdef.mainloop()


#FONCTION DÉFAITE


def defaite():
    global vicdef

    videf = Tk()

    vicdef.geometry('300x150')

    vicdef.title("Quelle tristesse...")

    myFont = Font(family="comic Sans MS", size=12)

    vicdef.label = Label(
        vicdef,
        text="GAME OVER! Vous avez perdu! \n Que voulez-vous faire maintenant?",
        font=myFont).pack()

    vicdef.rejouer = Button(
        vicdef,
        text="REJOUER",
        command=recommencer,
        width=10,
        height=1,
        bd=1,
        cursor="heart",
        activebackground="hot pink",
        font=myFont).pack(
            padx=15, side=LEFT)

    vicdef.quitter = Button(
        vicdef,
        text="QUITTER",
        command=quit,
        width=10,
        height=1,
        bd=1,
        cursor="pirate",
        bg="red3",
        activebackground="red3",
        font=myFont).pack(
            padx=15, side=RIGHT)

    vicdef.mainloop()


#FONCTION RECOMMENCER


def recommencer():
    vicdef.destroy()  #détruit fenêtre
    intro()  #recommence le JEU


#PARTIE II - LES MINI-JEUX

#LE JEU DU PENDU


def choisirMOTpendu(
):  #cette fonction permet de prendre un mot hasard dans un fichier texte.

    global lmotadeviner  #rend la variable mot globale, c'est à dire qu'on peut l'utiliser dans n'importe quelle fonction.

    motsFR = open("fr.txt", "r", encoding="utf8")
    mots = motsFR.readlines()  #lis chaque ligne du fichier

    for i in mots:
        motadeviner = mots[randint(
            0, 323470)]  #choisis une ligne au hasard dans le fichier texte

    lmotadeviner = list(
        motadeviner)  #transforme le mot en une liste de lettres
    lmotadeviner.pop()  #supprime le dernier élément de la liste: le "ENTER"


def CreerJeuDepart():

    global lettresdevinees

    for i in range(len(lmotadeviner)):
        lettresdevinees.append(
            "_")  #crée le "_ _ _ _" pour afficher la longueur du mot etc.

    print(
        " ".join(lettresdevinees))  #affiche le pointillé sans les ' ou les []


def untourpendu():

    lettre = str(input('Choisissez une lettre: '))  #le joueur rentre une lettre

    for i in range(len(lettresdevinees)):
        if lmotadeviner[i] == lettre:
            lettresdevinees[
                i] = lettre  #remplace le _ par la lettre si elle est correctement devinée

    if lettre not in lmotadeviner:
        print(lettre, "n'est pas dans le mot! Essayez-en une autre"
              )  #si la lettre est faussement devinée, ceci est affiché
        dessindupendu()  #dessine le bonhomme

    print(" ".join(lettresdevinees))


def tourspendu(
):  #mise en place du debut du jeu et verification de victoire/defaite
    print("--------------------------------------------")
    print(
        "Ce jeu est un jeu de pendu classique. Saississez des lettres. Tous les mots français (dont les verbes conjugués MUAHAHAHA...) sont utilisés. ATTENTION! NE PAS UTILISER D'ACCENTS OU DE MAJUSCULES. Bonne chance à trouver le mot de passe!"
    )
    print()
    tour = 0  #nombre de tours au départ
    choisirMOTpendu()  #choisis un mot au hasard
    CreerJeuDepart()  #crée les pointillés

    while NbFautes < 11 and '_' in lettresdevinees:  #lorsque le bonhomme n'est pas pendu et que le mot n'est pas deviné
        untourpendu()  #fait jouer le joueur
        tour = tour + 1  #on rajoute un tour à chaque fois qu'on joue

    if '_' in lettresdevinees:
        defaite(
        )  #si à la fin de 11 fautes le mot n'est toujours pas complet, c'est perdu
    else:
        victoire()  #sinon, c'est gagné
    print("Le mot était", "".join(lmotadeviner))  #le mot est affiché
    print()
    print("--------------------------------------------")
    print()
    time.sleep(3)
    exit()


def jeudupendu():
    reset()
    tourspendu()  #initialise le programme


lmotadeviner = []
lettresdevinees = []
NbFautes = 0  #Nombre de fautes au départ


def dessindupendu():

    global NbFautes

    NbFautes = NbFautes + 1  #augmente le nombre de fautes par 1 à chaque faute

    if NbFautes == 1:  #dessine la barre en haut (1ère faute)
        up()
        goto(-200, 200)
        down()
        forward(200)

    if NbFautes == 2:  #dessine la barre qui descend (2ème faute)
        left(180)
        forward(180)
        left(90)
        forward(300)

    if NbFautes == 3:  #dessine le socle (3ème faute)
        left(90)
        forward(50)
        left(180)
        forward(100)
        left(180)
        forward(50)
        left(90)

    if NbFautes == 4:  #dessine la barre qui tient (4ème faute)
        forward(250)
        right(45)
        forward(71)
        right(45)
        forward(100)

    if NbFautes == 5:  #dessine la corde (5ème faute)
        right(90)
        forward(80)

    if NbFautes == 6:  #dessine la tête (6ème faute)
        left(90)
        circle(20)

    if NbFautes == 7:  #dessine le bras droit (7ème faute)
        right(90)
        forward(15)
        left(90)
        forward(25)
        right(90)
        forward(50)

    if NbFautes == 8:  #dessine le bras gauche (8ème faute)
        left(180)
        forward(50)
        left(90)
        forward(50)
        left(90)
        forward(50)

    if NbFautes == 9:  #dessine le tronc (9ème faute)
        left(180)
        forward(50)
        right(90)
        forward(25)
        right(90)
        forward(80)

    if NbFautes == 10:  #dessine la jambe droite (10ème faute)
        left(90)
        forward(12)
        right(90)
        forward(80)

    if NbFautes == 11:  #dessine la jambe gauche (11ème faute)
        left(180)
        forward(80)
        left(90)
        forward(25)
        left(90)
        forward(80)


#LE MASTERMIND


def MM_reessayer():
    print()
    print(
        "Vous n'avez pas réussi à trouver le code! C'est dommage. Je ne vous félicite pas. Réessayer?"
    )
    print()
    reessayer = input("oui ou non?   ")
    print()

    if reessayer == "oui":
        mastermind()
    elif reessayer == "non":
        defaite()
    else:
        print("Entrez ce que je vous ai dit d'entrer!")
        MM_reessayer


def mastermind():
    print("--------------------------------------------")
    print(
        "Vous devez trouver la combinaison secrète de 4 chiffres. Vous avez gagné si vous y parvenez en un maximum de 12 coups."
    )
    print()
    print("Six chiffres sont a votre disposition: 0 1 2 3 4 5")
    print()
    codesecret = []
    alignementoriginal(codesecret)
    x = 0
    while x < 13:
        if essai(codesecret, x) == True:
            print()
            print(
                "Vous avez trouvé le mot de passe pour rentrer dans le fichier. Hehe."
            )
            x = 50
            print("--------------------------------------------")
            suite_PENDU()
    if x < 30:
        MM_reessayer()

    print("Le code était: ", codesecret)


def alignementoriginal(codesecret):
    for x in range(0, 4):
        codesecret.append(randint(0, 5))
    return codesecret


def essai(codesecret, x):
    L = ['0', '1', '2', '3', '4', '5']
    strcodeessai = input("Votre combinaison:    ")
    codeessai = [(strcodeessai[0]), strcodeessai[1], strcodeessai[2],
                 strcodeessai[3]]

    #verification de l'input

    for i in range(0, 4):
        if codeessai[i] not in L:
            print("Veuillez entrer uniquement les chiffres à votre disposition")
            essai(codesecret, x)
    codeessai = [
        int(codeessai[0]),
        int(codeessai[1]),
        int(codeessai[2]),
        int(strcodeessai[3])
    ]
    if verification(codesecret, codeessai) == True:
        return True


def verification(codesecret, codeessai):
    if codeessai == codesecret:
        return True
    else:
        bon2 = bon = faux = 0
    for i in range(0, 4):
        if codeessai[i] == codesecret[i]:
            bon2 = bon2 + 1
            bon = bon + 1
        elif codeessai[i] in codesecret:
            bon = bon + 1
        else:
            faux = faux + 1
    print()
    print("Il y a", bon2, "bon(s) chiffre(s) bien placé(s) dans le code,", bon,
          " chiffre(s) contenu(s) au moins une fois dans le code, et", faux,
          "chiffre(s) non dans le code.")
    print()


#JEU DU PIERRE FEUILLE CISEAUX


def recommencer_PFC():
    global points
    print()
    print(
        "C'est triste. Vous avez perdu au pierre feuille ciseaux. Dégouté(e), vous arrêtez de vous battre contre le hackeur qui, très clairement, est bien supérieur à vous... Ou pas?"
    )
    time.sleep(2)
    print()
    reessayer = input("Recommencer? Entrez 'oui' ou 'non':   ")
    print()

    if reessayer == "oui":
        points = 0
        pierrefeuilleciseaux_debut()
    elif reessayer == "non":
        defaite()
    else:
        print("Entrez ce que je vous ai dit d'entrer!")
        print()
        time.sleep(2)
        recommencer_PFC()


points = 0


def pierrefeuilleciseaux():
    fenetre_PFC.destroy()
    pierrefeuilleciseaux_debut()


def input_joueur():
    global joueur
    joueur = str(input("Choisir 'pierre', 'feuille', ou 'ciseaux' : "))


def pierrefeuilleciseaux_debut():
    global ordi, liste
    print()
    print("------------------------------------")
    print(
        "Ce jeu est un jeu de pierre/feuille/ciseaux classique. Vous disposez de 5 tours afin d'obtenir un total d'au moins 3 points. Une égalité donne 0.5 point, une victoire donne 1 point et une défaite donne 0 point. Courage."
    )
    tours = 0
    liste = ['pierre', 'feuille', 'ciseaux']
    while tours < 5:
        print()
        input_joueur()
        print()
        ordi = choice(liste)
        pfcvainqueur()
        tours = tours + 1
    if points >= 3:
        print()
        print(
            'BRAVO! Vous avez vaincu le hackeur au pierre feuille ciseaux! Le hackeur vous donne un indice: "Oh! Cher Noobmaster, ce que tu cherches se trouve dans un fichier caché dans un dossier apparamment vide sur ton Desktop..." ...Maintenant de retour à vos fichiers privés...'
        )
        print()
        time.sleep(5)
        print("--------------------------------------------")
        scene5()
    else:
        print()
        print()
        recommencer_PFC()


def pfcvainqueur():
    global points
    if joueur not in liste:
        print()
        print("Veuillez rentrer soit 'pierre', soit 'feuille', soit 'ciseaux'")
        print()
        input_joueur()
        pfcvainqueur()
    elif ordi == joueur:
        points = points + 0.5
        print('Le hackeur a choisi', ordi)
        print()
        print('Égalité! Vos points sont', points)
        print()
    elif ordi == 'feuille' and joueur == 'pierre' or ordi == 'pierre' and joueur == 'ciseaux' or ordi == 'ciseaux' and joueur == 'feuille':
        print('Le hackeur a choisi', ordi)
        print()
        print('Vous avez perdu! Vos points sont', points)
        print()
    elif ordi == 'pierre' and joueur == 'feuille' or ordi == 'ciseaux' and joueur == 'pierre' or ordi == 'feuille' and joueur == 'ciseaux':
        print('Le hackeur a choisi', ordi)
        points = points + 1
        print()
        print('Vous avez gagné! Vos points sont', points)
        print()


#JEU DU MORPION


def morpion():
    print()
    print("--------------------------------------------")
    print(
        "Ce jeu est un jeu de morpion classique. Veuillez entrer un chiffre de 0 à 8 qui correspondra au numéro de la case où vous voulez placer votre symbole. Le joueur sera représenté par le symbole 'X' et le robot par le symbole 'O'."
    )
    print()
    tableau()  #Affiche le tableau de début (avec seulement les chiffres)
    tour()
    gagnant()


#Liste des valeurs_tableau possibles du robot:
liste_robot = []

#Liste des valeurs du tableau:
valeurs_tableau = []

#Les listes prennent les valeurs de 0 à 8 (qui représentent alors les cases du tableau et les valeurs_tableau possibles du robot et du joueur).
for x in range(0, 9):
    valeurs_tableau.append(x)
    liste_robot.append(x)


#Fonction permettant l'affichage du tableau qui sera mis à jour après chaque tour
def tableau():
    print()  #choix esthétique : plus espacé
    print(valeurs_tableau[0], valeurs_tableau[1],
          valeurs_tableau[2])  #ligne 1 du tableau
    print(valeurs_tableau[3], valeurs_tableau[4],
          valeurs_tableau[5])  #ligne 2 du tableau
    print(valeurs_tableau[6], valeurs_tableau[7],
          valeurs_tableau[8])  #ligne 3 du tableau
    print()  #choix esthétique


#Fonction mise en place lorsque c'est le tour du joueur
def tour_joueur():
    user_input = input(
        "Quelle case choisissez-vous?  "
    )  #Le joueur choisit la case où il veut placer son symbole. ATTENTION : un caractère autre qu'un chiffre va arrêter le programme.

    try:
        J1 = int(user_input)
        if J1 in valeurs_tableau:  #Vérification du saisi du joueur 1:

            for x in range(
                    0, 9
            ):  #Le numéro de case choisi par le joueur 1 sera remplacé par "X" si c'est un chiffre compris entre 0 et 8 (9-1).

                if valeurs_tableau[J1] == x:
                    valeurs_tableau[J1] = "X"
                    liste_robot.remove(
                        x
                    )  #Enlève la case choisie par le joueur des choix possibles pour le robot.
        else:
            print()
            print(
                "Pas possible. Saisissez un chiffre entre 0 et 8 qui n'est pas déjà pris."
            )
            print()
            tour_joueur()

    except ValueError:  #Lorsque le chiffre saisi n'est pas un chiffre/nombre compris entre 0 et 8 où qu'il est déjà pris, le joueur 1 devra rejouer.
        print()
        print(
            "Pas possible. Saisissez un chiffre entre 0 et 8 qui n'est pas déjà pris."
        )
        print()
        tour_joueur()


#Fonction mise en place lorsque c'est le tour du robot
def tour_robot():
    J2 = choice(
        liste_robot
    )  #le robot choisit une valeur au hasard dans la liste des choix
    print()
    print("Le robot a choisi la case ", J2, "!")
    print()

    for x in range(0, 9):
        if valeurs_tableau[J2] == x:
            valeurs_tableau[J2] = "O"
            liste_robot.remove(
                x
            )  #Enlève la case choisie par le robot des choix possibles pour le robot.


#Fonction régulant les tours
def tour():
    tours = 1  #Nombre de tours
    while tours <= 9:  #Tant qu'il n'y a pas d'égalité
        if tours % 2 == 0:  #Le nombre de tours sera pair lorsque c'est le tour du robot et impair lorsque c'est le tour du joueur
            tour_robot()
            tableau()
        else:
            tour_joueur()

        tours = tours + 1

        if gagnant() == True:  #Si le joueur a gagné
            tableau()
            print("Vous avez gagné! :)")
            time.sleep(2)
            print()
            print("--------------------------------------------")
            scene3()

        if gagnant() == False:  #Si le joueur a perdu
            tableau()
            print("Vous avez perdu! :(")
            time.sleep(2)
            print()
            print("--------------------------------------------")
            scene3()

    print()
    print("Egalité! Recommencez le programme pour un nouveau jeu.")
    morpion()


def gagnant(
):  #On teste toutes les combinaisons possibles permettant la victoire.
    if valeurs_tableau[0] == valeurs_tableau[1] == valeurs_tableau[
            2] == "X" or valeurs_tableau[3] == valeurs_tableau[4] == valeurs_tableau[
                5] == "X" or valeurs_tableau[6] == valeurs_tableau[
                    7] == valeurs_tableau[8] == "X" or valeurs_tableau[
                        0] == valeurs_tableau[3] == valeurs_tableau[
                            6] == "X" or valeurs_tableau[1] == valeurs_tableau[
                                4] == valeurs_tableau[7] == "X" or valeurs_tableau[
                                    2] == valeurs_tableau[5] == valeurs_tableau[
                                        8] == "X" or valeurs_tableau[
                                            0] == valeurs_tableau[
                                                4] == valeurs_tableau[
                                                    8] == "X" or valeurs_tableau[
                                                        2] == valeurs_tableau[
                                                            4] == valeurs_tableau[
                                                                6] == "X":  #Pour tester si le joueur 1 a gagné
        return True
    elif valeurs_tableau[0] == valeurs_tableau[1] == valeurs_tableau[
            2] == "O" or valeurs_tableau[3] == valeurs_tableau[4] == valeurs_tableau[
                5] == "O" or valeurs_tableau[6] == valeurs_tableau[
                    7] == valeurs_tableau[8] == "O" or valeurs_tableau[
                        0] == valeurs_tableau[3] == valeurs_tableau[
                            6] == "O" or valeurs_tableau[1] == valeurs_tableau[
                                4] == valeurs_tableau[7] == "O" or valeurs_tableau[
                                    2] == valeurs_tableau[5] == valeurs_tableau[
                                        8] == "O" or valeurs_tableau[
                                            0] == valeurs_tableau[
                                                4] == valeurs_tableau[
                                                    8] == "O" or valeurs_tableau[
                                                        2] == valeurs_tableau[
                                                            4] == valeurs_tableau[
                                                                6] == "O":  #Pour tester si le joueur 2 a gagné
        return False


#PARTIE III - JEU.EXE + dialogue

#SCÈNE 1


def scene1():
    print()
    print()
    print()
    print("Pour jouer suivez les instructions données:")
    print("Pour faire un choix, entrez le numéro de la proposition.")
    print()
    print()
    print()
    print()
    time.sleep(2)  #attend 2 secondes puis continue
    print(
        "On dirait que votre ordinateur a été pris en otage par un hackeur ringard. Que voulez-vous faire maintenant?"
    )
    print()
    print("1. Pleurer.")
    print()
    print("2. Aller aux toilettes. C'est stressant comme situation.")
    print()
    print("3. Appeler la police.")
    print()
    print()
    scene = input("Tapez '1', '2' ou '3': ")
    print()
    print()

    if scene == '1':
        print("Vous pleurez.")
        print()
        time.sleep(1)
        print("Attendez 15s pour vous en remettre.")
        playsound("pleurs.mp3")

    elif scene == '2':
        print("Vous allez aux toilettes.")
        print()
        time.sleep(5)
        print("Ça prend du temps...")
        print()
        time.sleep(5)
        print()
        print()
        print("Bravo! Vous avez évacué votre vessie. Continuez...")

    elif scene == '3':
        print("Vous appelez la police.")
        print()
        time.sleep(1)
        playsound("phone.mp3")
        print("...")
        time.sleep(2)
        print()
        playsound("phone.mp3")
        print("...")
        time.sleep(1)
        print()
        print(
            "La police ne semble pas répondre. Vous commencez à chercher et vérifier vos fichiers."
        )
    else:
        print(
            "Le hackeur ne supporte pas l'insolence. Faites un choix raisonnable cette fois-ci"
        )
        scene1()

    print()
    print(
        "Il ne vous reste plus qu'à suivre les instructions. Vous ne vous laissez pas intimider par le hackeur. Franchement parlant, vous vous y connaissez un minimum en informatique, et vous savez que le premier endroit à vérifier dans le cadre de téléchargement automatique non desiré est le fichier C:/Users/Noobmaster121/ThisPC/Downloads."
    )
    scene2()


#SCÈNE 2


def scene2():
    time.sleep(2)
    print()
    print(
        "Malheureusement pour vous, votre fichier Download contient plus de 8000 documents et fichiers."
    )
    time.sleep(3)
    print("Vous cherchez... Il y a beaucoup de fichiers.")
    print()
    time.sleep(2)
    print("Matrix.mp4... asdksjhfsb.pdf... Non ce n'est pas ça...")
    time.sleep(4)
    print()
    print("Vous n'en revenez pas! 'JEU.exe'")
    print()
    time.sleep(1)
    print("C'est tellement simple, vous êtes génial(e).")
    print()
    time.sleep(1)
    print("Vous aviez raison de ne pas avoir peur de ce hackeur de pacotille.")
    time.sleep(3)
    print()
    print("Cependant!")
    print()
    time.sleep(1)
    print(
        "Au lieu de cliquer gauche puis 'delete', vous cliquez droit et ouvrez le fichier."
    )
    print()
    time.sleep(2)
    print("Qu'avez vous fait! ...Une fenêtre s'ouvre.")
    print()
    time.sleep(2)
    print("Un jeu de Morpion sauvage apparait.")
    print()
    time.sleep(1)
    print("...")
    time.sleep(2)
    print(
        "C'est le jeu codé par votre neveu que vous avez téléchargé l'année dernière. Vous saviez que ça ne serait pas aussi facile."
    )
    time.sleep(5)
    print()
    print(
        "Pour vous consolez, vous décidez de jouer à une partie. C'est un bon jeu."
    )
    time.sleep(1)
    morpion()


#SCÈNE 3


def scene3():
    print()
    print(
        "Même si le jeu est facile à battre, votre neveu a fait des efforts. Vous êtes fier(e)."
    )
    print()
    print()
    time.sleep(2)
    menurecherche(Lendroitachercher)


#SCÈNE 4


def scene4():
    print(
        "Bon. Ce n'est pas dans vos documents d'utilisateur. Il faudra donc chercher les documents du harddrive."
    )
    print()
    time.sleep(1)
    print("Tiens?")
    print()
    time.sleep(1)
    playsound("message.mp3")
    print("Vous avez recu un message du hackeur sous la forme d'une fenêtre.")
    print()
    time.sleep(3)
    suite_PFC()


#SCÈNE 5


def scene5():
    print()
    print()
    print(
        "Vous n'en revenez pas. Comment n'avez vous pas pensé aux fichiers cachés?"
    )
    print()
    time.sleep(1)
    print("Vous changez vos paramètres immédiatement!!!")
    print()
    time.sleep(3)
    print(
        "Effectivement, il y a bien un dossier caché appelé 'haha' dans le dossier vide de votre Desktop."
    )
    print()
    time.sleep(2)
    print(
        "Vous prenez votre courage à deux mains et vous ouvrez le dossier. Vous êtes bientôt libre!"
    )
    playsound("libere.mp3")
    print()
    print("Ou pas.")
    print()
    choix4052()


def choix4052():
    print("Vous faites face à deux dossiers differents:")
    print()
    time.sleep(1)
    print("1. '40'")
    print()
    time.sleep(1)
    print("2. '52'")
    print()
    choix4052var = input(
        "Quel fichier voulez-vous ouvrir? Entrez '1' ou '2':    ")
    if choix4052var == '1' or choix4052var == '40':
        choix1347()
    elif choix4052var == '2' or choix4052var == '52':
        choix5252()
    else:
        print("Veuillez entrez un numéro valable.")
        choix4052()


def choix5252():
    print()
    print("Vous faites face à deux dossiers differents:")
    print()
    time.sleep(1)
    print("1. '52'")
    print()
    time.sleep(1)
    print("2. '52'")
    print()
    print("3. Retour aux fichiers '52' et '40'")
    print()
    time.sleep(1)
    choix5252var = input(
        "Quel fichier voulez-vous ouvrir? Entrez '1' ou '2', sinon entrez '3':    "
    )
    if choix5252var == '1' or choix5252var == '2' or choix5252var == '52':
        choix5252()
    elif choix5252var == '3':
        print()
        time.sleep(1)
        print("Vous retournez en arrière jusqu'au choix '40' ou '52'")
        choix4052()
    else:
        print("Veuillez entrez un numéro valable.")
        choix5252()


def choix1347():
    print("Vous faites face à deux dossiers differents:")
    print()
    time.sleep(1)
    print("1. '47'")
    print()
    time.sleep(1)
    print("2. '13'")
    print()
    print("3. Retour au choix '40' ou '52'")
    print()
    time.sleep(1)
    choix1347var = input(
        "Quel fichier voulez-vous ouvrir? Entrez '1' ou '2', sinon '3':    ")
    if choix1347var == '2' or choix1347var == '13':
        choix7888()
    elif choix1347var == '1' or choix1347var == '47':
        choix6704()
    elif choix1347var == '3':
        choix4052()
    else:
        print("Veuillez entrez un numéro valable.")
        choix1347()


def choix6704():
    print()
    print("Vous faites face à deux dossiers differents:")
    print()
    time.sleep(1)
    print("1. '67'")
    print()
    time.sleep(1)
    print("2. '04'")
    print()
    print("3. Retour aux fichiers '13' et '47'")
    print()
    time.sleep(1)
    choix6704var = input(
        "Quel fichier voulez-vous ouvrir? Entrez '1' ou '2', sinon entrez '3':    "
    )
    if choix6704var == '1' or choix6704var == '2' or choix6704var == '67' or choix6704 == '04':
        choix6704()
    elif choix6704var == '3':
        print()
        time.sleep(1)
        print("Vous retournez en arrière jusqu'au choix '13' ou '47'")
        choix1347()
    else:
        print("Veuillez entrez un numéro valable.")
        choix6704()


def choix7888():
    print("Vous faites face à deux dossiers differents:")
    print()
    time.sleep(1)
    print("1. '78'")
    print()
    time.sleep(1)
    print("2. '88'")
    print()
    print("3. Retour aux choix '13' ou '47'")
    print()
    time.sleep(1)
    choix1347var = input(
        "Quel fichier voulez-vous ouvrir? Entrez '1' ou '2', sinon '3':    ")
    if choix1347var == '1' or choix1347var == '78':
        dossierfrozen()
    elif choix1347var == '2' or choix1347var == '88':
        choixcarotteaspirateur()
    elif choix1347var == '3':
        choix1347()
    else:
        print("Veuillez entrez un numéro valable.")
        choix7888()


def choixcarotteaspirateur():
    print()
    print("Vous faites face à deux dossiers differents:")
    print()
    time.sleep(1)
    print("1. 'carotte'")
    print()
    time.sleep(1)
    print("2. 'aspirateur'")
    print()
    print("3. Retour aux fichiers '78' et '88'")
    print()
    time.sleep(1)
    choixcarotteaspirateurvar = input(
        "Quel fichier voulez-vous ouvrir? Entrez '1' ou '2', sinon entrez '3':    "
    )
    if choixcarotteaspirateurvar == '1' or choixcarotteaspirateurvar == '2' or choixcarotteaspirateurvar == 'carotte' or choixcarotteaspirateurvar == 'aspirateur':
        choixcarotteaspirateur()
    elif choixcarotteaspirateurvar == '3':
        print()
        time.sleep(1)
        print("Vous retournez en arrière jusqu'au choix '78' ou '88'")
        choix7888()
    else:
        print("Veuillez entrez un numéro valable.")
        choixcarotteaspirateur()


def dossierfrozen():
    print()
    print()
    time.sleep(1)
    print("Vous faites face à un seul et unique dossier appelé: 'frozen'.")
    print()
    time.sleep(2)
    print(
        "Bon. Et vous qui chantiez Libérée, delivrée de Frozen, il n'y a que quelques minutes. Vous n'osez espérer. Ce dossier serait-il une autre blague du hackeur?"
    )
    print()
    time.sleep(5)
    print(
        "Vous cliquez sur le dossier pour l'ouvrir, seulement pour vous rendre compte que le dossier est protégé par un mot de passe!"
    )
    print()
    time.sleep(5)
    suite_MM()


#MENU DE RECHERCHES

Lendroitachercher = [
    "C:/Users/Noobmaster121/ThisPC/Pictures",
    "C:/Users/Noobmaster121/ThisPC/Documents",
    "C:/Users/Noobmaster121/ThisPC/Music",
    "C:/Users/Noobmaster121/ThisPC/Desktop",
    "C:/Users/Noobmaster121/ThisPC/Videos"
]


def scene_Pictures():
    print("Vous faites face à 2 dossiers et un fichier zip:")
    print()
    time.sleep(1)
    print("1.   'Photos_de_vacances_La Baulle_2018'")
    print()
    time.sleep(1)
    print("2.   'VIEILLEPHOTO.zip'")
    print()
    time.sleep(1)
    print("3.   'Screenshots'")
    print()
    time.sleep(1)
    print(
        "4.    Retournez aux dossiers principaux (Attention, vous ne pourrez plus reverifier ce dossier-ci)."
    )
    print()
    print()
    time.sleep(1)
    n = input("Entrez le nombre de votre choix: ")
    print()
    print()

    if n == '1':
        print()
        print(
            "Votre mère vous a envoyer TOUTES les photos des vacances prises à la Baulle avec votre famille étendue. Voulez-vous les regarder avec plus d'attention?"
        )
        print()
        print()
        time.sleep(2)
        reponse = input("Entrez oui ou non: ")
        if reponse == 'oui':
            print()
            print(
                "Vous prenez un moment pour observer les photos avec plus de détails..."
            )
            print()
            time.sleep(3)
            print("Les moules étaient bonnes ce jour la.")
            print()
            time.sleep(3)
            print(
                "Les diners de familles dans le jardin, si seulement la conversation à la 'table des grands' pouvait être un peu moins arrièrée."
            )
            print()
            time.sleep(5)
            print(
                "Il ne semble ne rien y avoir de particulier dans ces photos.")
            print()
            print()
            print()
            time.sleep(2)
        elif reponse == 'non':
            print()
            print(
                "Vous n'avez pas de temps pour les bons souvenirs. Vous continuez à chercher."
            )
            print()
            print()
            time.sleep(2)
        else:
            print(
                "Vous n'avez pas l'air motivé de répondre correctement. Tant pis pour les photos, vous continuez votre recherche."
            )
            print()
            print()
            time.sleep(2)
    elif n == '2':
        print(
            "Ce sont vos photos de jeunesse. Recupérer de chez le scanneur. Un trésor de souvenirs, bons comme malaisants."
        )
        print()
        time.sleep(4)
        print("...")
        print()
        time.sleep(3)
        print("Il n'y a rien d'intéréssant ici.")
        print()
        print()
        time.sleep(1)
    elif n == '3':
        print(
            "Les images de ce dossier correspondent a vos dernières captures d'écran. Vous les cherchez pour trouver un indice."
        )
        print()
        print()
        time.sleep(1)
        indice = input(
            "Combien faut-il de bits pour coder une image en noir et blanc de 3 pixels par 4 pixels? Votre réponse: "
        )
        print()
        print()
        if indice == '12':
            print(
                "Il y a un nombre qui semble revenir sur le site de download de JEU.exe: '40'"
            )
            print()
            time.sleep(3)
        else:
            print(
                "Malheureusement, vous ne remarquez rien de particuler dans les captures d'écrans."
            )
            print()
            time.sleep(2)
    else:
        "Vous avez choisi de choisir un autre fichier à vérifier."
        menurecherche(Lendroitachercher)
    scene_Pictures()


def scene_Documents():
    print("Vous faites face à 15 dossiers et 3 fichiers pdf:")
    print()
    time.sleep(2)
    print("Vous déséspérer devant le nombre de dossiers à verifier.")
    print()
    print()
    time.sleep(2)
    print(
        "Il n'y a rien d'inhabituel dans vos dossiers, si ce n'est qu'ils sont surprenamment bien rangés..."
    )
    print()
    print()
    time.sleep(3)
    menurecherche(Lendroitachercher)


def scene_Music():
    print()
    print(
        "Vous faites face à 800 fichiers mp3, 2 fichiers wav et ... un pdf de nom 'blaguesnulles.pdf' ?"
    )
    print()
    print()
    time.sleep(2)
    reponse = input(
        "Voulez vous ouvrir le fichier pdf? Si oui, entrez oui, sinon entrez non: "
    )
    if reponse == 'oui' or reponse == 'Oui':
        print()
        print("Vous decidez d'ouvrir le pdf.")
        print()
        time.sleep(1)
        print(
            "C'est un pdf de blagues nulles... Quelle est l'utilité d'un tel fichier?"
        )
        print()
        time.sleep(3)
        print("Que fait une fraise sur un cheval?")
        print()
        time.sleep(2)
        print("...Tagada tagada...")
        print()
        time.sleep(3)
        print("Vous décidez de fermer le fichier.")
    elif reponse == 'non':
        print()
        print(
            "Vous savez parfaitement à quoi sert ce document. Pas besoin de l'ouvrir."
        )
        print()
        time.sleep(3)
    else:
        print()
        print(
            "Sans savoir écrire oui ou non, vous décidez de ne pas ouvrir le fichier."
        )
        print()
        time.sleep(2)
    print()
    time.sleep(2)
    print(
        "Tous les fichiers mp3 semblent être normaux. Pas de fichier JEU.exe en vue. C'est simplement votre playlist habituelle."
    )
    print()
    time.sleep(4)
    print("Vous décidez de retourner vérifier les autres fichiers principaux.")
    print()
    time.sleep(4)
    menurecherche(Lendroitachercher)


def scene_Desktop():
    print()
    print(
        "Vous faites face à 5 fichiers executables, 2 dossiers et 7 autres fichiers:"
    )
    print()
    time.sleep(2)
    print(
        "Le hackeur semble avoir changer votre magnifique rébus image fond d'ecran 'pi-thon' a une photo d'un cheval dans un champs de fraises. Un indice peut-être?"
    )
    print()
    time.sleep(4)
    print(
        "Probablement pas. Par contre, vous remarquez un petit 78 en bougeant l'icone de la poubelle en haut à gauche de l'ecran... Une signature?"
    )
    print()
    print()
    time.sleep(6)
    print(
        "Après, avoir vérifier les dossiers, dont un est vide et un contient des documents notés (liste de courses etc...), Vous déecidez de retournez étudier les autres fichiers principaux"
    )
    print()
    time.sleep(4)
    menurecherche(Lendroitachercher)


def scene_Videos():
    print()
    print(
        "Vous avez sauvé beaucoup de films, vous faites donc face à beaucoup de fichiers mp4."
    )
    print()
    time.sleep(1)
    print(
        "En organisant les fichiers par extension, vous êtes certains qu'il n'y a effectivement que des fichiers mp4."
    )
    print()
    print()
    time.sleep(1)
    reponse = input(
        "Voulez-vous regarder les vidéos avec plus de détails dans le but de trouver un indice ou de chercher? Si entrez oui: "
    )
    if reponse == 'Oui' or reponse == 'oui':
        print()
        print(
            "Vous n'allez pas vérifier le contenu de toutes les vidéos? Vous décidez de vérifier d'abord 1 vidéo sur 3:"
        )
        indice = choice([1, 2, 3])
        if indice == 1 or indice == 2:
            print()
            print("...")
            print()
            time.sleep(2)
            print()
            print(
                "Que_font_deux_brosses_a_dents_le_14_juillet?_Des_feux_dentrifices!.mp4?? Suppression immédiate."
            )
            print()
            time.sleep(2)
            print("Vous ne trouvez rien.")
            r = input(
                "Voulez-vous continuer à regarder les vidéos avec plus de détails dans le but de trouver un indice? Si oui, entrez oui, sinon entrez non: "
            )
            if reponse == 'oui' or reponse == 'Oui':
                if indice == 1:
                    print()
                    print()
                    time.sleep(2)
                    print(
                        "Pourquoi_les_canards_sont_ils_toujours_a_l_l'heure?_Parcequ'ils_sont_dans_l'etang.mp4... Mais pourquoi appelez-vous vos vidéos de la sorte?"
                    )
                    print()
                    time.sleep(2)
                    print()
                    print("Vous ne trouvez toujours rien.")
                    print()
                    time.sleep(1)
                    r = input(
                        "Voulez vous finir de vérifier l'entièreté des vidéos dans le but de trouver un indice? Si oui, entrez oui, sinon entrez non : "
                    )
        print()
        print(
            "Vous remarquez qu'une de vos vidéos a pour nom: 00001101.mp4... Vous n'arrivez même pas a l'ouvrir et ne vous rappelez pas l'avoir télécharger. 00001101 est l'octet correspondant à 13, non?"
        )
        print()
        time.sleep(1)
        r = input(
            "Voulez-vous continuer à chercher? Si oui, entrez oui, sinon entrez non: "
        )
        if r == 'oui' or r == 'Oui':
            print()
            time.sleep(4)
            print("Vous ne trouvez rien.")
            time.sleep(1)
            print()
            print("Vous ne vous embêtez pas à chercher plus loin.")
            print()
            time.sleep(1)
            menurecherche(Lendroitachercher)
    elif reponse == 'Non' or reponse == 'non':
        print()
        print(
            "Vous n'avez pas le temps de vérifier chaque vidéo. C'est beaucoup trop long. Vous continuez à chercher les dossiers principaux."
        )
        print()
        time.sleep(3)
    else:
        print()
        print(
            "Vous n'avez pas l'air motivé de répondre correctement. Tant pis pour les vidéos, vous continuez votre recherche ailleurs."
        )
        print()
        time.sleep(3)

    menurecherche(Lendroitachercher)


def menurecherche(Lendroitachercher):
    if Lendroitachercher != []:
        print("Où chercher maintenant?")
        time.sleep(1)
        for n in range(1, len(Lendroitachercher) + 1):
            print()
            print()
            print(n, ". ", Lendroitachercher[n - 1])
            print()
            time.sleep(1)

        scene_n = input("Entrez le nombre de votre choix: ")
        scene_n = int(scene_n) - 1
        print()
        print()
        if scene_n in range(0, len(Lendroitachercher)):
            if Lendroitachercher[
                    scene_n] == "C:/Users/Noobmaster121/ThisPC/Pictures":
                del Lendroitachercher[scene_n]
                scene_Pictures()
            elif Lendroitachercher[
                    scene_n] == "C:/Users/Noobmaster121/ThisPC/Documents":
                Lendroitachercher.remove(
                    "C:/Users/Noobmaster121/ThisPC/Documents")
                scene_Documents()
            elif Lendroitachercher[
                    scene_n] == "C:/Users/Noobmaster121/ThisPC/Music":
                Lendroitachercher.remove("C:/Users/Noobmaster121/ThisPC/Music")
                scene_Music()
            elif Lendroitachercher[
                    scene_n] == "C:/Users/Noobmaster121/ThisPC/Desktop":
                Lendroitachercher.remove(
                    "C:/Users/Noobmaster121/ThisPC/Desktop")
                scene_Desktop()
            else:
                Lendroitachercher.remove(
                    "C:/Users/Noobmaster121/ThisPC/Videos")
                scene_Videos()
        else:
            print("Je ne pense pas que cela soit une bonne idée.")
            menurecherche(Lendroitachercher)
    else:
        scene4()


#DÉBUTE LE JEU


def debut_jeu():
    print()
    debut = input(
        "Voulez-vous jouer avec moi?...Si oui, saississez 'oui'; sinon 'non', et dites bye bye à votre ordinateur! MUAHAHA     "
    )
    print()

    if debut == "oui":
        time.sleep(1)
        print("...Excellent choix ;) Bonne chance mon amour.")
        #morpion()
        scene1()
    elif debut == "non":
        time.sleep(1)
        print("...AH! Quel dommage... enfin... pour vous... hehhehehehehehe")
        time.sleep(5)  #attends 3 secs pour faire la suite
        exit()  #quitte le programme
    else:
        time.sleep(1)
        print(
            "...Mais! Faites pas votre malin et saissisez ce que je vous ai dit!"
        )
        debut_jeu()


#FENÊTRES DÉBUT


def debut():
    debut = Tk()
    img = ImageTk.PhotoImage(Image.open("faitgaffe.png"))
    panel = Label(
        debut, image=img).pack(
            side="bottom", fill="both", expand="yes")
    playsound("alarme.mp3")
    debut.after(500, debut.destroy)
    debut.mainloop()


#INTRODUCTION


def intro():

    for i in range(3):
        debut()

    time.sleep(1)

    print(
        "«ÂtÜ¾÷œóûã½äÜf†fäýüƒÎÜ8ç{bÎóÆó€‡¢(Š¢(Š¢(Š¢(ËCº¢(Š¢(Š¢(Š¢¨@WEQEQEQEº¢(Š¢(Š¢(Š¢¨@WEQEQEQEº¢(Š¢(Š¢(Š¢¨@WEQEQEQEº¢(Š¢(Š¢(Š¢¨@WEQEQEQEº¢(Š¢(Š¢(Š¢¨@WEQEQEQEº¢(Š¢(Š¢(Š¢¨@WEQEQEQEº¢(Š¢(Š¢(Š¢¨@WEQEQEQEº¢(Š¢(Š¢(Š¢¨@WEQEQEQEº¢(Š¢(Š¢(Š¢¨@WEQEQEQEº¢(Š¢(Š¢(Š¢¨@Wzú`¢Á­p½$ñÔ?tAEQEQEQT +Ë¿½"
    )

    time.sleep(1)

    print(
        'EÁadÝ:ZÏë‚ôaLb±&ËË€«‹¢(Š¢(Š¢(*ÐU ÷šƒaØx^®ÝßûŒ]‰˜7’óþCÌ=L¬ÏŠóµ	q36;àÑL†ÇHq….Œ¢(Š¢(Š¢¨@_1ºA›]qø—ß{ÝöÙæ*„íHf_!ë½[ð5~Fâ¾ Æ={û(!nÆÏ‰ —Hp49Þ×ÅQEQEQèÝÃ4‚D‚[áf7%•›‰Ã½vGýM˜ûÈð	F÷ºíp2ã<ÒÞ¤ÛÎ>Iˆ[qø71vÔ³·O^pýˆòw,¶Àå÷¼H÷‘f).ÒREQEQèÝøØ‡÷âñ?ZÙÈè'
    )

    time.sleep(1)

    print(
        '{TMßºûÌRð2Ðx:$žÖõQEQEQèÝ#Äœ@šûHrrØÙò¼^…—’æÎ^µ}QÞÀbcÒÜJŠ«ÚüÞdU¢ÌÄ )®$Íx=ƒ{lñ‡Ô,È}»´:T¿ÁÀƒáçg¨Ý²ÿÑã (Š¢(Š¢(*Ð»Gë	r.þF‚Ãû†ãul¶%Íƒ½.¨a*6CÉò	Ž+p°J‰2“Ad¸³×T-Øl‹ÍÎ¤¹§o:ËGFAéXˆÝÍ—/ýï«xÂ‡‚áÏƒô»P³+:×^QEQEQT w[ 8 cÈñ*qöé;,eù½@ ?‡É:´²	^º_VzDHÍ ßÆ`–ÁœmÁù­ëŸW~?DF€ÛõG@êÅ¿Çn+¸Ýß³ÅÉZn€¦Kõn¤(Š¢(ŠÒÛ±W‡Üm^vD…äóP7J×IY>Ýf'
    )

    time.sleep(1)

    print(
        "LÅ¥žÛâÑÜëwØd-¢¼‚A).ïUóÛ}ìIˆûHr<Y^jóš —à<<I0Šïõþ›ÑÊ–xÔ-½/*>Š/ ·ZÆBlTN†À–0{+p~ÏŸÕQ/!ÆoížýQ¨~ü›Cî¨Ùœ_Û}`;(:|›J 5š./ÛµýlUÏƒY™4¼µ{‹›{W	îŠéÛ3='sïÒ]EQEQ”™ðþPr¥T]¦^[øwBø`H¿5»éZ)ËG ›¬M”× ‡ƒqù¥ìpˆ(ob²&’ä´^³ma*¥¤¸¢ Ë¼ƒ	s`’ä<2<¼üïU<€ÍpHŽ÷®¹Í^˜Àå7rLÃ½«)Š¢(Š¢,Jo”çÌØ$h:·°@Ïüæì k¥,nPIï ÅÄÙ‡ÿë;á|ìJ–×‰3¼ŒÒ|ð`"
    )

    time.sleep(1)

    print(
        '2<@’³EeýÈp7I.XîÛ-½ó§’äì6“•	r6ƒ1(’8|[È1³ó_Rù„ö–ôÚ½ågÅç@äX0‹á×U¸yÞÑÁk–£ô;…?³ä(:[n´§~=*ÿÆûE2÷Ùo¡ìffo^'
    )

    time.sleep(1)

    print(
        'Kû­j¨zILîœ_%‹oeëÒù®ôê×À¿	``&?Ã«ßÏýIïlŠ¢(Š¢(=MÑPr™ˆðš=þ]ùDˆÙ/E {q]/eÙtðSÄ˜¬Fœ‘ä˜Ñv:Äø9—±µ½fÛdúäx‘8‡8`¢¼†ÉFy÷ü}—û6û9’·“æ.R\²ÐoÂÜ‹ ‚€MÎúIãBÜÜë‹ÿ‚À`¨xN„ätùùÊß½&85ðk¿ù¯eãÅø-6¡ýwÕTî.™÷¦ þHá×•ÝÑãÀm€æ«ægº‹Ï‡âó îH½Ü¹Å*¹T‚˜bHØNäÝ&ÙÖæ«º¶ø“ò=ù¦|FÝázIïlŠ¢(Š¢(=Mpˆ<{¹1¨¹Ÿx^¼¢£ågµ{AîÛ¾½¯f`Í¯PUúŠ@‡(oa±	IÎ"Ã}b§œF«ðˆ‘àhr¼Þýs—5°Øƒ"rü—¯—hÛ"<Íž8ü#ïŒïxÍ³Øì‘w{ºÜg[lI”É2“£XçSp)Q>"ÃýØÆ^x¡ÝÈ…"äx¯é)ñîˆÊ'
    )

    time.sleep(1)

    print(
        'EH§fI–yî©»Jôq;¿ÂìME¨ƒ˜ÆU½(né™Ï vpñG°×ª)`‚ì¿ vOpf¾—ß+eð‰§¡þØù¿ó­ì¦ïômÙBÝÁ9ŠN³²_AãYb~×YÂ¡b")!é…o:KCEQEQ–Šh­g?{ehºDFåÎ¥dŒ$aÜF¨?\¦õUBûBÑÉà¥ ùZÈ|¤Ç¾/	t)ß×‘âª>±Ó6;æ	Â¤¸Œ4ºõ9A.ÃÏô\<êqø'
    )

    time.sleep(1)

    print(
        '¿¶ôfÜV	d>†–ÚÎÙœ÷ýeâ.,—²[/?scÐ:^Þ«(Š¢(ŠÒ[(>GÆÖÆ„†“{×¶ù7ñ/êP=E¡ßkà[âOBÃñòs«?T¿*Â6ùRïªPzàÜ½¢ÇËô¨ä4icXÔãª·t?#q.ßÒÊÖ@n©l¨Œò:—ßHs7î[@è>ŠÍrL#Éyx4uâó®$ÀYùRò£È1«SÛa²^Á Šç‘á‰ü2:]Þ§0“ð±qö Ç{ùÏ_“/a2,O“à˜v¶ÿRœ8¤¸4·Ö‡ìEˆû1(Êÿ$™ÏrOêÑããc?ÂÜ'
    )

    time.sleep(1)

    print(
        'Ö“E·áü8‰ë µð¶a­"rÿ¦ýFz§sß-pv¡ß[`¯MçÏwO¯˜¡ý!÷•˜»•O37§FfR&ž]àbºŠÏÌ2ûPDvhO°*åÿë^0€p§Dzs?ÂœmÅ~n¦:óÙâ/ànâÚîß<WÜÕëGƒ—hç'
    )

    time.sleep(1)

    print(
        '‡ù-ˆ0ƒ|96!2<D’ž.+²ð½‹Z—ï °¹Ã9Cæ»µGé2g<÷=ÌÞráßUL‚ðAr£s~±n„$«\wÈü×Ÿ+¢ØˆHi÷Ürx’¥Òk$SO Ü9"¬7s|^¯ú€üebˆ87lÉ¦²]Ùçç`à[WÊÚ­•%ˆàÖ‹o:·ks$£ r¼”ç¥2ÞËå£u¦ln¾Oj:4^0?Pà[ÊÆÊ~g¿’(ß‚•	Š¢(Š¢(ËßºP5]žaj†ˆ¨ë“ûñg¨œ"ÆÇ±‰ó'
    )
    time.sleep(1)

    print()
    print()
    print()
    print()
    print()
    print()

    playsound('rire.mp3')

    time.sleep(1)

    print(
        "...MUAHAHAHAHHA!!! Ton ordinateur a été hacké par MOI! ;) Et oui! Le fichier était en effet un CHEVAL DE TROIE! Et vous êtes TOMBE DANS LE PIEGE!"
    )

    time.sleep(4)

    print()
    print("...")
    print()

    time.sleep(2)

    print(
        "...Mais comme je suis sympatique, et que vous me faites pitié, je veux bien vous laisser recupérer le contrôle de celui-ci..."
    )
    time.sleep(2)
    print()
    print(
        "...SI, et seulement si, vous arrivez à retrouver le fichier jeu.exe depuis cette commande,"
    )
    print()
    time.sleep(3)
    print("...Et arrivez à le supprimer~~")
    print()
    print()
    time.sleep(3)
    debut_jeu()


#POUR COMMENCER LE JEU

intro()
