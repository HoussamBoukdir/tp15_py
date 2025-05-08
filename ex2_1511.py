class Compte:
    def __init__(self, numero, solde_initial):
        
        self.numero = numero              
        self.solde = solde_initial         

    def afficher_solde(self):
        
        print(f"Compte numéro: {self.numero}, Solde: {self.solde:.2f} DH")

    def obtenir_solde(self):
    
        return self.solde


numero = input("Entrez le numéro du compte : ")
solde_initial = float(input("Entrez le solde initial : "))


compte = Compte(numero, solde_initial)


compte.afficher_solde()


print(f"Solde actuel via méthode : {compte.obtenir_solde():.2f} DH")
