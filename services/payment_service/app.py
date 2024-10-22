# app.py - payment-service
from flask import Flask, request, jsonify
import stripe

app = Flask(__name__)

stripe.api_key = "your_stripe_secret_key"

@app.route('/payment', methods=['POST'])
def process_payment():
    data = request.get_json()
    try:
        charge = stripe.Charge.create(
            amount=data['amount'],  # Amount in cents
            currency='usd',
            source=data['stripe_token'],  # Stripe token
            description='Payment for order'
        )
        return jsonify({'status': 'Payment successful', 'charge_id': charge.id})
    except Exception as e:
        return jsonify({'status': 'Payment failed', 'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
