from flask import session, render_template, request
import random

def init():
    session['ordre_couleur_utilisateur'] = []
    session['ordre_couleur'] = []
    #Compteur de base à 0 obligé de mettre int() pour nombre
    session['compteur'] = int("0")
    session['rouge'] = "#FF0000"
    session['bleu'] = "#0000FF"
    session['vert'] = "#00FF00"
    session['jaune'] = "#FFFF00"
    session['couleur_py'] = ""
    session['message_ko_py'] = ""
    session['message_ok_py'] = ""
    session['message_ordre_couleur_py'] = ""
    session['message_ordre_couleur_utilisateur_py'] = ""

def controle_couleur(couleur_bouton):
    print(session['ordre_couleur'][int(session['compteur'])])
    print(couleur_bouton)

    session['ordre_couleur_utilisateur'].append(couleur_bouton)

    session['message_ordre_couleur_py'] = ""
    session['message_ordre_couleur_utilisateur_py'] = session['ordre_couleur_utilisateur']

    # si c'est le bon bouton
    if session['ordre_couleur'][int(session['compteur'])] == couleur_bouton:
        #ajouter_couleur()
        # je décale le compteur pour comparer lors du prochain bouton
        session['compteur'] = int(session['compteur']) + 1

        # si je sais déjà que je suis à la fin de la liste alors tout est bon on peut recommencer en rajoutant une lettre
        if len(session['ordre_couleur']) == int(session['compteur']):
            ajouter_couleur()
            session['compteur'] = int("0")
            session['ordre_couleur_utilisateur'].clear()
    # si c'est le mauvais bouton
    else:
        session['message_ko_py'] = "Perdu !!"
        session['message_ordre_couleur_py'] = session['ordre_couleur']

def ajouter_couleur():
    session['couleur_py'] = random.randint(1, 4)
    if session['couleur_py'] == 1:
        session['couleur_py'] = "r"
        session['ordre_couleur'].append(session['couleur_py'])
        print(session['ordre_couleur'])
    if session['couleur_py'] == 2:
        session['couleur_py'] = "b"
        session['ordre_couleur'].append(session['couleur_py'])
        print(session['ordre_couleur'])
    if session['couleur_py'] == 3:
        session['couleur_py'] = "v"
        session['ordre_couleur'].append(session['couleur_py'])
        print(session['ordre_couleur'])
    if session['couleur_py'] == 4:
        session['couleur_py'] = "j"
        session['ordre_couleur'].append(session['couleur_py'])
        print(session['ordre_couleur'])
    print("Juste ordre couleur", session['ordre_couleur'])
    session['message_ordre_couleur_py']=session['ordre_couleur']
    session['message_ordre_couleur_utilisateur_py']=""

# def jouer():
#     #Si toutes les couleurs sont > à compteur :
#     if len(session['ordre_couleur']) > int(session['compteur']):
#         #On eface tout ce qui est inutile (au cas ou...)
#         session['ordre_couleur_utilisateur'] = [element.replace('"', '').replace("'", '').replace("[", "").replace("]", "") for element in session['ordre_couleur_utilisateur']]
#         #a_jouer = à un element de toutes les couleurs
#         a_jouer = session['ordre_couleur_utilisateur'][session['compteur']]
#         #Mettre le carré en blanc
#         if a_jouer == "r":
#             session['rouge'] = "#FFFFFF"
#         if a_jouer == "b":
#             session['bleu'] = "#FFFFFF"
#         if a_jouer == "j":
#             session['jaune'] = "#FFFFFF"
#         if a_jouer == "v":
#             session['vert'] = "#FFFFFF"
#         #Ajouter 1 pour la couleur suivante
#         session['compteur'] += 1

def main():
    print("Hello !!!!")
    if request.method == 'GET':   #Réinitialisation sur actualisation
        init()
    if request.method == 'POST':
        if 'lancer' in request.form:
            init()
            ajouter_couleur()
            #while len(session['ordre_couleur_utilisateur']) != 6:
            #jouer()
        if 'carre_rouge' in request.form:
            controle_couleur("r")
        if 'carre_bleu' in request.form:
            controle_couleur("b")
        if 'carre_jaune' in request.form:
            controle_couleur("j")
        if 'carre_vert' in request.form:
            controle_couleur("v")

    return render_template('simon_says.html',
                           couleur_html=session['couleur_py'],
                           rouge_html=session['rouge'],
                           bleu_html=session['bleu'],
                           vert_html=session['vert'],
                           jaune_html=session['jaune'],
                           ordre_couleur_utilisateur_html=session['message_ordre_couleur_utilisateur_py'],
                           ordre_couleur_html=session['message_ordre_couleur_py'],
                           message_ok_html=session['message_ok_py'],
                           message_ko_html=session['message_ko_py']
                           )