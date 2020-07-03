import json

def lambda_handler(event, context):
    print('Function loaded successfully');
    orderID = event['Order']
    tempStr = 'Order ' + orderID + ': is being delivered...'
    response = {
        'Order': orderID,
        'Message': tempStr
    }
    print('Returning response: ')
    print(response)
    return response
