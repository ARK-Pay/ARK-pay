# app.py
from flask import Flask, render_template, request, redirect, url_for
from models import db, User, Transaction
from forms import PaymentForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///payments.db'
app.config['SECRET_KEY'] = 'your_secret_key'
db.init_app(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    form = PaymentForm()
    if form.validate_on_submit():
        # Here you would process the payment logic.
        # This is where you would communicate with the bank's API.
        # For demonstration purposes, we'll simulate payment processing.
        
        transaction_status = process_payment(form)  # Custom function to handle payment
        
        # Save transaction details in the database
        new_transaction = Transaction(user_id=1, amount=form.amount.data, status=transaction_status)
        db.session.add(new_transaction)
        db.session.commit()
        
        if transaction_status == "success":
            return redirect(url_for('success'))
        else:
            return redirect(url_for('failure'))
    
    return render_template('index.html', form=form)

def process_payment(form):
    # Simulate payment processing logic here.
    # In a real-world scenario, you would integrate with banking APIs.
    return "success" if form.amount.data < 1000 else "failure"  # Example condition

@app.route('/success')
def success():
    return "Payment Successful!"

@app.route('/failure')
def failure():
    return "Payment Failed!"

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables if they don't exist
    app.run(debug=True)
