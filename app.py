from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Base de données factice pour les utilisateurs (à remplacer par une vraie base de données)
users = {'john': 'password', 'susan': 'password'}

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            # Redirection vers la page de profil en cas de succès de la connexion
            return redirect(url_for('profile', username=username))
        else:
            # Affichage d'un message d'erreur en cas d'échec de la connexion
            return render_template('login.html', error='Nom d\'utilisateur ou mot de passe incorrect')
    return render_template('login.html')

@app.route('/profile/<username>')
def profile(username):
    return f'Bienvenue sur votre page de profil, {username}'

if __name__ == '__main__':
    app.run(debug=True)
