# Récupérer le un prix HT et afficher le PrixTTC

while True :
    try :
        PrixHT = float(input("Donnez votre prix HT : "))

        # PrixTTC=X*(1+TVA)    .15 = 0.15 (15%)

        print("Le prix TTC de notre prix HT : {0:.2f} est : {1:.2f}".format(PrixHT, PrixHT * (1 + .15)))
        # {:.2f} c'est pour dire que je veux 2 chiffre après la virgurle
        break
    except ValueError :
        print("Faites attention Erreur de saisie :( ")


# float parce que enventuelement il y a des , flottante dans les prix come 8.990dt







