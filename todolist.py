import tkinter as tk
from glob import glob
from tkinter.font import Font
from  main import Taches
tch = Taches() 

tch.db_connecter()
fenetre = tk.Tk()

liste_label = []
def supprimer():
    global liste_label
    for label in liste_label:
        label.destroy()
    liste_label = []
    
def cliquez(event):
    tache = event.widget.cget('text')
    entree.delete(0,tk.END)
    entree.insert(0,tache)

def terminer_label():
    tache = entree.get()
    tch.terminer(tache)
    affichez_taches()


def affichez_taches():
    global liste_label
    supprimer()
    tch.db_connecter()
    for idx,tache,etat in tch.recuperer():
        label = tk.Label(text=tache,font=('size=10'),padx=10,cursor="hand2",borderwidth=1,
                        bg='Red' if etat==1 else fenetre.cget('bg'),
                        relief='raised')
        liste_label.append(label)
        label.bind("<Button-1>",cliquez)
        label.pack(fill=tk.BOTH,expand=1)
    tch.db_fermer()

def fermer():
    tch.db_fermer()
    fenetre.destroy()


def plus():
    tache = entree.get()
    if tache:
        tch.ajouter(tache,etat=0)
        affichez_taches()


def Supprimer_label():
    tache = entree.get()
    tch.supprimer(tache)
    affichez_taches()


frame = tk.Frame()
entree = tk.Entry(frame,width=30)
btn_plus = tk.Button(frame,text='Ajouter',command=plus)
btn_supprimer = tk.Button(frame,text='Supprimer', command=Supprimer_label)
btn_moins = tk.Button(frame,text='terminer', command=terminer_label)


entree.grid(row=0,column=0,padx=10)
btn_plus.grid(row=0,column=1,padx=3)
btn_supprimer.grid(row=0,column=2,padx=3)
btn_moins.grid(row=0,column=4,padx=3)
frame.pack()

affichez_taches()
fenetre.protocol("WM_DELETE_WINDOW",fermer)
fenetre.mainloop()

tch.db_fermer()



