# build display template
#glbal settings 
token = 'app_name'
valid_template_type = []
backbutton = "HIDDEN"
list_template = ['ListTemplate1', 'ListTemplate2']

def get_display_template(temp_type, payload):
    return build_template_response(build_display_template(temp_type, payload))

def build_template_response(template):
    return {
            "type": "Display.RenderTemplate",
            "template": template
    }

def build_display_template(temp_type, payload):
    template = {}
    template['token'] = token
    template['type'] = temp_type
    
    template['backgroundImage'] = {
        "sources": [
            {
              "url":  payload['BACKGROUND_IMAGE']
            }
        ],
        }
    template['backButton'] = backbutton

    if temp_type != "BodyTemplate6":
        template['title'] = payload['TITLE']
    if temp_type != "BodyTemplate1" and temp_type not in list_template:
        template['image'] = {
        "sources": [
                {
                "url":  payload['FOREGROUND_IMAGE']
                }
            ],
        }        

    if temp_type != "BodyTemplate7" and temp_type not in list_template:
        template['textContent'] = {}
        template['textContent']['primaryText'] = {
            "type": "RichText",
            "text": payload['PRIMARY_TEXT']
            }
        template['textContent']['secondaryText'] = {
            "type": "RichText",
            "text": payload['SECONDARY_TEXT']
        }
        template['textContent']['tertiaryText'] = {
            "type": "RichText",
            "text": payload['TERTIARY_TEXT']
        }       
    if temp_type in list_template:
        template['listItems'] = []
        for ITEM in payload['ITEM_LIST']:            
            item = {
                    "token": ITEM['TOKEN'],
                    "image": ITEM['IMAGE'],
                    "textContent": {
                        "primaryText": {
                            "type": "RichText",
                            "text": ITEM['TEXT']
                        }
                    }
                }
            template['listItems'].append(item)
    return template


#-------------------------------------- Examples from documentaton -----------
#sample mixed payload (body+list)
#"DISPLAY":{
#    "TYPE" : "BodyTemplate2",
#    "PAYLOAD":{
#        "BACKGROUND_IMAGE" : "https://d2o906d8ln7ui1.cloudfront.net/images/BT7_Background.png",
#        "TITLE" : "welcome",
#        "FOREGROUND_IMAGE" : "https://d2o906d8ln7ui1.cloudfront.net/images/BT7_Background.png",
#        "PRIMARY_TEXT" : "Welcome %USER% to the skill.",
#        "SECONDARY_TEXT" : "to alexa",
#        "TIRTIARY_TEXT" : "skill",
#        "ITEM_LIST":[
#            {
#                "IMAGE": "https://d2o906d8ln7ui1.cloudfront.net/images/BT7_Background.png",
#                "TEXT": "Sample1"
#            },
#            {
#                "IMAGE": "https://d2o906d8ln7ui1.cloudfront.net/images/BT7_Background.png",
#                "TEXT": "Sample1"
#            }
#        ]
#    }                
#},
#
#{
#  "type":"BodyTemplate1",
#  "token": "string",
#  "backButton": "VISIBLE"(default) | "HIDDEN",
#  "backgroundImage": Image,
#  "title": "string",
#  "textContent": TextContent
#}
#
#{
#  "type": "BodyTemplate2",
#  "token": "string",
#  "backButton": "VISIBLE"(default) | "HIDDEN",
#  "backgroundImage": "Image",
#  "title": "string",
#  "image": Image,
#  "textContent": TextContent
#}
#
#  "type": "BodyTemplate3",
#  "token": "string",
#  "backButton": "VISIBLE"(default) | "HIDDEN",
#  "backgroundImage": "Image",
#  "title": "string",
#  "image": Image,
#  "textContent": TextContent
#}

