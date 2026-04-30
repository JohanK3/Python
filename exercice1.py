"""Ce module calcule le prix TTC à partir d'un prix HT."""

# Utilisation d'une constante pour la TVA (convention de nommage en majuscules)
TVA = 0.15

def calculer_prix():
    """Demande un prix à l'utilisateur et affiche le TTC."""
    while True:
        try:
            entree = input("Donnez votre prix HT : ")
            prix_ht = float(entree)

            prix_ttc = prix_ht * (1 + TVA)

            # Utilisation de f-string (déjà présent dans ta correction, c'est parfait)
            print(f"Le prix TTC de {prix_ht:.2f} est : {prix_ttc:.2f}")
            break
        except ValueError:
            print("Erreur de saisie, veuillez entrer un nombre valide.")

if __name__ == "__main__":
    calculer_prix()