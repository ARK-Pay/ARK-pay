# forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SubmitField

class PaymentForm(FlaskForm):
    name = StringField('Name')
    card_number = StringField('Card Number')
    expiry_date = StringField('Expiry Date (MM/YY)')
    cvv = StringField('CVV')
    amount = FloatField('Amount')
    submit = SubmitField('Pay Now')
