from flask import session, render_template, request
import random

def init():
    session['choix_machine'] = random.randint(1,3)
    session['choix_utilisateur'] = ""
    session['reponse'] = ""

def verification():
    if session['choix_machine'] == 1 and session['choix_utilisateur'] == 2:
        session['reponse'] = "Vous avez gagné ! Pierre contre Feuille"
    if session['choix_machine'] == 2 and session['choix_utilisateur'] == 3:
        session['reponse'] = "Vous avez gagné ! Feuille contre Ciseaux"
    if session['choix_machine'] == 3 and session['choix_utilisateur'] == 1:
        session['reponse'] = "Vous avez gagné ! Ciseaux contre Pierre"
    if session['choix_machine'] == session['choix_utilisateur']:
        session['reponse'] = "Il y a égalité."
    if session['choix_machine'] == 3 and session['choix_utilisateur'] == 2:
        session['reponse'] = "Vous avez perdu ! Feuille contre Ciseaux"
    if session['choix_machine'] == 1 and session['choix_utilisateur'] == 3:
        session['reponse'] = "Vous avez perdu ! Pierre contre Ciseaux"
    if session['choix_machine'] == 2 and session['choix_utilisateur'] == 1:
        session['reponse'] = "Vous avez perdu ! Feuille contre Pierre"

def rejouer():
    init()

def main():
    if request.method == 'GET':  # Réinitialisation sur actualisation
        init()
        print('init')
    if request.method == 'POST':
        # Si le bouton pierre est cliqué alors
        if 'pierre' in request.form:
            session['choix_utilisateur'] = 1
            verification()
        if 'feuille' in request.form:
            session['choix_utilisateur'] = 2
            verification()
        if 'ciseaux' in request.form:
            session['choix_utilisateur'] = 3
            verification()
        if 'rejouer' in request.form:
            rejouer()

    return render_template('pierre_feuille_ciseaux.html',
                       choix_machine=session['choix_machine'],
                       choix_utilisateur=session['choix_utilisateur'],
                       reponse=session['reponse']
                       )