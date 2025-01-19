from flask import session, render_template, request
import random
# import msvcrt
# import pynput

def init():
    session['mots_pendu'] = ['pomme', 'table', 'livre', 'plage', 'sable', 'neige', 'tissu','nuage', 'fruit', 'rayon',
                             'porte', 'fleur', 'glace', 'pluie','arbre', 'plume', 'jaune', 'tapis', 'perle', 'lampe',
                             'coque','balle', 'terre', 'vague', 'chaud', 'noire', 'flanc', 'pente', 'soupe', 'douce',
                             'wagon', 'balai', 'lapin']
    session['mot_mystere_py'] = random.choice(session['mots_pendu'])
    session['mot_utilisateur_py'] = '_____'
    session['nombre_lettres_loupées'] = '10'
    session['lettres_deja_utilisees'] = ''
    session['message_ko_py'] = ""
    session['message_ok_py'] = ""
    session['message_attention_py'] = ""
    print(session['mot_mystere_py'])
def main():
    reponse_utilisateur_py = ""
    if request.method == 'GET':  # Réinitialisation sur actualisation
        init()
        print(f"init")
    if request.method == 'POST':
        # Si le bouton valider est cliqué alors
        if 'valider' in request.form:
            trouve = False
            reponse_utilisateur_py = request.form['reponse_utilisateur'] # reponse_utilisateur_py = input dans html
            print(f"valider")
            print(session['mot_utilisateur_py'])
            # Pour le compteur, de base est à false
            print(session['lettres_deja_utilisees'].find(reponse_utilisateur_py))
        # Si la lettre n'a jamais été demandée alors
            if session['lettres_deja_utilisees'].find(reponse_utilisateur_py) == -1:
                session['lettres_deja_utilisees'] = session['lettres_deja_utilisees'] + reponse_utilisateur_py + ","
                # Mettre la nouvelle lettre dans la session "lettres déjà demandées"
            print(session['lettres_deja_utilisees'])
            # Regarder pour chaques lettres du mot mystère si il contient lettre utilisateur
            for position, lettre in enumerate (session['mot_mystere_py']):
                if lettre == reponse_utilisateur_py.lower():
                    print(session['mot_utilisateur_py'])
                    # Remplacer le mot utilisateur par la lettre (obligé de passer par une liste)
                    mot_liste = list(session['mot_utilisateur_py'])
                    mot_liste[position] = reponse_utilisateur_py
                    session['mot_utilisateur_py']=''.join(mot_liste)
                    # Mettre trouve à vrai
                    trouve = True
                    print("coucou")
        # Si trouve n'est pas vrai alors
            if not trouve:
                nb_lettre_loupees = int(session['nombre_lettres_loupées'])
                # Ajouter 1 aux lettres loupées
                nb_lettre_loupees -= 1
                session['nombre_lettres_loupées'] = str(nb_lettre_loupees)
    if 'rejouer' in request.form:
        init()
        print("hello je rejoue !")
    if int(session['nombre_lettres_loupées']) <= 0:
        session['message_ko_py'] = "Tu as perdu !! 😫😭😱"
    if session['mot_mystere_py'] == session['mot_utilisateur_py']:
        if int(session['nombre_lettres_loupées']) > 0:
            session['message_ok_py'] = "Tu es trop fort(e) !! 👌👏😍"
    return render_template('pendu.html',
                        mot_mystere_html=session['mot_mystere_py'],
                        mot_utilisateur_html=session['mot_utilisateur_py'],
                        reponse_utilisateur_html=reponse_utilisateur_py,
                        compteur_html=session['nombre_lettres_loupées'],
                        lettres_deja_utilisees_html=session['lettres_deja_utilisees'][:-1],
                        message_ok_html=session['message_ok_py'],
                        message_ko_html=session['message_ko_py'],
                        message_attention_html=session['message_attention_py'],
                        image_number_html=str(11-int(session['nombre_lettres_loupées'])),
                        couleur_bouton=session['couleur_bouton']
                        )


