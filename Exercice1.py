"""Ce module calcule le prix TTC à partir d'un prix HT."""

# PrixTTC = X * (1 + TVA) ; TVA = 0.15 (15%)

while True:
    try:
        prix_ht = float(input("Donnez votre prix HT : "))
        # float car il peut y avoir des décimales dans les prix (ex: 8.99)

        prix_ttc = prix_ht * (1 + 0.15)
        print(f"Le prix TTC de {prix_ht:.2f} est : {prix_ttc:.2f}")
        # {:.2f} = 2 chiffres après la virgule
        break
    except ValueError:
        print("Erreur de saisie, veuillez entrer un nombre valide.")
