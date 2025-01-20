from flask import render_template, request, session

def pour_fichier():
    with open("ressources/avis_utilisateurs.txt", "a") as fichier:
        fichier.write(session['nom_utilisateur_py'] + ";" + session['jeu_joue_py'] + ";" + session['avis_py'] + "\n")

def init():
    session['nom_utilisateur_py'] = ""
    session['jeu_joue_py'] = ""
    session['avis_py'] = ""
    session['remerciment'] = ""
    session['avis_tous_utilisateurs'] = ""
    try:
        with open("ressources/avis_utilisateurs.txt", 'r') as fichier:  # Ouvre le fichier en mode lecture
            session['avis_tous_utilisateurs'] = fichier.read()  # Lit tout le contenu du fichier
            fichier.close()
    except FileNotFoundError:
        print("Erreur : Le fichier est introuvable.")
    except Exception as e:
        print("Erreur lors de la lecture du fichier : {e}")



def main():
    if request.method == 'GET': #Réinitialisation sur actualisation
        init()

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
                            avis_tous_utilisateurs=session['avis_tous_utilisateurs'],
                            couleur_bouton=session['couleur_bouton'],
                           )