import random

print("// La roulette //")
print("Vous arriver dans le Casino")

nombre_mise = int(input('Quel nombre voulez-vous misé entre 0 et 49:'))
deposer_nombre = int(input('Quel nombre souhaite tu misé:'))
gain = 0

if nombre_mise % 2 == 0:
    couleur_mise = "Noire"
else:
    couleur_mise = "rouge"

# le croupier

print("Le courpier lance la roulette, lache la bille")
hasard = random.randint(0, 49)

if hasard % 2 == 0:
    couleur_hasard = 'Noire'
else:
    couleur_hasard = 'Rouge'
print(f"La bille s'est arrreté sur le nombre \n=====> {hasard} \n et la couleur \n=====> {couleur_hasard}")

if nombre_mise == hasard:
    gain = deposer_nombre * 3
    print(f'vous avez gagné vous êtes tombé sur le bon numéro \n le gain total est {gain}')
else:
    if couleur_mise == couleur_hasard:
        gain = deposer_nombre * 1.5
        print(f'vous êtes tombé sur la bonne couleur {couleur_hasard}, vous gagné 50 pourcent de votre mise \n '
              f'votre gain est donc {gain}')
    else:
        gain = 0
        print(f'vous avez perdu, votre nombre est {nombre_mise} et votre couleur est {couleur_mise}')
