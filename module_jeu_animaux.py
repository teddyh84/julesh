from flask import render_template, request, session
import random

def init():
    session['test'] = 'type="submit" id="lancer_partie_b" name="lancer_partie_b">Bonjour'
    session['lien_image'] = ""
    session['nombre_nourriture'] = 15
    session['amour'] = 0
    session['faim'] = 5
    session['afficher_amour_nourriture'] = False
    session['afficher_visuel_bouton_lancer'] = True
    session['afficher_visuel_bouton_nourrir'] = False
    session['afficher_visuel_bouton_caresser'] = False
    session['afficher_erreur'] = False

def main():
    if request.method == 'GET':  # Réinitialisation sur actualisation
        init()
    if request.method == 'POST':
        # Si le bouton est cliqué alors
        if 'lancer_partie' in request.form:
            session['afficher_visuel_bouton_lancer'] = False
            session['afficher_visuel_bouton_nourrir'] = True
            session['afficher_visuel_bouton_caresser'] = True
            session['afficher_amour_nourriture'] = True
            session['lien_image'] = "ressources/image_chat_a.png"
        if 'maison' in request.form:
            session['afficher_visuel_bouton_lancer'] = True
            session['afficher_visuel_bouton_nourrir'] = False
            session['afficher_visuel_bouton_caresser'] = False
            session['afficher_amour_nourriture'] = False
            session['lien_image'] = ""
        if 'nourrir' in request.form:
            nourrir()

    return render_template('jeu_animaux.html',
                                couleur_bouton=session['couleur_bouton'],
                                test=session['test'],
                                lien_image=session['lien_image'],
                                afficher_visuel_bouton_lancer=session['afficher_visuel_bouton_lancer'],
                                afficher_visuel_bouton_nourrir=session['afficher_visuel_bouton_nourrir'],
                                afficher_visuel_bouton_caresser=session['afficher_visuel_bouton_caresser'],
                                nombre_nourriture=session['nombre_nourriture'],
                                afficher_erreur=session['afficher_erreur'],
                                afficher_amour_nourriture=session['afficher_amour_nourriture'],
                                amour=session['amour'],
                                faim=session['faim']
                           )

def nourrir():
    if session['nombre_nourriture'] == 0:
        session['nombre_nourriture'] = "Tu n'as plus de nourriture !"
    elif session['nombre_nourriture'] == "Tu n'as plus de nourriture !":
        session['nombre_nourriture'] = 0
    else:
        session['nombre_nourriture'] -= 1
        session['faim'] = random.randint

