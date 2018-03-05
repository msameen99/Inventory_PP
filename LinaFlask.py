from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import StringField, SubmitField, SelectField, RadioField, FileField, FloatField, IntegerField, TextAreaField
from wtforms.validators import Required, Length, InputRequired

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'top secret!'

class NameForm(Form):
    name = StringField('What is your name?', validators=[Required(), Length(1,16)])
    submit = SubmitField('Submit')
    email = StringField('Email', validators=[InputRequired()])
    textarea = TextAreaField("Paragraph: Write as you like")
    radio = RadioField('Radio',default='option2' ,choices=[('option1', 'Option 1 is this'), ('option2', 'Option 2 can be something else')])
    select = SelectField('Select', choices=[(1,11), (2,22), (3,33), (4,44), (5,55)])

@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''

    return render_template('index.html', form=form, name=name)

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html')
	
if __name__ == '__main__':
	app.run(debug=True)

