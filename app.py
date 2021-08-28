from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client

from utils import fetch_reply

app = Flask(__name__)


@app.route("/")
def hello():
    return "<h1>Hello, World!</h1>"


@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body')
    phone_num = request.form.get('From')
    reply = fetch_reply(msg, phone_num)

    # Create reply
    resp = MessagingResponse()
    resp.message(reply)

    print(msg)
    print(phone_num)

    return str(resp)


@app.route("/send", methods=['GET'])
def send_msg():
    account_sid = 'AC21ad6b4f62361a23ae96b3cc249c545b'
    auth_token = '46a0a3beb3deabc859dc1b3283cef13a'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body='Hello! Welcome',
        to='whatsapp:+919773610710'
    )

    print(message.sid)


if __name__ == "__main__":
    app.run(debug=True)
