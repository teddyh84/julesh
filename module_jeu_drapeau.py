from flask import session, render_template, request
import random

def init():
    session['nom_drapeau_image'] = ["allemagne", "grece", "autriche", "hongrie", "belgique", "irlande", "bulgarie",
                                    "italie"]
    session['nombre_aleatoire'] = random.randint(0, len(session['nom_drapeau_image']) - 1)
    session['image_drapeau'] = session['nom_drapeau_image'][session['nombre_aleatoire']]
    print('image :' + session['image_drapeau'])
    session['nom_drapeau'] = ["Allemagne", "Grèce", "Autriche", "Hongrie", "Belgique", "Irlande", "Bulgarie",
                              "Italie"]
    session['proposition_1'] = session['nom_drapeau'][random.randint(0,len(session['nom_drapeau']) - 1)]
    session['proposition_2'] = session['nom_drapeau'][random.randint(0, len(session['nom_drapeau']) - 1)]
    session['proposition_3'] = session['nom_drapeau'][random.randint(0, len(session['nom_drapeau']) - 1)]
    session['vrai_choix'] = random.randint(1,3)
    session[f'proposition_{session["vrai_choix"]}'] = session['nom_drapeau'][session['nombre_aleatoire']]
    print('proposition 1,2,3 : ' + session['proposition_1'] + ',' + session['proposition_2'] + ',' + session['proposition_3'])
    session['message'] = ""
    session['afficher_nouveau_drapeau'] = False

def main():
    if request.method == 'GET': # Réinitialisation sur actualisation
        init()

    if request.method == 'POST':
        if 'generer' in request.form:
            init()
        if 'proposition_1' in request.form:
            if session['proposition_1'] == session['nom_drapeau'][session['nombre_aleatoire']]:
                bon_choix()
            else:
                mauvais_choix()
        if 'proposition_2' in request.form:
            if session['proposition_2'] == session['nom_drapeau'][session['nombre_aleatoire']]:
                bon_choix()
            else:
                mauvais_choix()
        if 'proposition_3' in request.form:
            if session['proposition_3'] == session['nom_drapeau'][session['nombre_aleatoire']]:
                bon_choix()
            else:
                mauvais_choix()

    return render_template('jeu_drapeau.html',
                           nombre_aleatoire=session['nombre_aleatoire'],
                           couleur_bouton=session['couleur_bouton'],
                           image_drapeau=session['image_drapeau'],
                           proposition_1=session['proposition_1'],
                           proposition_2=session['proposition_2'],
                           proposition_3=session['proposition_3'],
                           vrai_choix=session['vrai_choix'],
                           message=session['message'],
                           afficher_nouveau_drapeau=session['afficher_nouveau_drapeau']
                           )

def bon_choix():
    session['message'] = "Bravo c'est le bon drapeau 🤩!"
    session['afficher_nouveau_drapeau'] = True

def mauvais_choix():
    session['message'] = "Dommage c'est le mauvais drapeau 😭!"
    session['afficher_nouveau_drapeau'] = True


