import json

def handler(event, context):
    try:
        return{
                "isBase64Encoded":False,
                "statusCode":200,
                "headers": {
                    'Content-Type': 'application/json',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'GET',
                'Access-Control-Allow-Origin': '*'
                },
            "body": json.dumps({"status":"succeed!"})
        }

    except Exception as e:
        print(e)
        res = {"status":"500"}
        return json.dumps(res)

