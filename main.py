from twilio.rest import Client
from twilio.twiml.messaging_response import Body, Message, Redirect, MessagingResponse
import threading
from threading import Thread
from time import sleep
from random import randint
# local libraries
import questions, users

account = "ACf6ddb664419f225eb09901d32dbfc5c9"
token = "345335f019dfac112d93292888a4ca5f"
client = Client(account, token)

#message = client.messages.create(to="+447534003420", from_="+441618502075", body="Hello there!")

from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

client = Client(account, token)

# global variables
asked_question = False
question = ""
user = ""

def send_message(message, send_to_num, from_num="+441618502075"):
    """ function to send "message" to "send_to_num" from default num, "from_num" """
    client.api.account.messages.create(
    to = send_to_num,
    from_n = from_num,
    body=message)
    # internal confirmation
    print("Message {} sent to {} from {}",format(message, from_num, send_to_num))

def sms_get_body_define(message):
    """ simple function to determine what was in the body """

    return None

def flashcard_loop():
    while True:
        if randint(0, 15) == 15:
            global question
            global user
            question = questions.get_random_question()
            user = users.get_random_users()
            asked_question = false
            send_message(question, user)
        else:
            sleep(1)

@app.route("/sms", methods=['GET', 'POST'])
def sms_get_body():
    """Respond to incoming calls with a simple text message."""
    # Start our TwiML response
    resp = MessagingResponse()

    body = request.values.get('Body', None)
    from = request.values.get("From", None)

    if asked_question:
        answered = false
        while answered != false:
            if body == question['correctAnswer']:
                send_message("You got it right!", user)
                answered = true
            else:
                send_message("You got that one wrong... Try again!", user)
    
    asked_question = False
    user = ""
    body = ""
    from = ""
    question = ""
    return str(resp)

if __name__ == "__main__":
    Thread(target = flashcard_loop).start()
    Thread(target = app.run(debug=True)).start()
