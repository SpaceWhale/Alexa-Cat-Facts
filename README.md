# Alexa-Cat-Facts
This is a simple proof of concept messing around with alexa skills. A cat facts alexa skill

# Requirements
flask_ask
python
Amazon Developer Account

# Setup
1. Download ngrok https://ngrok.com/
2. run catFacts.py
3. run ngrok: ./ngrok http 5000

# Setup amazon developer account
1. https://developer.amazon.com/
2. add skill: https://developer.amazon.com/edw/home.html#/skills/list
3. Leave the "Skill Type" set to "Custom Interaction Model"
4. Enter "Cat Facts" for both the "Name" and "Invocation Name" fields.
5. Copy the IntentSchema & SampleUtterances files into each respective field
6. Make sure the HTTPS radio button is selected for the "Endpoint" field.
7. Enter the HTTPS endpoint from ngrok into the textfield.
8. Don't bother with "Account Linking".
