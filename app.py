from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_secret'

todos = ['Learn Flask', 'Setup venv', 'Build a cool app', 'Deploy App on Hiroku']

class TodoForm(FlaskForm):
    togo = StringField("Todo")
    submit = SubmitField("Add Todo")


@app.route('/', methods=['GET', 'POST'])
def index():  # put application's code here
    if 'todo' in request.form:
        todos.append(request.form['todo'])
    return render_template('index.html', todos=todos, template_form=TodoForm())


if __name__ == '__main__':
    app.run()
