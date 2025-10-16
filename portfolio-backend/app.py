from dotenv import load_dotenv
load_dotenv()
from flask import Flask, request, jsonify
from flask_mail import Mail, Message
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# ----------------------
# Flask-Mail Configuration
# ----------------------
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME') or 'your_email@gmail.com'
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD') or 'your_app_password'
app.config['MAIL_DEFAULT_SENDER'] = app.config['MAIL_USERNAME']

mail = Mail(app)

# ----------------------
# Routes
# ----------------------

@app.route('/contact', methods=['POST'])
def contact():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')

    if not (name and email and message):
        return jsonify({'status': 'error', 'message': 'All fields are required.'}), 400

    try:
        msg = Message(
            subject=f"📩 New Contact Message from {name}",
            recipients=['your_email@gmail.com'],  # your destination email
            body=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
        )
        mail.send(msg)
        return jsonify({'status': 'success', 'message': 'Message sent successfully!'})
    except Exception as e:
        print("Error sending email:", e)
        return jsonify({'status': 'error', 'message': 'Failed to send message. Please try again later.'}), 500

# ----------------------
# Run the app
# ----------------------
if __name__ == '__main__':
    app.run(debug=True)
