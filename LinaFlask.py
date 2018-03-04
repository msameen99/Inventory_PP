from flask import Flask, render_template, url_for, request
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required, Length

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'top secret!'

class NameForm(Form):
    name = StringField('What is your name?', validators=[Required(), Length(1,16)])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''

    SKU = ['EVVN001', 'EVVN070', 'EVVN090', 'EVVN300', 'EVVN600', 'EVFT02', 'EVFT05', 'EVMR01', 'EVMR02', 'EVMR03', 'EVAC001', 'EVAC002', 'EVAC003', 'EVAC004', 'EVAC005']
    Prices = {
        SKU[0]: {'MAP': 110, 'MSRP': 230, 'Cost': 60, 'Amazon Cost': 100},
        SKU[1]: {'MAP': 111, 'MSRP': 231, 'Cost': 61, 'Amazon Cost': 101},
        SKU[2]: {'MAP': 112, 'MSRP': 232, 'Cost': 62, 'Amazon Cost': 102},
        SKU[3]: {'MAP': 113, 'MSRP': 233, 'Cost': 63, 'Amazon Cost': 103},
        SKU[4]: {'MAP': 114, 'MSRP': 234, 'Cost': 64, 'Amazon Cost': 104},
        SKU[5]: {'MAP': 115, 'MSRP': 235, 'Cost': 65, 'Amazon Cost': 105},
        SKU[6]: {'MAP': 116, 'MSRP': 236, 'Cost': 66, 'Amazon Cost': 106},
        SKU[7]: {'MAP': 117, 'MSRP': 237, 'Cost': 67, 'Amazon Cost': 107},
        SKU[8]: {'MAP': 118, 'MSRP': 238, 'Cost': 68, 'Amazon Cost': 108},
        SKU[9]: {'MAP': 119, 'MSRP': 239, 'Cost': 69, 'Amazon Cost': 109},
        SKU[10]: {'MAP': 120, 'MSRP': 240, 'Cost': 70, 'Amazon Cost': 110},
        SKU[11]: {'MAP': 121, 'MSRP': 241, 'Cost': 71, 'Amazon Cost': 111},
        SKU[12]: {'MAP': 122, 'MSRP': 242, 'Cost': 72, 'Amazon Cost': 112},
        SKU[13]: {'MAP': 123, 'MSRP': 243, 'Cost': 73, 'Amazon Cost': 113},
        SKU[14]: {'MAP': 124, 'MSRP': 244, 'Cost': 74, 'Amazon Cost': 114}
    }
    Highlight = {"MinMap": 113, 'MaxMap': 122, 'MinMsrp': 231, 'MaxMsrp': 243, 'MinCost':65, 'MaxCost': 71, 'MinAmzCost': 104, 'MaxAmzCost': 111}


    return render_template('index.html', SKU=SKU, Prices=Prices, Highlight=Highlight,form=form, name=name)

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html')
	
if __name__ == '__main__':
	app.run(debug=True)

