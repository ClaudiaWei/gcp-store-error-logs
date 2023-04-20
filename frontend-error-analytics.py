from flask import Response
from google.cloud import storage
from datetime import datetime
import json

bucket_name = '<bucket_name>'

def records(request):
    body = request.get_json()
    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)

    if request.method == 'OPTIONS':
        headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'POST',
        'Access-Control-Allow-Headers': 'Content-Type, x-api-key',
        'Access-Control-Max-Age': '3600'
        }
        response = 'ok'
        return Response(response=response, status=200, headers=headers)
    errortime = format(body['datetime'])
    appName = format(body['appName'])
    today = datetime.today()
    year = today.year
    month = today.month
    day = today.day
    app = appName

    blob_name = str(year) + '/' + str(month) + '/' + str(day) + '/' + errortime + '-' + app + '.json'
    blob = bucket.blob(blob_name)
    blob.upload_from_string(data=json.dumps(body), content_type='application/json')

    print(
        'Save data to blob {} in bucket {}.'.format(
            blob.name,
            bucket.name,
        )
    )

    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'POST',
        'Access-Control-Allow-Headers': 'Content-Type, x-api-key',
        'Access-Control-Max-Age': '3600'
        }
    response = 'ok'
    return Response(response=response, status=200, headers=headers)
