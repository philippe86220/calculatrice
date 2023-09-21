#Le code du design de la calculatrice provient du site  : https://koor.fr/Python/Tutoriel_Tkinter/tkinter_layout_grid.wp
# je l'ai modifié en ajoutant deux lignes de boutons et en l'adaptant pour Mac
from statistics import mean
import tkinter as tk
import math
from tkmacosx import Button
from tkinter import messagebox
import re

# On définit une classe qui dérive de la classe Tk (la classe de fenêtre).
class Calculatrice(tk.Tk):

    def __init__(self):
        self.calcul = ""
        self.var=""
        self.var2=""
        self.operation=""
        self.list_operations = []
        self.x = 0
        self.bool_binaire = False
        self.liste =[] # fonction somme, multiplication
        
        # On appelle le constructeur parent
        super().__init__()
        self.creation_design()
        self.create_menu_bar()

       #calcul général - ajoute un symbole (chiffre, +, - ...) 
    def ajout_calcul(self,symbol):
        self.calcul += str(symbol)
        self.var.set(self.calcul)
        
        #évalue le calcul avec la fonction eval()
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
            
      #gestion des événements clavier      
    def clavier(self,event):
        clavier = ('.','0','1','2','3','4','5','6','7','8','9','/','*','-','+','(',')',',')
        if event.char == ',':
             event.char = '.'   
        if event.char in clavier:
            self.ajout_calcul(event.char)
            
    def even_calcul(self,event):
        self.eval_calcul()
            
       #remise à zéro 
    def effacer_ecran(self):
        self.calcul = ""
        #self.calcul = int(self.calcul )
        self.var.set("0")
        
        # fonctions de calcul    
    def unSurX(self):
        try:
            resultat = str(eval('1/ ' + self.calcul))
            self.var.set(resultat)
            self.operation = f"1 / {self.calcul}  = {resultat}"
            self.list_operations.append(self.operation)
            fenetre.title(f"{self.operation}")
            self.calcul = resultat
        except Exception as exc:
            if isinstance(exc, ZeroDivisionError):
               self.var.set("division par zéro")
        
    def pourcent(self):  
        nombres = [float(c) for c in re.findall(r'-?\d+\.?\d*', self.calcul)]
        if len(nombres) >1 :
            resultat = (nombres[0] * nombres[1])/100
            self.var.set(resultat)
            self.operation = f"{nombres[1]} % de {nombres[0]}  = {resultat} "
            self.list_operations.append(self.operation)
            fenetre.title(f"{self.operation}")
            self.calcul = str(nombres[0]) +  '+'  + str(resultat)
        else:
            resultat = nombres[0] / 100
            self.var.set(resultat)
            self.operation = f"1 % de {nombres[0]}  = {resultat} "
            self.list_operations.append(self.operation)
            self.calcul =  str(resultat)
        
    def binaire(self):
        if 'x' in self.calcul:
            self.calcul = f'{int(self.calcul,16)}'
        try:   
            self.operation = f"{self.calcul} = "
            self.calcul = bin((int(self.calcul)))
            self.calcul= str( self.calcul)
            self.operation += self.calcul
            self.var.set(self.calcul)
            self.list_operations.append(self.operation)
            fenetre.title(f"{self.operation}")
            self.bool_binaire = True
        except:
            self.calcul=""
            self.var.set("erreur votre valeur doit-être un entier décimal")
            
    def hexa(self):
        if 'b' in self.calcul:
            self.calcul = f'{int(self.calcul,2)}'
        try:
            self.operation = f"{self.calcul} = " 
            self.calcul = hex((int(self.calcul)))
            self.calcul= str( self.calcul)
            self.operation += self.calcul
            self.var.set(self.calcul)
            self.list_operations.append(self.operation)
            fenetre.title(f"{self.operation}")
            self.bool_binaire = False
        except:
            self.var.set("erreur votre valeur doit-être un entier décimal")
            self.calcul=""
            
    def base_dix(self):
        try:
            self.operation = f"En base 10 : {self.calcul} = "
            if self.bool_binaire ==True:
                self.calcul = int(self.calcul,2) 
            elif self.bool_binaire ==False:
                self.calcul =int(self.calcul,16)
            self.calcul = str( self.calcul)
            self.operation += self.calcul
            self.var.set(self.calcul)
            self.list_operations.append(self.operation)
            fenetre.title(f"{self.operation}")
        except:
            self.calcul=""
            self.var.set("erreur votre valeur doit-être un entier")
            
    def racine_carre(self):
        self.operation = f"Racine carrée de {self.calcul} = " 
        self.calcul =math.sqrt(float(eval(str(self.calcul))))
        self.calcul= str( self.calcul)
        self.operation += self.calcul
        self.var.set(self.calcul)
        self.list_operations.append(self.operation)
        fenetre.title(f"{self.operation}")

    def factorielle(self):
        try:
            self.operation = f"factorielle de {self.calcul} = " 
            self.calcul =math.factorial(int(self.calcul))
            self.calcul= str( self.calcul)
            self.operation += self.calcul
            self.var.set(self.calcul)
            self.list_operations.append(self.operation)
            fenetre.title(f"{self.operation}")
        except:
            self.var.set("erreur votre valeur doit-être un entier décimal")
            self.calcul=""
            
    def absolue(self):
        self.operation = f"Valeur absolue de {self.calcul} = " 
        self.calcul =abs(float(self.calcul))
        self.calcul= str( self.calcul)
        self.operation += self.calcul
        self.var.set(self.calcul)
        self.list_operations.append(self.operation)
        fenetre.title(f"{self.operation}")

        #mémorisation des opérations
    def memoire(self):
        monTexte = ""
        for elements in self.list_operations:
           monTexte+= '{}\n'.format(" ".join (elements))
        toplevel = tk.Toplevel()
        toplevel.geometry('2000x1000')
        mon_text = tk.Text(toplevel, height = 58, width =220, fg="black", font=("Arial", 15))
        mon_text.insert (tk.END, monTexte)
        mon_text.pack()
        toplevel.tk.call('tk::PlaceWindow', toplevel)

        #effacement de la mémorisation des opérationset remise à zéro
    def effacement_memoire(self):
        self.list_operations.clear()
        self.operation=""
        self.calcul = ""
        self.var.set("0")
        self.title("Calculatrice")
        
        #design calculatrice
    def creation_design(self):
        # On prépare une grille de huit lignes et 4 colonnes
        # La première ligne cherchera à saturer l'espace restant dans la fenêtre.
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=0)
        self.grid_rowconfigure(2, weight=0)
        self.grid_rowconfigure(3, weight=0)
        self.grid_rowconfigure(4, weight=0)
        self.grid_rowconfigure(5, weight=0)
        self.grid_rowconfigure(6, weight=0)
        self.grid_rowconfigure(7, weight=0)
        self.grid_rowconfigure(8, weight=0)
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

        self.effacement = Button(self, text="AC", **self.default_button_style, command = lambda : self.effacement_memoire() )
        self.effacement.grid(column=1, row=1, **self.default_button_grid)
        
        self.racine = Button(self, text="√", **self.default_button_style, command = lambda : self.racine_carre() )
        self.racine.grid(column=2, row=1, **self.default_button_grid)

        self.div2 = Button(self, text="1/x", **self.default_button_style, command = self.unSurX)
        self.div2.grid(column=3, row=1, **self.default_button_grid)        
        
        # Troisième ligne
        self.bin = Button(self, text="bin", **self.default_button_style, command = self.binaire)
        self.bin.grid(column=0, row=2, **self.default_button_grid)

        self.hex = Button(self, text="hex", **self.default_button_style, command = self.hexa )
        self.hex.grid(column=1, row=2, **self.default_button_grid)

        self.dec = Button(self, text="dec", **self.default_button_style, command = self.base_dix )
        self.dec.grid(column=2, row=2, **self.default_button_grid)

        self.pourcent = Button(self, text="%", **self.default_button_style, command = self.pourcent)
        self.pourcent.grid(column=3, row=2, **self.default_button_grid)

        # Quatrième ligne
        self.puissance = Button(self, text="^", **self.default_button_style, command = lambda : self.ajout_calcul('**'))
        self.puissance.grid(column=0, row=3, **self.default_button_grid)

        self.factorial = Button(self, text="x!", **self.default_button_style, command = self.factorielle)
        self.factorial.grid(column=1, row=3, **self.default_button_grid)

        self.abs = Button(self, text="abs", **self.default_button_style, command = self.absolue)
        self.abs.grid(column=2, row=3, **self.default_button_grid)

        self.div = Button(self, text="/", **self.default_button_style, command = lambda : self.ajout_calcul("/"))
        self.div.grid(column=3, row=3, **self.default_button_grid)
        
        # Cinquième ligne
        self.d7 = Button(self, text="mem", **self.default_button_style, command = lambda : self.memoire())
        self.d7.grid(column=0, row=4, **self.default_button_grid)

        self.d8 = Button(self, text="(", **self.default_button_style, command = lambda : self.ajout_calcul("("))
        self.d8.grid(column=1, row=4, **self.default_button_grid)

        self.d9 = Button(self, text=")", **self.default_button_style, command = lambda : self.ajout_calcul(")"))
        self.d9.grid(column=2, row=4, **self.default_button_grid)

        self.mul = Button(self, text="*", **self.default_button_style, command = lambda : self.ajout_calcul("*"))
        self.mul.grid(column=3, row=4, **self.default_button_grid)
        
        
        # Sixième ligne
        self.d7 = Button(self, text="7", **self.default_button_style, command = lambda : self.ajout_calcul(7))
        self.d7.grid(column=0, row=5, **self.default_button_grid)

        self.d8 = Button(self, text="8", **self.default_button_style, command = lambda : self.ajout_calcul(8))
        self.d8.grid(column=1, row=5, **self.default_button_grid)

        self.d9 = Button(self, text="9", **self.default_button_style, command = lambda : self.ajout_calcul(9))
        self.d9.grid(column=2, row=5, **self.default_button_grid)

        self.sub = Button(self, text="-", **self.default_button_style, command = lambda : self.ajout_calcul("-"))
        self.sub.grid(column=3, row=5, **self.default_button_grid)

        # Septième ligne
        self.d4 = Button(self, text="4", **self.default_button_style, command = lambda : self.ajout_calcul(4))
        self.d4.grid(column=0, row=6, **self.default_button_grid)

        self.d5 = Button(self, text="5", **self.default_button_style, command = lambda : self.ajout_calcul(5))
        self.d5.grid(column=1, row=6, **self.default_button_grid)

        self.d6 = Button(self, text="6", **self.default_button_style, command = lambda : self.ajout_calcul(6))
        self.d6.grid(column=2, row=6, **self.default_button_grid)

        self.add = Button(self, text="+", **self.default_button_style, command = lambda : self.ajout_calcul("+"))
        self.add.grid(column=3, row=6, **self.default_button_grid)

       # Huitième ligne
        self.d1 = Button(self, text="1", **self.default_button_style, command = lambda : self.ajout_calcul(1))
        self.d1.grid(column=0, row=7, **self.default_button_grid)

        self.d2 = Button(self, text="2", **self.default_button_style, command = lambda : self.ajout_calcul(2))
        self.d2.grid(column=1, row=7, **self.default_button_grid)

        self.d3 = Button(self, text="3", **self.default_button_style, command = lambda : self.ajout_calcul(3))
        self.d3.grid(column=2, row= 7, **self.default_button_grid)

        self.equal = Button(self, text="=",**self.equal_button_style, command = self.eval_calcul) 
        self.equal.grid(column=3, row=7, rowspan=2, **self.default_button_grid)


        # Neuvième ligne
        self.d0 = Button(self, text="0", **self.default_button_style, command = lambda : self.ajout_calcul(0))
        self.d0.grid(column=0, row=8, columnspan=2, **self.default_button_grid)

        self.dot = Button(self, text=".", **self.default_button_style, command = lambda : self.ajout_calcul("."))
        self.dot.grid(column=2, row=8, **self.default_button_grid)

        # On change la couleur de fond et les marges de la fenêtre.
        self.configure(bg="#333333", padx=10, pady=10)

        #Création barre de menu
    def create_menu_bar(self):
        self.menu_bar = tk.Menu(self)
        
        self.menu_file = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Fichier", menu=self.menu_file)
        self.menu_file.add_command(label="π", command = lambda : self.ajout_calcul(math.pi))
        self.menu_file.add_command(label="Calculs divers", command =  self.calculs)
        self.menu_file.add_separator()
        self.menu_file.add_command(label="Quitter", command=self.destroy)
        self.config(menu=self.menu_bar)

        #Toplevel calculs divers
    def calculs(self):
        self.effacer_ecran()
        self.operation=""
        self.toplevel = tk.Toplevel()
        self.toplevel.geometry('1700x250')
        self.toplevel.title(" Pour somme et addition mettez un espace entre chaque chiffre")
        self.calcul_somme = tk.Entry(self.toplevel, width = 150)
        self.calcul_somme.pack()
        self.btn_somme = Button(self.toplevel, text = "somme", command = self.addition, width = 215, font= ('arial', 14))
        self.btn_somme.pack()
        self.btn_moyenne = Button(self.toplevel, text = "moyenne", command = self.moyenne, width = 215, font= ('arial', 14))
        self.btn_moyenne.pack()
        self.btn_multiplication = Button(self.toplevel, text = "multiplication", command = self.multiplication, width = 215, font= ('arial', 14))
        self.btn_multiplication.pack()
        self.btn_calcul_divers = Button(self.toplevel, text = "calculs divers", command = self.calc, width = 215, font= ('arial', 14))
        self.btn_calcul_divers.pack()
        self.btn_fonction = Button(self.toplevel, text = "calcul avec une variable", command = self.fonction, width = 215, font= ('arial', 14))
        self.btn_fonction.pack()
        self.calcul_fonction = tk.Entry(self.toplevel, width = 50)
        self.calcul_fonction.insert(0, "Entrez la valeur de x")
        self.calcul_fonction.pack()
        self.toplevel.tk.call('tk::PlaceWindow', self.toplevel)
    
    def addition(self):
        try:
            nb_virgules = self.calcul_somme.get().count(',')
            remplace = self.calcul_somme.get().replace(',','.',nb_virgules)
            self.liste =(remplace.split( ))
            float_lst = [float(item) for item in self.liste]
            self.calcul = str((sum(float_lst)))
            for  i in range( len (float_lst)):
                self.operation+= str(float_lst[i])
                if i < len (float_lst)-1:
                    self.operation+=  ' + '
            self.operation+= " = " + str(self.calcul)
            self.list_operations.append(self.operation)
            self.var.set(self.operation)
            fenetre.title(f"{self.operation}")
            self.toplevel.destroy()
        except:
            self.var.set("erreur par exemple : un espace remplace le +")
            self.calcul=""
            
    def moyenne(self):
        nb_virgules = self.calcul_somme.get().count(',')
        remplace = self.calcul_somme.get().replace(',','.',nb_virgules)
        self.liste =(remplace.split( ))
        float_lst = [float(item) for item in self.liste]
        self.calcul = str(mean(float_lst))
        self.operation = f"Moyenne de {float_lst} = {self.calcul}"
        self.list_operations.append(self.operation)
        self.var.set(self.operation)
        fenetre.title(f"{self.operation}")
        self.toplevel.destroy()
            
    def multiplication(self):
        try:
            resultat =1
            nb_virgules = self.calcul_somme.get().count(',')
            remplace = self.calcul_somme.get().replace(',','.',nb_virgules)
            self.liste =(remplace.split( ))
            float_lst = [float(item) for item in self.liste]
            for element in float_lst:
                resultat *= element
            self.calcul = str(resultat)
            for  i in range( len (float_lst)):
                self.operation+= str(float_lst[i])
                if i < len (float_lst)-1:
                    self.operation+=  ' * '
            self.operation+= " = " + str(self.calcul)
            self.list_operations.append(self.operation)
            self.var.set(self.operation)
            fenetre.title(f"{self.operation}")
            self.toplevel.destroy()
        except:
            self.var.set("erreur par exemple : un espace remplace le *")
            self.calcul=""

    def calc(self):
        nb_virgules = self.calcul_somme.get().count(',')
        remplace = self.calcul_somme.get().replace(',','.',nb_virgules)
        self.calcul =  remplace
        self.eval_calcul()
        self.toplevel.destroy()
        
            
    def fonction(self):
        try:
            nb_virgules = self.calcul_fonction.get().count(',')
            remplace = self.calcul_fonction.get().replace(',','.',nb_virgules)
            self.x =  remplace
            x = float(self.x)
            nb_virgules = self.calcul_somme.get().count(',')
            remplace2 = self.calcul_somme.get().replace(',','.',nb_virgules)
            self.calcul = remplace2
            self.operation = f" x =  {x} ➔ {self.calcul} =  "
            self.calcul = eval(str(self.calcul))
            self.calcul = str(self.calcul)
            self.operation += self.calcul     
            self.list_operations.append(self.operation)
            self.var.set(self.operation)
            fenetre.title(f"{self.operation}")
            self.toplevel.destroy()
        except:
            self.var.set("erreur")
            self.calcul=""
            
fenetre= Calculatrice()
fenetre.title("Calculatrice")
fenetre.bind("<Return>", fenetre.even_calcul)
fenetre.bind("<KP_Enter>", fenetre.even_calcul)
fenetre.bind("<Key>", fenetre.clavier)
fenetre.tk.call('tk::PlaceWindow', fenetre)

fenetre.mainloop()

