from flask import Flask, session, render_template, request
import traduction
import calculatrice
import random

app = Flask(__name__)
app.secret_key = 'session_jeux'

@app.route('/kill_session', methods=['GET', 'POST'])
def kill_session():
    session.pop('session_jeux', None)  # Supprime la session de l'utilisateur
    return render_template('index.html')

@app.route('/traduction', methods=['GET', 'POST'])
def traduction():
    try:
        return traduction_include(app, session, request, random)
    except Exception as e:
        return("Erreur dans /traduction : {e}")

@app.route('/calculatrice', methods=['GET', 'POST'])
def calculatrice():
    try:
        calculatrice_include(app, session)
    except Exception as e:
        return render_template('index.html',
           message_html="{e}",
           erreur_html={e},
           result_html=e,
           num1_html="",
           num2_html=""
           )

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html',
       message_html="",
       erreur_html="",
       result_html="",
       num1_html="",
       num2_html=""
       )

if __name__ == '__main__':
    app.run(debug=True)
