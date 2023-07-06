from flask import Flask, request

from sdk import AliceRequest, AliceResponse
from handler import handle_dialog

app = Flask(__name__)


@app.route('/', methods=['POST'])
def main():
    alice_request = AliceRequest(request.json)
    print('alice_request ', alice_request)
    print('______________________')

    alice_response = AliceResponse(alice_request)

    alice_response = handle_dialog(alice_request, alice_response)

    print('______________________\n_____________________')
    return alice_response.dumps()
