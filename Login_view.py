import tkinter as tk
from tkinter import messagebox

# On importe le contrôleur géré par Iavosoa
# import controllers.auth_controller as auth_ctrl

class LoginView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestion Financière - Connexion")
        self.geometry("350x400")
        self.resizable(False, False)

        # Formulaire Connexion / Inscription
        self.is_login_mode = True

        self.label_title = tk.Label(self, text="Connexion", font=("Helvetica", 16, "bold"))
        self.label_title.pack(pady=20)

        # Champ Nom d'utilisateur / Email
        tk.Label(self, text="Nom d'utilisateur :").pack(anchor="w", padx=30)
        self.entry_username = tk.Entry(self, width=30)
        self.entry_username.pack(padx=30, pady=5)

        # Champ Mot de passe
        tk.Label(self, text="Mot de passe :").pack(anchor="w", padx=30)
        self.entry_password = tk.Entry(self, show="*", width=30)
        self.entry_password.pack(padx=30, pady=5)

        # Bouton principal
        self.btn_submit = tk.Button(self, text="Se connecter", bg="#28a745", fg="white", width=25, command=self.handle_submit)
        self.btn_submit.pack(pady=20)

        # Basculer entre Connexion et Inscription
        self.btn_toggle = tk.Button(self, text="Pas de compte ? S'inscrire", relief="flat", fg="blue", command=self.toggle_mode)
        self.btn_toggle.pack()

    def toggle_mode(self):
        self.is_login_mode = not self.is_login_mode
        if self.is_login_mode:
            self.label_title.config(text="Connexion")
            self.btn_submit.config(text="Se connecter", bg="#28a745")
            self.btn_toggle.config(text="Pas de compte ? S'inscrire")
        else:
            self.label_title.config(text="Inscription")
            self.btn_submit.config(text="S'inscrire", bg="#007bff")
            self.btn_toggle.config(text="Déjà un compte ? Se connecter")

    def handle_submit(self):
        username = self.entry_username.get().strip()
        password = self.entry_password.get().strip()

        if not username or not password:
            messagebox.showwarning("Erreur", "Veuillez remplir tous les champs.")
            return

        if self.is_login_mode:
            # Appel à la fonction de Iavosoa
            # success, user_or_err = auth_ctrl.se_connecter(username, password)
            success = True  # Simulation pour le test
            
            if success:
                messagebox.showinfo("Succès", f"Bienvenue, {username} !")
                self.destroy()  # Ferme la fenêtre de login
                # Ouvre le Dashboard de Felantsoa
                # DashboardView(user_id=user_or_err.id).mainloop()
            else:
                messagebox.showerror("Erreur", "Identifiants incorrects.")
        else:
            # Appel de la fonction d'inscription de Iavosoa
            # success, msg = auth_ctrl.s_inscrire(username, password)
            success = True  # Simulation pour le test
            
            if success:
                messagebox.showinfo("Succès", "Compte créé avec succès ! Vous pouvez vous connecter.")
                self.toggle_mode()
            else:
                messagebox.showerror("Erreur", "Échec de l'inscription.")

if __name__ == "__main__":
    app = LoginView()
    app.mainloop()
