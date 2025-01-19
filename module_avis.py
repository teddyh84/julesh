from flask import render_template, request, session
def pour_fichier():
    with open("ressources/avis_utilisateurs.txt", "a") as fichier:
        fichier.write(session['nom_utilisateur_py'] + ";" + session['jeu_joue_py'] + ";" + session['avis_py'] + "\n")

def main():
    session['nom_utilisateur_py'] = ""
    session['jeu_joue_py'] = ""
    session['avis_py'] = ""
    session['remerciment'] = ""

    print("HOLLA")
    if request.method == 'POST':
        if 'bouton' in request.form:
            session['nom_utilisateur_py'] = request.form['nom']
            print("L'utilisateur s'appelle :", session['nom_utilisateur_py'])
            session['jeu_joue_py'] = request.form['jeu_joue']
            print("L'utilisateur a joué à :", session['jeu_joue_py'])
            session['avis_py'] = request.form['avis']
            print("L'utilisateur c'est dit :", session['avis_py'])
            session['remerciment'] = "Merci d'avoir répondu 👍😘️"
            pour_fichier()
    return render_template('avis.html',
                            remerciment=session['remerciment'],
                            couleur_bouton=session['couleur_bouton'],
                           )