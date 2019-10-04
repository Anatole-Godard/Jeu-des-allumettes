from tkinter import *
  
class Part():
    def __init__ (self):
        self.fen = Tk () #fenêtre
        self.fen.title("Jeu des allumettes") #titre de la fenêtre
        self.can = Canvas( width = 430, height = 270 , bg='black') #paramètres du canevas (hauteur, largeur, couleur)
        self.can.pack()
        self.compteurtour=1

        Règles = Button (self.fen, text = 'Règles', command = lambda : self.règles()) #bouton pour expliquer les règles
        Règles.pack (side=TOP)

        valider= Button(self.fen, text = 'Valider', command=lambda: self.valide()) #bouton pour valider nos réponses
        valider.pack(side = BOTTOM)

            #boutons des joueurs pour retirer les allumettes:

        self.bouton1_1 = Button (self.fen, text = '1', command = lambda : self.prendre (1))
        self.bouton2_1 = Button (self.fen, text = '2', command = lambda : self.prendre (2))   
        self.bouton3_1 = Button (self.fen, text = '3', command = lambda : self.prendre (3))

        self.bouton1_1.pack (side=LEFT)
        self.bouton2_1.pack (side=LEFT)
        self.bouton3_1.pack (side=LEFT)

        self.bouton1_2 = Button (self.fen, text = '1', command = lambda : self.prendre (1))
        self.bouton2_2 = Button (self.fen, text = '2', command = lambda : self.prendre (2))
        self.bouton3_2 = Button (self.fen, text = '3', command = lambda : self.prendre (3))

        self.bouton1_2.pack (side=RIGHT)
        self.bouton2_2.pack (side=RIGHT)
        self.bouton3_2.pack (side=RIGHT)

        self.joueur1(DISABLED)
        self.joueur2(NORMAL)


    #condition pour pouvoir activer les boutons du joueur 1 ou 2 selon les tours
    def joueur1(self, etat):
        if etat == DISABLED:
            self.bouton1_1['state'] = 'disabled'
            self.bouton2_1['state'] = 'disabled'
            self.bouton3_1['state'] = 'disabled'
        else:
            self.bouton1_1['state'] = 'normal'
            self.bouton2_1['state'] = 'normal'
            self.bouton3_1['state'] = 'normal'

    def joueur2(self, etat):
        if etat == DISABLED:
            self.bouton1_2['state'] = 'disabled'
            self.bouton2_2['state'] = 'disabled'
            self.bouton3_2['state'] = 'disabled'
        else:
            self.bouton1_2['state'] = 'normal'
            self.bouton2_2['state'] = 'normal'
            self.bouton3_2['state'] = 'normal'
        
    #fonction valide qui permet de effacer le bon nombre d'allumettes voulu et de regarder au quel tour nous sommes pour savoir quel joueur doit jouer. 
    def valide(self):
        self.allumettes -= self.valeurJoue
        self.afficher(self.allumettes)
        self.compteurtour=self.compteurtour+1
        if self.compteurtour% 2== 0:
            self.joueur2(DISABLED)
            self.joueur1(NORMAL)
        else:
            self.joueur2(NORMAL)
            self.joueur1(DISABLED)

        
    #mise en place des allumettes dans le canevas
    def jeu (self):
        self.allumettes= 21
        self.afficher(self.allumettes)
        self.fen.mainloop()
          
    #affichage du nombre d'allumettes nésséssaire celon la variable val
    def afficher (self, val):
        try : self.can.delete (ALL)
        except : pass
        x, y, x2, y2 = 0, 0, 10, 20
        for i in range (val):
            self.can.create_rectangle (x2,50, y2, 200, fill="#FFE4C4")
            self.can.create_rectangle (x2,50,y2, 30, fill="red")
            x2 = x2 + 20
            y2 = x2 + 10

    def prendre (self, x = 1):
        self.valeurJoue = x
        m = self.allumettes - x
        self.afficher (m)
        if (self.allumettes <= 1):
            self.fin ()


    #message de fin(quitter, rejouer)
    def fin(self):
        fenetre = Tk ()
        fenetre.title("FIN")
        fenetre.geometry("150x150")
        fenetre.configure(bg="#999999")
    
        label = Label(fenetre, text="VOUS AVEZ PERDU !!!")
        label.pack()
        
        rejouer = Button (fenetre, fg="blue", text = 'rejouer', command= lambda : self.jeu())
        rejouer.pack (side=RIGHT)

        quitter = Button (fenetre, fg="red", text = 'quitter',command= lambda : fenetre.destroy())
        quitter.pack (side=LEFT)
    


    #énoncer les règles
    def règles(self):
        regles= Tk ()
        label = Label(regles, text="Jouez chacun votre tour. Prenez 1,2 ou 3 allumettes par tour. Le joueur piochant la dernière allumette perd la partie.",bg="#999999")
        label.pack()

        quitter = Button (regles, fg="red", text = 'quitter',command= lambda : regles.destroy())
        quitter.pack (side=BOTTOM)
          
Part = Part()
Part.jeu()

