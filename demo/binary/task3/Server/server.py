from flask import Flask, request, jsonify

app = Flask(__name__)
messages = {}

@app.route('/messages', methods=['GET', 'POST'])
def handle_messages():
    user_id = request.remote_addr

    if request.method == 'GET':
        user_messages = messages.get(user_id, [])
        return jsonify(user_messages)

    if request.method == 'POST':
        message = request.json.get('message')

        if user_id not in messages:
            messages[user_id] = []

        messages[user_id].append(message)
        return 'Message received: {}'.format(message)

if __name__ == '__main__':
    app.run(host='0.0.0.0')

