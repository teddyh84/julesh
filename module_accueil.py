from flask import session, render_template

def main():
    return render_template('index.html',
                           couleur_bouton=session['couleur_bouton']
                           )