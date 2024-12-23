from flask import session, render_template, request
import random


def minuscule(texte):
    result = texte
    result = result.lower()
    result = result.replace(" ", "")
    print(f"Réponse utilisateur :{result}:")
    return result

def init():
    session['nb_bonnes_reponses'] = 0
    session['nb_reponses'] = 0
    session['mots_anglais'] = ['Apple', 'Ball', 'Cat', 'Dog', 'Fish', 'House', 'Tree', 'Book', 'Chair', 'Table',
                    'Car', 'Bike', 'Sun', 'Moon', 'Water', 'Fire', 'Food', 'Hand', 'Foot',
                    'King', 'Queen', 'Boy', 'Girl', 'Baby', 'Happy (Indice : H...)', 'Sad', 'Love', 'Good', 'Bad',
                    'Day', 'Night', 'Rain', 'Snow', 'Wind', 'Sky', 'Light', 'Dark', 'River', 'Beach',
                    'Bread', 'Milk', 'Tea', 'Sugar', 'Cake', 'Phone', 'Bag', 'Pen', 'Door', 'Window']
    session['traduction_fr'] = ['Pomme', 'Balle', 'Chat', 'Chien', 'Poisson', 'Maison', 'Arbre', 'Livre', 'Chaise', 'Table',
                     'Voiture', 'Vélo', 'Soleil', 'Lune', 'Eau', 'Feu', 'Nourriture', 'Main', 'Pied',
                     'Roi', 'Reine', 'Garçon', 'Fille', 'Bébé', 'Heureux', 'Triste', 'Amour', 'Bon', 'Mauvais',
                     'Jour', 'Nuit', 'Pluie', 'Neige', 'Vent', 'Ciel', 'Lumière', 'Sombre', 'Rivière', 'Plage',
                     'Pain', 'Lait', 'Thé', 'Sucre', 'Gâteau', 'Téléphone', 'Sac', 'Stylo', 'Porte', 'Fenêtre']

def main():
    if request.method == 'GET':  # Réinitialisation sur actualisation
        init()
    message_py = ""
    erreur_py = ""
    score_py = ""

    mot_choisi = random.randint(0, len(session['mots_anglais']) - 1)
    mot_a_afficher = session['mots_anglais'][mot_choisi]
    mot_a_trouver = session['traduction_fr'][mot_choisi]
    question_py = mot_a_afficher # "hello"
    reponse_attendue_py = mot_a_trouver # "bonjour"
    reponse_py = ""
    if request.method == 'POST':
        if 'repondre' in request.form:
            try:
                # Récupérer les valeurs des champs du formulaire
                reponse_py = request.form['reponse']
                reponse_attendue_py = request.form['reponse_attendue']
                if minuscule(reponse_py)==minuscule(reponse_attendue_py):
                    message_py = "Bravo !"
                    session['nb_bonnes_reponses'] = session['nb_bonnes_reponses'] + 1
                else:
                    message_py = "La bonne réponse était : " + reponse_attendue_py
                session['nb_reponses'] += 1
                score_py = "Tu as " + str(session['nb_bonnes_reponses']) + " / " + str(session['nb_reponses'])
                del session['mots_anglais'][mot_choisi]
                del session['traduction_fr'][mot_choisi]
                reponse_attendue_py = mot_a_trouver
                reponse_py = ""
                if session ['nb_reponses'] == 50:
                    if session ['nb_reponses'] == session ['nb_bonnes_reponses']:
                        message_py = "Bravo !!! Tu as 50/50 👏👌 "
                    else:
                        message_py = "Bravo ! Et merci d'avoir participé ❤️"

                print(f"Bonne réponse : {session['nb_bonnes_reponses']}, Total réponses : {session['nb_reponses']}")
                print(f"Nb mots anglais : {len(session['mots_anglais'])}, Nb traduction : {len(session['traduction_fr'])}")

            except:
                erreur_py = "Erreur : veuillez entrer une réponse valide."
    return render_template('traduction.html',
                           message_html=message_py,
                           erreur_html=erreur_py,
                           score_html=score_py,
                           question_html=question_py,
                           reponse_attendue_html=reponse_attendue_py,
                           reponse_html=reponse_py
                           )

