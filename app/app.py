import json

def handler(event, context):
    try:
        res = {"status":"200"}
        return json.dumps(res)

    except Exception as e:
        print(e)
        res = {"status":"500"}
        return json.dumps(res)

