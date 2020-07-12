import json
from response_builder import  alexa_response
from intent_handler import on_intent
def on_launch(intent, session):
    return get_welcome_response(intent, session)

def end_session(intent, session):
    if 'attribute' not in session:
        session['attribute'] = {}
    parameters = []
    current_step = "SESSION_END"
    session['attribute']['current_step'] = current_step
    return alexa_response(session, current_step, parameters)

def get_welcome_response(intent, session):
    if 'attribute' not in session:
        session['attribute'] = {}
    parameters = []
    current_step = "WELCOME"

    user = "human"

    parameters.append({'source_string' : '%USER%', 'target_string' : user})
    
    session['attribute']['current_step'] = current_step
    return alexa_response(session, current_step, parameters)
    

def lambda_handler(event, context):
    
    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return end_session(event['request'], event['session'])