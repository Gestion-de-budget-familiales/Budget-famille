class Compte:
    def __init__(self, solde_initial, budget_limite=0):
        self.solde_initial = solde_initial
        self.budget_limite = budget_limite

    # RG3: Solde = SoldeInitial + Revenus - Dépenses
    def calculer_solde(self, total_revenus, total_depenses):
        return self.solde_initial + total_revenus - total_depenses

    # RG4: Alerte orange 80%, rouge 100%
    def verifier_alerte(self, total_depenses):
        if self.budget_limite <= 0:
            return "ok"

        pourcentage = (total_depenses / self.budget_limite) * 100

        if pourcentage >= 100:
            return "rouge"
        elif pourcentage >= 80:
            return "orange"
        return "ok"
