def demander_nombre_entre_min_et_max(min, max):
    """Asks user to enter an integer between min and max."""
    while True:
        n = input(message)
        if n.isdigit():
            n = int(n)
        else:
            continue

        if min <= n <= max:
            return nn

fonction choisir_entier_aleatoire_entre_min_et_max(min, min):
    code de la fonction
fin fonction

def demander_si_continuer():
    response = input("Voulez-vous continuer à miser? (oui/non) ")
    if response == 'oui':
        return True
    return False

def main():
    argent_disponible = 1000

    while demander_si_continuer() and argent_disponible > 0:
        n = demander_nombre_entre_min_et_max(1, 50)
        mise = demander_nombre_entre_min_et_max(1, argent_disponible)
        // vérifier que la mise est inférieure ou égale à l'argent disponible (déjà ok)
        resultat = choisir_entier_aleatoire_entre_min_et_max(1, 50)
        if n == resultat:
            ajouter 2 fois la mise à l'argent disponible
        elif ((n % 2) == (resultat % 2)):
            ajouter... à l'argent disponible
        sinon
            l'argent misé est perdu
        
    fin tant


main()