from flask import Flask, session, render_template, request

def calculatrice():
    message_py = ""
    erreur_py = ""
    num1_py = ""
    num2_py = ""
    result_py = ""

    if request.method == 'POST':
        if 'effacer' in request.form:
            message_py = "Tout a été effacé"
        if 'calculer' in request.form:
            try:
                num1_py = int(request.form['num1'])
                num2_py = int(request.form['num2'])
                result_py = num1_py + num2_py
                message_py = "Le résultat est : "
            except ValueError:
                erreur_py = "Erreur : veuillez entrer des nombres valides."

    return render_template('calculatrice.html',
                           message_html=message_py,
                           erreur_html=erreur_py,
                           result_html=result_py,
                           num1_html=num1_py,
                           num2_html=num2_py
                           )
