from flask import Flask, session, render_template, request

def main():
    message_add_py = ""
    message_sous_py = ""
    message_multi_py = ""
    message_divi_py = ""
    erreur_py = ""
    num1_py = ""
    num2_py = ""
    result_add_py = ""
    result_sous_py = ""
    result_multi_py = ""
    result_divi_py = ""
    if request.method == 'POST':
        if 'effacer' in request.form:
            message_add_py = "Tout a été effacé"
        if 'calculer' in request.form:
            try:
                # soustraction / division / multiplication
                num1_py = int(request.form['num1'])
                num2_py = int(request.form['num2'])
                result_sous_py = num1_py - num2_py
                message_sous_py = "La différence est : "
                result_multi_py = num1_py * num2_py
                message_multi_py = "Le produit est : "
                if num1_py and num2_py != 0:
                    result_divi_py = num1_py / num2_py
                    message_divi_py = "Le quotient est : "
                else:
                    erreur_py = "Il ne faut pas mettre de zéro pour une division !"
                result_add_py = num1_py + num2_py
                message_add_py = "La somme est : "
            except ValueError:
                erreur_py = "Erreur : veuillez entrer des nombres valides."
    return render_template('calculatrice.html',
                           erreur_html=erreur_py,
                           num1_html=num1_py,
                           num2_html=num2_py,
                           result_add_html=result_add_py,
                           result_sous_html=result_sous_py,
                           result_multi_html=result_multi_py,
                           result_divi_html=result_divi_py,
                           message_add_html=message_add_py,
                           message_sous_html=message_sous_py,
                            message_multi_html = message_multi_py,
                           message_divi_html=message_divi_py

                           )
