import logging
import urllib2
import json

from flask import Flask
from flask_ask import Ask, request, session, question, statement



app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger('flask_ask').setLevel(logging.DEBUG)

catFactApi = "http://catfacts-api.appspot.com/api/facts"

@ask.launch
def launch():
    speech_text = 'Welcome to Cat Facts. Ask me for a cat fact'
    return question(speech_text).reprompt(speech_text).simple_card(title=None, content=speech_text)


@ask.intent('CatFactIntent')
def cat_fact():
    catFact = get_cat_fact()
    return statement(catFact).simple_card(title=None, content=catFact)


@ask.intent('AMAZON.HelpIntent')
def help():
    speech_text = 'You can ask me for a cat fact'
    return question(speech_text).reprompt(speech_text).simple_card(title=None, content=speech_text)


@ask.session_ended
def session_ended():
    return "", 200

def get_cat_fact():
    try:
        response = urllib2.urlopen(catFactApi)
        data = json.load(response)
        catFact = data['facts'][0]
        print(catFact)
        return(catFact)
    except:
        return "I was unable to find a cat fact!"
    


if __name__ == '__main__':
    app.run(debug=True)