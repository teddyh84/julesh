from flask import session, render_template, request

def init():
    session['prix'] = ""
    session['couleur_primaire'] = ""
    session['couleur_secondaire'] = ""
    session['modele'] = ""

def main():
    if request.method == 'GET':
        init()  # Réinitialisation sur actualisation
    elif request.method == 'POST':
        session['modele'] = request.form.get('modele')
        session['couleur_primaire'] = request.form.get('couleur_primaire')
        session['couleur_secondaire'] = request.form.get('couleur_secondaire')
        print("Modèle choisi :", session['modele'])
        print("Couleur primaire :", session['couleur_primaire'])
        print("Couleur secondaire :", session['couleur_secondaire'])
        calcul_prix()

    return render_template('commandes_3d.html',
                           modele=session['modele'],
                           couleur_primaire=session['couleur_primaire'],
                           couleur_secondaire=session['couleur_secondaire'],
                           prix=session['prix'],
                           couleur_bouton=session['couleur_bouton']
                           )

def calcul_prix():
