# build APL template
import json
#glbal settings 
token = 'app_name'

def get_apl_document(document_name, payload):

    with open(document_name, 'r') as data:
            document = json.load(data)

    return {
        "type": "Alexa.Presentation.APL.RenderDocument",
        "token": token,
        "document": document,
        "datasources": payload
    }


