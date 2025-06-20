import pyfiglet
from flask import Flask, request, render_template_string
import logging

# Disable Flask logging to keep console clean
logging.getLogger('werkzeug').setLevel(logging.ERROR)

# Create Flask app
app = Flask(__name__)

# Banner
def print_banner():
    banner = pyfiglet.figlet_format("SMS Phishing Simulator")
    print(banner)
    print("Coded by Pakistani Ethical Hacker Mr. Sabaz Ali Khan")
    print("="*50)
    print("WARNING: This is an educational tool. Do not use for illegal activities.")
    print("="*50)

# HTML template for fake login page
LOGIN_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Secure Login</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f0f0f0;
            margin: 0;
        }
        .login-container {
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
            width: 300px;
            text-align: center;
        }
        input[type="text"], input[type="password"] {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        input[type="submit"] {
            width: 100%;
            padding: 10px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        input[type="submit"]:hover {
            background-color: #45a049;
        }
        .warning {
            color: red;
            font-size: 12px;
            margin-top: 10px;
        }
    </style>
</head>
<body>
    <div class="login-container">
        <h2>Secure Login</h2>
        <p>Please enter your credentials to proceed</p>
        <form method="POST" action="/login">
            <input type="text" name="username" placeholder="Username" required><br>
            <input type="password" name="password" placeholder="Password" required><br>
            <input type="submit" value="Login">
        </form>
        <p class="warning">This is a simulated phishing page for educational purposes.</p>
    </div>
</body>
</html>
"""

# Route for the phishing page
@app.route('/')
def index():
    return render_template_string(LOGIN_PAGE)

# Route to handle form submission
@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    print(f"[CAPTURED] Username: {username}, Password: {password}")
    return "Credentials received! This is a simulation. In a real attack, this data would be sent to the attacker."

# Main function
if __name__ == "__main__":
    print_banner()
    print("Starting SMS Phishing Simulator...")
    print("Open your browser and navigate to http://localhost:5000")
    print("Simulated SMS: 'Your account needs verification. Click here to login: http://localhost:5000'")
    app.run(debug=False)