#{
#  "type": "BodyTemplate6",
#  "token": "string",
#  "backButton": "VISIBLE"(default) | "HIDDEN",
#  "backgroundImage": Image,
#  "image": "Image",
#  "textContent": TextContent
#}
#
#{
#  "type": "BodyTemplate7",
#  "token": "SampleTemplate_3476",
#  "backButton": "VISIBLE",
#  "title": "Sample BodyTemplate7",
#  "backgroundImage": {
#    "contentDescription": "Textured grey background",
#    "sources": [
#      {
#        "url": "https://www.example.com/background-image1.png"
#      }
#    ]
#  },
#  "image": {
#    "contentDescription": "Mount St. Helens landscape",
#    "sources": [
#      {
#        "url": "https://example.com/resources/card-images/mount-saint-helen-small.png"
#      }
#    ]
#  }
#}

#{
#  "type": "ListTemplate1",
#  "token": "string",
#  "backButton": "VISIBLE"(default) | "HIDDEN",
#  "backgroundImage": "Image",
#  "title": "string",
#  "listItems": [
#    {
#      "token": "string",
#      "image": Image,
#      "textContent": TextContent
#    },
#    ...
#    ...
#    {
#      "token": "string",
#      "image": Image,
#      "textContent": TextContent
#    }
#  ]
#}

#{
#  "type": "ListTemplate2",
#  "token": "string",
#  "backButton": "VISIBLE"(default) | "HIDDEN",
#  "backgroundImage": "Image",
#  "title": "string",
#  "listItems": [
#    {
#      "token": "string",
#      "image": Image,
#      "textContent": TextContent
#    },
#    ...
#    ...
#    {
#      "token": "string",
#      "image": Image,
#      "textContent": TextContent
#    },
#  ]
#}



#--------------------------------For Developer's Reference ----------------------------------#
#type	Name of the template	

# BodyTemplate1
#BodyTemplate2
#BodyTemplate3
#BodyTemplate6
#BodyTemplate7
#ListTemplate1
#ListTemplate2

#token	Used to track selectable elements in the skill service code. The value can be any user-defined string.	Dog-List-2
#1212323312

#backButton	Used to place the back button on a display template.	
# HIDDEN | VISIBLE

#backgroundImage	Used to include a background image on a display template.	
#{
#    "contentDescription": "string",
#    "sources": [
#      {
#        "url": "string",
#        "size": "string",
#        "widthPixels": integer,
#        "heightPixels": integer
#     },
#      {
#        "url": "string",
#        "size": "string",
#        "widthPixels": integer,
#        "heightPixels": integer
#      },
#      {...}
#    ]
#}

# title	Used for title for a display template. The value can be any user-defined string.	"Doggie Carousel", "Cake Recipes Galore"

# textContent	Contains primaryText, secondaryText, and tertiaryText.	

#{
#   "primaryText": ...,
#    "secondaryText": ...,
#    "tertiaryText": ...
#}"""

#primaryText	Contains type (which is PlainText or RichText) and text (which is a string). Limit of 8000 characters.	

#{
#    "text": "string",
#    "type": "PlainText" | "RichText"
#}

#secondaryText	Contains type (which is PlainText or RichText) and text (which is a string). Limit of 8000 characters.	

#{
#    "text": "string",
#    "type": "PlainText" | "RichText"
#}

#tertiaryText	Contains type (which is PlainText or RichText) and text (which is a string). Limit of 8000 characters.	

#{
#    "text": "string",
#    "type": "PlainText" | "RichText"
#}

#image	References and describes the image. Multiple sources for the image can be provided. The same format is used for both `backgroundImage` and `image`.	

#{
#    "contentDescription": "string",
#    "sources": [
#      {
#        "url": "string",
#        "size": "string",
#        "widthPixels": integer,
#        "heightPixels": integer
#     },
#      {
#        "url": "string",
#        "size": "string",
#        "widthPixels": integer,
#        "heightPixels": integer
#      },
#      {...}
#    ]
#}

#listItems	Contains the text and images of the list items.	

#  [
#    {
#      "token": "string",
#      "image": "Image",
#      "textContent": "TextContent"
#    },
#    ...
#    ...
#    {
#      "token": "string",
#      "image": "Image",
#      "textContent": "TextContent"
#    }
#  ]