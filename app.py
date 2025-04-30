from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


etudiants = []
cours = []
notes = []

@app.route('/')
def home():
    return render_template('index.html', etudiants=etudiants, cours=cours, notes=notes)

@app.route('/etudiants')
def list_etudiants():
    return render_template('etudiants.html', etudiants=etudiants)

@app.route('/cours')
def list_cours():
    return render_template('cours.html', cours=cours)

@app.route('/notes')
def list_notes():
    return render_template('notes.html', notes=notes)

@app.route('/ajouter_etudiant', methods=['GET', 'POST'])
def ajouter_etudiant():
    if request.method == 'POST':
        etudiants.append({
            'nom': request.form['nom'],
            'prenom': request.form['prenom'],
            'age': request.form['age'],
            'classe': request.form['classe']
        })
        return redirect(url_for('list_etudiants'))
    return render_template('ajouter_etudiant.html')

@app.route('/ajouter_cours', methods=['GET', 'POST'])
def ajouter_cours():
    if request.method == 'POST':
        cours.append({
            'nom': request.form['nom'],
            'professeur': request.form['professeur']
        })
        return redirect(url_for('list_cours'))
    return render_template('ajouter_cours.html')

@app.route('/ajouter_note', methods=['GET', 'POST'])
def ajouter_note():
    if request.method == 'POST':
        notes.append({
            'etudiant': request.form['etudiant'],
            'cours': request.form['cours'],
            'note': request.form['note']
        })
        return redirect(url_for('list_notes'))
    return render_template('ajouter_note.html', etudiants=etudiants, cours=cours)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/stats')
def stats():
    return render_template('stats.html',
                           total_etudiants=len(etudiants),
                           total_cours=len(cours),
                           total_notes=len(notes))

if __name__ == '__main__':
    app.run(debug=True)