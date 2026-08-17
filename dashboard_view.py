import tkinter as tk
from tkinter import ttk, messagebox

# On importe le modèle de compte géré par Onja
# import models.compte as compte_model

class DashboardView(tk.Tk):
    def __init__(self, user_id=1):
        super().__init__()
        self.user_id = user_id
        self.title("Tableau de Bord - Gestion Financière")
        self.geometry("500x450")
        self.resizable(False, False)

        # En-tête
        tk.Label(self, text="Tableau de Bord du Mois", font=("Helvetica", 16, "bold")).pack(pady=15)

        # --- BLOC DES CARTES FINANCIÈRES ---
        frame_cards = tk.Frame(self)
        frame_cards.pack(pady=10, fill="x", padx=20)

        # Carte Revenus
        frame_rev = tk.LabelFrame(frame_cards, text="Revenus", font=("Helvetica", 10, "bold"), fg="#28a745", padx=10, pady=10)
        frame_rev.grid(row=0, column=0, padx=10, pady=5, sticky="nsew")
        self.lbl_revenus = tk.Label(frame_rev, text="0.00 Ar", font=("Helvetica", 12))
        self.lbl_revenus.pack()

        # Carte Dépenses
        frame_dep = tk.LabelFrame(frame_cards, text="Dépenses", font=("Helvetica", 10, "bold"), fg="#dc3545", padx=10, pady=10)
        frame_dep.grid(row=0, column=1, padx=10, pady=5, sticky="nsew")
        self.lbl_depenses = tk.Label(frame_dep, text="0.00 Ar", font=("Helvetica", 12))
        self.lbl_depenses.pack()

        # Carte Solde (Calculé selon RG3 par le module d'Onja)
        frame_solde = tk.LabelFrame(frame_cards, text="Solde Actuel", font=("Helvetica", 10, "bold"), fg="#007bff", padx=10, pady=10)
        frame_solde.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
        self.lbl_solde = tk.Label(frame_solde, text="0.00 Ar", font=("Helvetica", 14, "bold"))
        self.lbl_solde.pack()

        frame_cards.grid_columnconfigure(0, weight=1)
        frame_cards.grid_columnconfigure(1, weight=1)

        # --- ALERTE BUDGET (RG4) ---
        self.lbl_alerte = tk.Label(self, text="", font=("Helvetica", 10, "bold"))
        self.lbl_alerte.pack(pady=5)

        # --- BARRE D'ACTIONS (Lien avec le travail d'Olivia) ---
        frame_actions = tk.Frame(self)
        frame_actions.pack(pady=20)

        tk.Button(frame_actions, text="+ Transactions (F2)", width=18, command=self.open_transactions).grid(row=0, column=0, padx=5)
        tk.Button(frame_actions, text="Catégories (F3)", width=18, command=self.open_categories).grid(row=0, column=1, padx=5)
        tk.Button(self, text="Actualiser", command=self.charger_donnees).pack(pady=5)

        # Chargement initial des valeurs
        self.charger_donnees()

    def charger_donnees(self):
        """
        Récupère les données calculées par Onja/Iavosoa et met à jour l'affichage.
        """
        # Exemple d'appel aux fonctions backend :
        # stats = compte_model.get_statistiques_mois(self.user_id)
        # revenus, depenses, solde, taux_budget = stats['revenus'], stats['depenses'], stats['solde'], stats['taux_budget']

        # Simulation de données pour test visuel :
        revenus = 500000.0
        depenses = 420000.0
        solde = revenus - depenses  # RG3
        budget_max = 500000.0
        taux = (depenses / budget_max) * 100  # Pour évaluer RG4

        # Mise à jour des libellés
        self.lbl_revenus.config(text=f"{revenus:,.2f} Ar")
        self.lbl_depenses.config(text=f"{depenses:,.2f} Ar")
        self.lbl_solde.config(text=f"{solde:,.2f} Ar")

        # Application de la règle RG4 (Alerte Orange 80%, Rouge 100%)
        if taux >= 100:
            self.lbl_alerte.config(text="⚠️ ALERTE ROUGE : Budget mensuel dépassé !", fg="red")
        elif taux >= 80:
            self.lbl_alerte.config(text="⚠️ ALERTE ORANGE : 80% du budget atteint !", fg="orange")
        else:
            self.lbl_alerte.config(text="Budget sous contrôle", fg="green")

    def open_transactions(self):
        # Lien vers la vue d'Olivia (F2)
        # from views.transaction_view import TransactionView
        # TransactionView(self, self.user_id)
        messagebox.showinfo("Navigation", "Ouverture de transaction_view.py (Module d'Olivia)")

    def open_categories(self):
        # Lien vers la vue d'Olivia (F3)
        # from views.categorie_view import CategorieView
        # CategorieView(self, self.user_id)
        messagebox.showinfo("Navigation", "Ouverture de categorie_view.py (Module d'Olivia)")

if __name__ == "__main__":
    app = DashboardView()
    app.mainloop()
