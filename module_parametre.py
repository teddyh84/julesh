from flask import session, render_template, request

def init():
    if 'couleur_bouton' not in session:
        session['couleur_bouton'] = ""

def main():
    if request.method == 'GET':  # Réinitialisation sur actualisation
        init()
    if request.method == 'POST':
        if 'carre_rouge' in request.form:
            session['couleur_bouton'] = "#ff0000"
        if 'carre_bleu' in request.form:
            session['couleur_bouton'] = "#0000ff"
        if 'carre_jaune' in request.form:
            session['couleur_bouton'] = "#ffff00"
        if 'carre_vert' in request.form:
            session['couleur_bouton'] = "#00ff00"
        if 'carre_violet' in request.form:
            session['couleur_bouton'] = "#4a00a3"
        if 'carre_rose' in request.form:
            session['couleur_bouton'] = "#ff00ff"
        if 'carre_orange' in request.form:
            session['couleur_bouton'] = "#ff9e00"
        if 'carre_bleu_ciel' in request.form:
            session['couleur_bouton'] = "#5bd9f5"

    return render_template('parametres.html',
                           couleur_bouton=session['couleur_bouton']
                           )