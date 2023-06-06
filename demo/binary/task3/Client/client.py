import requests

while True:
    action = input('Enter an action (get/post/exit): ')
    if action == 'exit':
        break

    if action == 'get':
        response = requests.get('http://server:5000/messages')
        messages = response.json()
        print('Messages received:', messages)

    if action == 'post':
        message = input('Enter a message: ')
        if message == 'exit':
            break
        response = requests.post('http://server:5000/messages', json={'message': message})
        print(response.text)

