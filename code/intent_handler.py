from response_builder import alexa_response

def on_intent(intent_request, session):
    intent= intent_request['intent']
    intent_name = intent_request['intent']['name']

    if intent_name == "Amazon.HelpIntent":
        return fn_help(intent, session)
    else:
        return fn_fallback(intent, session)

def fn_help(intent, session):
    if 'attribute' not in session:
        session['attribute'] = {}
    parameters = []
    current_step = "HELP"
    return alexa_response(session, current_step, parameters)

def fn_fallback(intent, session):
    if 'attribute' not in session:
        session['attribute'] = {}
    parameters = []
    current_step = "FALLBACK"
    return alexa_response(session, current_step, parameters)