#Le code du design de la calculatrice provient du site  : https://koor.fr/Python/Tutoriel_Tkinter/tkinter_layout_grid.wp
# je l'ai modifié en ajoutant une ligne de boutons et en l'adaptant pour Mac

import tkinter as tk
import math
from tkmacosx import Button
from tkinter import messagebox


# On définit une classe qui dérive de la classe Tk (la classe de fenêtre).
class Calculatrice(tk.Tk):

    def __init__(self):
        self.calcul = ""
        self.var=""
        self.var2=""
        self.operation=""
        self.list_operations = []
        # On appelle le constructeur parent
        super().__init__()
        self.creation_design()

    def ajout_calcul(self,symbol):
        self.calcul += str(symbol)
        self.var.set(self.calcul)
       
        
    def eval_calcul(self):
        try:
            self.operation = f"{self.calcul} = " 
            self.calcul = str(eval(self.calcul))
            self.operation += self.calcul
            self.var.set(self.calcul)
            self.list_operations.append(self.operation)
            fenetre.title(f"{self.operation}")
           
        except:
            self.effacer_ecran()
            self.var.set("erreur") 
            
    def effacer_ecran(self):
        self.calcul = ""
        self.var.set("0")

    def racine_carre(self):
        #self.calcul =str(math.sqrt(float(eval(self.calcul))))
        self.operation = f"Racine carrée de {self.calcul} = " 
        self.calcul =math.sqrt(float(eval(str(self.calcul))))
        self.calcul= str( self.calcul)
        self.operation += self.calcul
        self.var.set(self.calcul)
        self.list_operations.append(self.operation)
        fenetre.title(f"{self.operation}")

    def even_calcul(self,event):
       self.eval_calcul()
        
    def secondaire(self):
        monTexte = ""
        for elements in self.list_operations:
           monTexte+= '{}\n'.format(" ".join (elements))
        self.var2 = tk.StringVar()
        self.var2.set(monTexte)
        toplevel = tk.Toplevel()
        toplevel.geometry('600x550')
        label = tk.Label(toplevel, textvariable=self.var2,fg="black", font=("Arial", 15))
        label.pack()
    
    def creation_design(self):
        # On prépare une grille de sept lignes et 4 colonnes
        # La première ligne cherchera à saturer l'espace restant dans la fenêtre.
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=0)
        self.grid_rowconfigure(3, weight=0)
        self.grid_rowconfigure(4, weight=0)
        self.grid_rowconfigure(5, weight=0)
        self.grid_rowconfigure(6, weight=0)
        # On force la taille des colonne avec le paramètre uniform. "same_group" est texte libre.
        # Le fait que les 4 colonnes utilisent la même chaîne force la même taille. 
        # Les paramètres weight servent uniquement pour que les 4 colonnes utilisent 100% de la 
        # largeur de la fenêtre.
        self.grid_columnconfigure(0, weight=1, uniform="same_group")
        self.grid_columnconfigure(1, weight=1, uniform="same_group")
        self.grid_columnconfigure(2, weight=1, uniform="same_group")
        self.grid_columnconfigure(3, weight=1, uniform="same_group")

        # On définit quelques éléments de style pour les boutons.
        self.default_button_style = {
            "bg": "#595959", "fg": "white", "highlightthickness": 0,
            "font": ("Arial", 25, "bold")
        }
        self.equal_button_style = self.default_button_style | {"bg": "#f05a2D"}
        self.default_button_grid = {"padx": 10, "pady": 10, "sticky": "nsew"}

        # Première ligne
        self.var = tk.StringVar()
        self.text_resultat = tk.Label(self, textvariable=self.var, anchor='e',  bg="#a2af77", fg="white", font=("Arial", 24))
        self.text_resultat.grid(column=0, row=0, columnspan=4,**self.default_button_grid)
        self.var.set("0")
        
        # Seconde ligne
        self.mc = Button(self, text="C", **self.default_button_style, command = self.effacer_ecran )
        self.mc.grid(column=0, row=1, **self.default_button_grid)

        self.mplus = Button(self, text="√", **self.default_button_style, command = lambda : self.racine_carre() )
        self.mplus.grid(column=1, row=1, **self.default_button_grid)

        self.div = Button(self, text="/", **self.default_button_style, command = lambda : self.ajout_calcul("/"))
        self.div.grid(column=2, row=1, **self.default_button_grid)

        self.mul = Button(self, text="*", **self.default_button_style, command = lambda : self.ajout_calcul("*"))
        self.mul.grid(column=3, row=1, **self.default_button_grid)
        
       # Troisième ligne
        self.d7 = Button(self, text="mem", **self.default_button_style, command = lambda : self.secondaire())
        self.d7.grid(column=0, row=2, **self.default_button_grid)

        self.d8 = Button(self, text="(", **self.default_button_style, command = lambda : self.ajout_calcul("("))
        self.d8.grid(column=1, row=2, **self.default_button_grid)

        self.d9 = Button(self, text=")", **self.default_button_style, command = lambda : self.ajout_calcul(")"))
        self.d9.grid(column=2, row=2, **self.default_button_grid)

        self.sub = Button(self, text="-", **self.default_button_style, command = lambda : self.ajout_calcul("-"))
        self.sub.grid(column=3, row=2, **self.default_button_grid)
        
        # Quatrième ligne
        self.d7 = Button(self, text="7", **self.default_button_style, command = lambda : self.ajout_calcul(7))
        self.d7.grid(column=0, row=3, **self.default_button_grid)

        self.d8 = Button(self, text="8", **self.default_button_style, command = lambda : self.ajout_calcul(8))
        self.d8.grid(column=1, row=3, **self.default_button_grid)

        self.d9 = Button(self, text="9", **self.default_button_style, command = lambda : self.ajout_calcul(9))
        self.d9.grid(column=2, row=3, **self.default_button_grid)

        self.sub = Button(self, text="-", **self.default_button_style, command = lambda : self.ajout_calcul("-"))
        self.sub.grid(column=3, row=3, **self.default_button_grid)

        # Cinquième ligne
        self.d4 = Button(self, text="4", **self.default_button_style, command = lambda : self.ajout_calcul(4))
        self.d4.grid(column=0, row=4, **self.default_button_grid)

        self.d5 = Button(self, text="5", **self.default_button_style, command = lambda : self.ajout_calcul(5))
        self.d5.grid(column=1, row=4, **self.default_button_grid)

        self.d6 = Button(self, text="6", **self.default_button_style, command = lambda : self.ajout_calcul(6))
        self.d6.grid(column=2, row=4, **self.default_button_grid)

        self.add = Button(self, text="+", **self.default_button_style, command = lambda : self.ajout_calcul("+"))
        self.add.grid(column=3, row=4, **self.default_button_grid)

        # Sixième ligne
        self.d1 = Button(self, text="1", **self.default_button_style, command = lambda : self.ajout_calcul(1))
        self.d1.grid(column=0, row=5, **self.default_button_grid)

        self.d2 = Button(self, text="2", **self.default_button_style, command = lambda : self.ajout_calcul(2))
        self.d2.grid(column=1, row=5, **self.default_button_grid)

        self.d3 = Button(self, text="3", **self.default_button_style, command = lambda : self.ajout_calcul(3))
        self.d3.grid(column=2, row= 5, **self.default_button_grid)

        self.equal = Button(self, text="=",**self.equal_button_style, command = self.eval_calcul) 
        self.equal.grid(column=3, row=5, rowspan=2, **self.default_button_grid)

        # Septième ligne
        self.d0 = Button(self, text="0", **self.default_button_style, command = lambda : self.ajout_calcul(0))
        self.d0.grid(column=0, row=6, columnspan=2, **self.default_button_grid)

        self.dot = Button(self, text=".", **self.default_button_style, command = lambda : self.ajout_calcul("."))
        self.dot.grid(column=2, row=6, **self.default_button_grid)

        # On change la couleur de fond et les marges de la fenêtre.
        self.configure(bg="#333333", padx=10, pady=10)


fenetre= Calculatrice()
fenetre.title("Calculatrice")
fenetre.bind("<Return>", fenetre.even_calcul)
fenetre.mainloop()

