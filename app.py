from flask import Flask, session, render_template, send_from_directory
import module_traduction
import module_calculatrice
import module_pendu
import module_avis
import module_simon_says
import module_pierre_feuille_ciseaux
import module_parametre
import module_accueil
import module_jeu_rpg
import module_jeu_animaux
import module_jeu_drapeau

app = Flask(__name__)
app.secret_key = 'session_jeux'

@app.route('/ressources/<path:filename>')
def ressources(filename):
    return send_from_directory('ressources', filename)

@app.route('/traduction', methods=['GET', 'POST'])
def traduction():
    return module_traduction.main()


@app.route('/pendu', methods=['GET', 'POST'])
def pendu():
    return module_pendu.main()

@app.route('/calculatrice', methods=['GET', 'POST'])
def calculatrice():
    return module_calculatrice.main()

@app.route('/simon_says', methods=['GET', 'POST'])
def simon_says():
    return module_simon_says.main()

@app.route('/pierre_feuille_ciseaux', methods=['GET', 'POST'])
def pierre_feuille_ciseaux():
    return module_pierre_feuille_ciseaux.main()

@app.route('/jeu_rpg', methods=['GET', 'POST'])
def jeu_rpg():
    return module_jeu_rpg.main()

@app.route('/jeu_animaux', methods=['GET', 'POST'])
def jeu_animaux():
    return module_jeu_animaux.main()

@app.route('/jeu_drapeau', methods=['GET', 'POST'])
def jeu_drapeau():
    return module_jeu_drapeau.main()

@app.route('/avis', methods=['GET', 'POST'])
def avis():
    return module_avis.main()

@app.route('/parametres', methods=['GET', 'POST'])
def parametres():
    return module_parametre.main()

@app.route('/accueil', methods=['GET', 'POST'])
def accueil():
    return module_accueil.main()

# @app.route('/keypress', methods=['POST'])
# def keypress():
#     return module_simon_says.keypress()

@app.route('/accueil', methods=['GET', 'POST'])
def kill_session():
    session.pop('session_jeux', None)  # Supprime la session de l'utilisateur
    return render_template('index.html')



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
