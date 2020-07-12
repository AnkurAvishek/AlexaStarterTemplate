def get_slot_value(intent,slotname):
    slotvalue = {}
    try:
        if "slots" in intent:
            if "resolutions" in intent['slots'][slotname]:                
                if "values" in intent['slots'][slotname]['resolutions']['resolutionsPerAuthority'][0] and intent['slots'][slotname]['resolutions']['resolutionsPerAuthority'][0]['status']['code'] == "ER_SUCCESS_MATCH":
                    slotvalue["synonymId"] = intent['slots'][slotname]['resolutions']['resolutionsPerAuthority'][0]['values'][0]['value']['id']
                    slotvalue["synonymName"] = intent['slots'][slotname]['resolutions']['resolutionsPerAuthority'][0]['values'][0]['value']['name']
                    slotvalue["value"] = intent['slots'][slotname]['value']
                elif intent['slots'][slotname]['resolutions']['resolutionsPerAuthority'][0]['status']['code'] == "ER_SUCCESS_NO_MATCH":
                    slotvalue["synonymId"] = "undefined"
                    slotvalue["synonymName"] = "undefined"
                    slotvalue["value"] = intent['slots'][slotname]['value']
                else:
                    slotvalue["synonymId"] = "undefined"
                    slotvalue["synonymName"] = "undefined"
                    slotvalue["value"] = "undefined"
            elif "value" in intent['slots'][slotname]:
                    debug_print("found value")
                    slotvalue["synonymId"] = "undefined"
                    slotvalue["synonymName"] = "undefined"
                    if intent['slots'][slotname]["value"] != '?':
                    	slotvalue["value"] = intent['slots'][slotname]['value'].lower()		
                    else:		
                    	slotvalue["value"] = "undefined"
            else:
                slotvalue["synonymId"] = "undefined"
                slotvalue["synonymName"] = "undefined"
                slotvalue["value"] = "undefined"
        else:
            slotvalue["synonymId"] = "undefined"
            slotvalue["synonymName"] = "undefined"
            slotvalue["value"] = "undefined"        
    except:
        slotvalue["synonymId"] = "undefined"
        slotvalue["synonymName"] = "undefined"
        slotvalue["value"] = "undefined"        
    return slotvalue

def get_previous_state(intent,session):
    previous_state = {}
    try :
        if "attributes" in session:
            if "current_step" in session['attributes']:
                previous_state['previous_step'] = session['attributes']['current_step']
            else:
                previous_state['previous_step'] = None
        else:
            previous_state['previous_step'] = None
    except:
        previous_state['previous_step'] = None
    return previous_state
