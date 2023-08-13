from typing import Any
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, IntegerField, SelectField
from wtforms.validators import ValidationError, DataRequired, Length

app = Flask(__name__)
app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'

@app.route('/')
def home():
    return render_template('homepage.html')

#### payform route /payment
class PayForm(FlaskForm):
    first_name = StringField('First Name', validators=[
        DataRequired(),
        Length(min=2, max=30)
    ])

    last_name = StringField('Last Name', validators=[
        DataRequired(),
        Length(min=2, max=30)
    ])
    #dob = DateField('%Y-%m','Date of Birth')
    dob = DateField('Date of Birth')
    card_num = IntegerField('Enter 16 digit Card Number',validators=[
        DataRequired(),
        Length(min=16, max=16)
    ])


    cvc_num = IntegerField('Enter 3 digit Security Number')
    fav_num = IntegerField('Favourite Number')
    
    fav_food = SelectField('Favourite Food', choices=[
        ('pizza', 'Pizza'),
        ('spaghetti', 'Spaghetti'),
        ('chilli', 'Chilli')
    ])
    username = StringField('Username')
    submit = SubmitField('Pay Now')

@app.route('/payment', methods=['GET', 'POST'])
def payment():
    message = ""
    form = PayForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            first_name = form.first_name.data
            last_name = form.last_name.data
            # fav_num = form.fav_num.data
            # fav_food = form.fav_food.data

            if len(first_name) == 0 or len(last_name) == 0:
                message = "Please supply both first and last name"
            else:
                message = f'Thank you, {first_name} {last_name}. Payment Accepted'

    return render_template('payment.html', form=form, message=message)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')