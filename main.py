from flask import Flask, request

from sdk import AliceRequest, AliceResponse
from handler import handle_dialog

app = Flask(__name__)
session_storage = {}


@app.route('/', methods=['POST'])
def main():
    alice_request = AliceRequest(request.json)
    print('alice_request ', alice_request)
    print('______________________')

    alice_response = AliceResponse(alice_request)

    user_id = alice_request.user_id
    print('session_storage.get(user_id) to handle ', session_storage.get(user_id))

    alice_response, session_storage[user_id] = handle_dialog(
        alice_request, alice_response, session_storage.get(user_id)
    )
    print('______________________\n_____________________')
    return alice_response.dumps()


app.run('0.0.0.0', port=5000, debug=True)
