# import tkinter as tk
# from tkinter.font import Font

# fenetre = tk.Tk()
# monlabel = tk.Label(text='Ma premiere fenetre Tkinter',
#                      foreground='blue',
#                        background='red',
#                        width= 20,
#                        height=4,
#                        font= Font(family='sans serif',weight='bold',size=12)
#                        )
# monlabel.pack()

# montexte = tk.Label(text=5)

# def ma_fonction():
#     montext=montexte.cget("text")
#     montext +=1
#     montexte.configure(text=montexte)

# montexte.pack()

# button = tk.Button(text='Mon bouton',bd=10,
#                    command=ma_fonction,
#                    fg='blue',
#                    bg='red',
#                    padx=20,
#                    pady=10)

# button.pack()
# fenetre.mainloop()
import sqlite3
class Taches:
    def __init__(self):
        self.db_nom = 'tache.db'
        self.db_connecter()
        self.curseur.execute('''CREATE TABLE IF NOT EXISTS Taches
                             (id INTEGER PRIMARY KEY AUTOINCREMENT,tache TEXTE,etat INTEGER )''')
        self.db_fermer()

    def db_connecter(self):
        self.connection =sqlite3.connect(self.db_nom)
        self.curseur = self.connection.cursor()
    
    def db_fermer(self):
        self.connection.close()
    
    def ajouter(self,tache,etat=0):
        self.db_connecter()
        requette = f"INSERT INTO Taches(tache,etat) VALUES(?,?)"
        self.curseur.execute(requette,(tache,etat))
        self.connection.commit()
        self.db_fermer()

    def existe(self, tache):
        requette = f"SELECT * FROM Taches WHERE tache = '{tache}'"
        resultat = self.curseur.execute(requette).fetchone()
        return True if resultat else False
        
        

    def afficher(self):
        requette = "SELECT * FROM Taches"
        taches = self.curseur.execute(requette).fetchall()
        for t in taches:
            if t[2] == True:
                print(f"{t[0]} - {t[1]}, {t[2]}")
            else:
                print(f"{t[0]} - {t[1]}, {t[2]}")

    def recuperer(self):
        requette = "SELECT * FROM Taches"
        return self.curseur.execute(requette).fetchall()
    
    def terminer(self,tache):
        self.db_connecter()
        requette =f"UPDATE Taches SET etat = 1 WHERE tache = ? " 
        self.curseur.execute(requette,(tache,))
        self.connection.commit()
        self.db_fermer()
    
    def supprimer(self,tache):
        self.db_connecter()
        requette = "DELETE FROM Taches WHERE tache =?"
        self.curseur.execute(requette,(tache,))
        self.connection.commit()
        self.db_fermer()



taches = Taches()
