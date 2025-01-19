from flask import render_template, request, session

def init():
    session['afficher_bouton'] = "Lancer la partie"
    session['test'] = 'type="submit" id="lancer_partie_b" name="lancer_partie_b">Bonjour'
    session['lien_image'] = ""
    session['afficher_visuel_bouton'] = True
    session['afficher_visuel_bouton_nourrir'] = False
    session['afficher_visuel_bouton_caresser'] = False

def main():
    if request.method == 'GET':  # Réinitialisation sur actualisation
        init()
    if request.method == 'POST':
        # Si le bouton est cliqué alors
        if 'lancer_partie' in request.form:
            session['afficher_visuel_bouton'] = False
            session['afficher_visuel_bouton_nourrir'] = True
            session['afficher_visuel_bouton_caresser'] = True
            session['afficher_bouton'] = "Bonjour"
            session['lien_image'] = "ressources/image_chat_a.png"

    return render_template('jeu_animaux.html',
                                couleur_bouton=session['couleur_bouton'],
                                afficher_bouton=session['afficher_bouton'],
                                test=session['test'],
                                lien_image=session['lien_image'],
                                afficher_visuel_bouton=session['afficher_visuel_bouton'],
                                afficher_visuel_bouton_nourrir=session['afficher_visuel_bouton_nourrir'],
                                afficher_visuel_bouton_caresser=session['afficher_visuel_bouton_caresser']
                           )