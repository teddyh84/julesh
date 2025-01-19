from flask import session, render_template, request
import random

def init():
    session['coucou'] = random.randint(1,100)

def main():
    session['coucou'] = 2
    init()

    return render_template('jeu_drapeau.html',
                           coucou=session['coucou'],
                           couleur_bouton=session['couleur_bouton']
                           )
