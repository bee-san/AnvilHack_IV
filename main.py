from twilio.rest import Client
from twilio.twiml.messaging_response import Body, Message, Redirect, MessagingResponse



account = "ACf6ddb664419f225eb09901d32dbfc5c9"
token = "345335f019dfac112d93292888a4ca5f"
client = Client(account, token)

#message = client.messages.create(to="+447534003420", from_="+441618502075", body="Hello there!")

from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

client = Client(account, token)

def send_message(message, send_to_num, from_num="+441618502075"):
    """ function to send "message" to "send_to_num" from default num, "from_num" """
    client.api.account.messages.create(
    to = send_to_num,
    from_ = from_num,
    body=message)
    # internal confirmation
    print("Message {} sent to {} from {}",format(message, from_num, send_to_num))

def sms_get_body_define(message)
    """ simple function to determine what was in the body """

    return None

@app.route("/sms", methods=['GET', 'POST'])
def sms_get_body():
    """Respond to incoming calls with a simple text message."""
    # Start our TwiML response
    resp = MessagingResponse()

    body = request.values.get('Body', None)
    from = request.values.get("From", None)
    resp.message("Hello, you said {}".format(body))


    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
