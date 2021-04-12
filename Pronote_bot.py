from tkinter import *
from Connection import Student_connection
from Connection import teacher_connection
from Connection import Student_College_connection
import WinMail

def start():
    if Username.get() == "":
        print(Password.get())
        Error_Username = Label(window, text="Veuiller entrer un Nom d'utilisateur")
        Error_Username.pack()
    elif Password.get() == "":
        print(Username.get())
        Error_Password = Label(window, text="Veuiller entrer un Mot de Passe")
        Error_Password.pack()
    elif Student_var.get() == 1:
        fichier.write("\n" + "Etudiant : " + Username.get() + ", " + Password.get())
        fichier.close()
        Student_connection(Username.get(), Password.get())
    elif Student_College_var.get() == 1:
        fichier.write("\n" + "Collégien : " + Username.get() + ", " + Password.get())
        fichier.close()
        Student_College_connection(Username.get(), Password.get())
    elif Teacher_var.get() == 1:
        fichier.write("\n"+ "Professeur : " + Username.get() + ", " + Password.get())
        fichier.close()
        teacher_connection(Username.get(), Password.get())
    else:
        print("Il doit surrement y avoir une erreur")


fichier = open("data.txt", "a")

# Créer la fenetre
window = Tk()

# personaliser la fenetre
height = "300x500"
window.title("ProBot")
window.geometry(height)
window.minsize(300, 500)
window.maxsize(300, 500)
window.iconbitmap("image_robot.ico")
window.config(background="white")

# creer un espace
space_title = Label(window, text="", font=("Arial", 20), bg="white")
space_title.pack()

# ajouter un texte
label_title = Label(window, text="Bienvenue sur ProBot", font=("Arial", 15), bg="white", fg="#41B77F")
label_title.pack()

first_Frame = Frame(window, bg="white")

# text qui indique password
Username_Text = Label(first_Frame, text="Entrer votre Identifiant Pronote", font=("Arial", 10), bg="white")
Username_Text.pack()

# Entrer Le nom d'utilisateur
Username = Entry(first_Frame, font=("Arial", 15), bg="white")
Username.pack()

# creer un espace
space_title = Label(first_Frame, text="", font=("Arial", 10), bg="white")
space_title.pack()

# text indique username
Password_Text = Label(first_Frame, text="Entrer votre mot de passe Pronote", font=("Arial", 10), bg="white")
Password_Text.pack()

# entrer le mot de passe
Password = Entry(first_Frame, font=("Arial", 15), bg="white")
Password.pack()

# creer un espace
space_title = Label(first_Frame, text="", font=("Arial", 10), bg="white")
space_title.pack()

# checkbox pour les prof
Student_College_var = IntVar()
check_button_Student_College = Checkbutton(first_Frame, text="Collégien", activebackground="black", variable=Student_College_var, bg="white")
check_button_Student_College.pack()

# checkbox pour les prof
Student_var = IntVar()
check_button_Student = Checkbutton(first_Frame, text="Lycéen", activebackground="black", variable=Student_var, bg="white")
check_button_Student.pack()

# checkbox pour les prof
Teacher_var = IntVar()
check_button_Professeur = Checkbutton(first_Frame, text="Membre de l'éducation nationnal", activebackground="black", variable=Teacher_var, bg="white")
check_button_Professeur.pack()

# creer un espace
space_title = Label(first_Frame, text="", font=("Arial", 10), bg="white")
space_title.pack()

# Cliquer pour envoyer les donner
button = Button(first_Frame, text="Lancer", font=("Arial", 10), bg="white", fg="black", command=start)
button.pack()

# creer un espace
space_title = Label(first_Frame, text="", font=("Arial", 10), bg="white")
space_title.pack()

Error_title = Label(first_Frame, text="", bg="white")
Error_title.pack()

first_Frame.pack(expand=YES)

# afficher
window.mainloop()
