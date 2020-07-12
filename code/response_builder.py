import json 
from random import randint
from template_builder import get_display_template
from apl_builder import get_apl_document
local = 'en-in'
def get_speech(local, current_step):
    with open('master.json', 'r') as data:
        response_labels = json.load(data)
        response_labels = response_labels[local]
    return response_labels[current_step]


def alexa_response(session, current_step, parameters, type="standard", context=None):
    
    response_elements = get_speech(local, current_step)
    
    if type == 'standard':
        
        output = response_elements['SPEECH'][randint(0, len(response_elements['SPEECH'])-1)]
        reprompt = response_elements['REPROMPT'][randint(0, len(response_elements['REPROMPT'])-1)]
        card_title = response_elements['CARD']['TITLE']
        card_content = response_elements['CARD']['CONTENT']        
        card_small_image_url = response_elements['CARD']['SMALL_IMAGE_URL']
        card_large_image_url = response_elements['CARD']['LARGE_IMAGE_URL']
        end_session = response_elements['SESSION_END']
   
        if len(response_elements['REPEAT']) > 0:
            output = response_elements['REPEAT'][randint(0, len(response_elements['REPEAT'])-1)]
        else:
            output = response_elements['SPEECH'][randint(0, len(response_elements['SPEECH'])-1)]

        #build directive
        directives = []
        #add display template
        display_template = get_display_template(response_elements['DISPLAY']['TYPE'],response_elements['DISPLAY']['PAYLOAD'])
        directives.append(display_template)
        #add apl template
        apl_document = get_apl_document(response_elements['APL']['DOCUMENT'], response_elements['APL']['PAYLOAD'])
        directives.append(apl_document)

        for i in range(0,len(parameters)):
            output = output.replace(parameters[i]["source_string"],parameters[i]["target_string"])
            reprompt = reprompt.replace(parameters[i]["source_string"],parameters[i]["target_string"])
            #repeat = repeat.replace(parameters[i]["source_string"],parameters[i]["target_string"])
            card_title = card_title.replace(parameters[i]["source_string"],parameters[i]["target_string"])
            card_content = card_content.replace(parameters[i]["source_string"],parameters[i]["target_string"])

             
        speechlet_response = build_speechlet_response(output, reprompt, card_title, card_content, card_small_image_url, card_large_image_url, directives, end_session)     
        return build_response(session, speechlet_response )
    else:
        pass


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


def build_speechlet_response(output, reprompt, card_title, card_content, card_small_image_url, card_large_image_url, directives, end_session):
    return {
        'outputSpeech': {
            'type': 'SSML',
            'ssml': '<speak>'+output+'</speak>'
        },
        'card': {
            'type': 'Standard',
            'title':  card_title,
            'text':  card_content,
            "image": {
                "smallImageUrl": card_small_image_url,
                "largeImageUrl": card_large_image_url
            } 
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'SSML',
                'ssml': '<speak>'+reprompt+'</speak>'
            }
        },
        'directives': directives,
        'shouldEndSession': end_session
    }

