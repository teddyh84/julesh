from flask import session, render_template, request
import random

def init():
    session['monstre_a_apparaitre'] = random.randint(1,2)
    session['adversaire_lock'] = []
    session['zombie'] = [100,10,25,15]
    session['squellette'] = [150, 15,20,10]
    session['joueur_lock'] = [100,15,25,10]
    print(session['monstre_a_apparaitre'])
    session['a_qui_de_jouer'] = "joueur"
    session['coucou_py'] = ""
    session['joueur'] = session['joueur_lock']
    session['adversaire'] = []
    session['info'] = ""
    session['defense_robot'] = 0
    session['defense_joueur'] = 0

def main():
    if request.method == 'GET': # Réinitialisation sur actualisation
        init()
        choisir_adversaire()
    if request.method == 'POST':
        if session['a_qui_de_jouer'] == "joueur":
            if 'attaquer' in request.form:
                attaquer()
            #if 'defense' in request.form:
                #defense()
            if 'soins' in request.form:
                soins()
        if session['a_qui_de_jouer'] == "robot":
            choix_action_adversaire()
    return render_template('jeu_rpg.html',
                           image_monstre=session['monstre_a_apparaitre'],
                           vie_joueur=session['joueur'][0],
                           vie_monstre=session['adversaire'][0],
                           couleur_bouton=session['couleur_bouton'],
                           coucou_html=session['coucou_py'],
                           info=session['info']
                           )
def choisir_adversaire():
    if session['monstre_a_apparaitre'] == 1:
        session['monstre_a_apparaitre'] = "squellette"
        session['adversaire_lock'] = session['squellette']
        session['adversaire'] = session['adversaire_lock']
        print("Squellette")
    elif session['monstre_a_apparaitre'] == 2:
        session['monstre_a_apparaitre'] = "zombie"
        session['adversaire_lock'] = session['zombie']
        session['adversaire'] = session['adversaire_lock']
        print("Zombie")

def attaquer():
    print("Joueur = Attaque")
    if session['defense_robot'] != 0:
        adversaire = session['adversaire']
        adversaire[0] -= session['joueur'][1] - session['defense_robot']
        session['adversaire'] = adversaire
        session['a_qui_de_jouer'] = "robot"
    else:
        adversaire = session['adversaire']
        adversaire[0] -= session['joueur'][1]
        session['adversaire'] = adversaire
        session['a_qui_de_jouer'] = "robot"

#def defense():


def soins():
    print("Joueur = Soin")
    if session['joueur'][0] + session['joueur'][2] > session['joueur_lock'][0]:
        joueur = session['joueur']
        joueur[0] = 100
        session['joueur'] = joueur
        session['a_qui_de_jouer'] = "robot"
    else:
        joueur = session['joueur']
        joueur[0] += joueur[2]
        session['joueur'] = joueur
        session['a_qui_de_jouer'] = "robot"

def choix_action_adversaire():
    if session['adversaire'][0] < session['adversaire_lock'][0] * 0.3:  # Si ses PV sont inférieurs à 30%
        choix = random.choices(
            ["soin", "attaque", "defense"],
            weights=[0.6, 0.3, 0.1]  # Plus de chances de se soigner
        )[0]
    elif session['joueur'][0] < 20:  # Si le joueur est presque KO
        choix = random.choices(
            ["attaque", "defense", "soin"],
            weights=[0.7, 0.2, 0.1]  # Priorité à l'attaque
        )[0]
    else:
        choix = random.choices(
            ["attaque", "defense", "soin"],
            weights=[0.5, 0.3, 0.2]  # Équilibre entre défense et attaque
        )[0]
    if choix == "attaque":
        attaquer_joueur()
        session['info'] = "Robot = Attaque"
    if choix == "defense":
        defense_robot()
        session['info'] = "Robot = Défense"
    if choix == "soin":
        soin_robot()
        session['info'] = "Robot = Soin"

def attaquer_joueur():
    joueur = session['joueur']
    joueur[0] -= session['adversaire'][1]
    session['joueur'] = joueur
    session['a_qui_de_jouer'] = "joueur"

def soin_robot():
    if session['adversaire'][0] + session['adversaire'][2] > session['adversaire_lock'][0]:
        session['adversaire'][0] = session['adversaire_lock'][0]
    else:
        adversaire = session['adversaire']
        adversaire[0] += 25
        session['adversaire'] = adversaire
        session['a_qui_de_jouer'] = "joueur"

def defense_robot():
    adversaire = session['adversaire']
    session['defense_robot'] = adversaire[3]
    session['adversaire'] = adversaire
    session['a_qui_de_jouer'] = "joueur"
