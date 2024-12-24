from flask import session, render_template, request
import random
def init():
    session['ordre_couleur_lock'] = []
    session['ordre_couleur'] = []
    #Compteur de base à 0 obligé de mettre int() pour nombre
    session['compteur'] = int("0")
    session['rouge'] = "#FF0000"
    session['bleu'] = "#0000FF"
    session['vert'] = "#00FF00"
    session['jaune'] = "#FFFF00"
    session['couleur_py'] = ""

def ajouter_couleur():
    session['couleur_py'] = random.randint(1, 4)
    if session['couleur_py'] == 1:
        session['couleur_py'] = "r"
        session['ordre_couleur_lock'].append(session['couleur_py'])
        print(session['ordre_couleur_lock'])
    if session['couleur_py'] == 2:
        session['couleur_py'] = "b"
        session['ordre_couleur_lock'].append(session['couleur_py'])
        print(session['ordre_couleur_lock'])
    if session['couleur_py'] == 3:
        session['couleur_py'] = "v"
        session['ordre_couleur_lock'].append(session['couleur_py'])
        print(session['ordre_couleur_lock'])
    if session['couleur_py'] == 4:
        session['couleur_py'] = "j"
        session['ordre_couleur_lock'].append(session['couleur_py'])
        print(session['ordre_couleur_lock'])
    session['ordre_couleur'] = session['ordre_couleur_lock']
    print("Juste ordre couleur", session['ordre_couleur'])
    print("Juste ordre couleur lock", session['ordre_couleur_lock'])


def jouer():
    #Si toutes les couleurs sont > à compteur :
    if len(session['ordre_couleur']) > int(session['compteur']):
        #On eface tout ce qui est inutile (au cas ou...)
        session['ordre_couleur_lock'] = [element.replace('"', '').replace("'", '').replace("[", "").replace("]", "") for element in session['ordre_couleur_lock']]
        #a_jouer = à un element de toutes les couleurs
        a_jouer = session['ordre_couleur_lock'][session['compteur']]
        #Mettre le carré en blanc
        if a_jouer == "r":
            session['rouge'] = "#FFFFFF"
        if a_jouer == "b":
            session['bleu'] = "#FFFFFF"
        if a_jouer == "j":
            session['jaune'] = "#FFFFFF"
        if a_jouer == "v":
            session['vert'] = "#FFFFFF"
        #Ajouter 1 pour la couleur suivante
        session['compteur'] += 1

def main():
    print("Hello !!!!")
    if request.method == 'GET':   #Réinitialisation sur actualisation
        init()
    if request.method == 'POST':
        if 'lancer' in request.form:
            ajouter_couleur()
            #while len(session['ordre_couleur_lock']) != 6:
            #jouer()

    return render_template('simon_says.html',
                           couleur_html=session['couleur_py'],
                           rouge_html=session['rouge'],
                           bleu_html=session['bleu'],
                           vert_html=session['vert'],
                           jaune_html=session['jaune'],
                           ordre_couleur_lock_html=session['ordre_couleur_lock']
                           )