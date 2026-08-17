class Transaction:
    def __init__(self, montant, type_transaction, description=""):
        self.montant = montant
        self.type_transaction = type_transaction  # 'revenu' na 'depense'
        self.description = description
