"""from twilio.rest import Client
from twilio.twiml.messaging_response import Body, Message, Redirect, MessagingResponse



account = "ACf6ddb664419f225eb09901d32dbfc5c9"
token = "345335f019dfac112d93292888a4ca5f"
client = Client(account, token)"""

#message = client.messages.create(to="+447534003420", from_="+441618502075", body="Hello there!")

from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/inbound", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Start our TwiML response
    resp = MessagingResponse()

    # Add a message
    resp.message("The Robots are coming! Head for the hills!")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
