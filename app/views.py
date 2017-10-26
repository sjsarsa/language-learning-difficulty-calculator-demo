from app import app_data
from app import app
from flask import render_template, request, redirect


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
                           title='Languages, yay!',
                           header='Language learning difficulty calculator 0.1',
                           languages=[l for l in app_data.get_languages() if l not in app_data.get_user_languages()],
                           user_languages=app_data.get_user_languages(),
                           language_difficulties=app_data.get_language_difficulties())


@app.route('/user_languages', methods=['POST'])
def add_language():
    if request.method == 'POST':
        result = request.form['add_user_language']
        app_data.add_user_language(result)
    return redirect('/index')


@app.route('/user_languages/<language>', methods=['POST'])
def remove_language(language):
    if request.method == 'POST':
        app_data.remove_user_language(language)
    return redirect('/index')
