import json


def respond(err, res=None):
    return{
    "isBase64Encoded":False,
    "statusCode":400 if err else 200,
    "headers": {
        "Content-Type": "application/json",
        "Access-Control-Allow-Headers": "Content-Type",
        'Access-Control-Allow-Methods': "GET,POST,PUT,DELETE",
        'Access-Control-Allow-Origin': '*'
        },
    "body": err.message if err else json.dumps(res)
    }



def handler(event, context):
    if event['httpMethod'] == 'GET':
        try:
            payload = "fuck!!!!!!"
            return respond(None, payload)


        except Exception as e:
            res = {"status":"500"}
            return respond(ValueError("no"))
    else:
        return respond(ValueError("no"))

