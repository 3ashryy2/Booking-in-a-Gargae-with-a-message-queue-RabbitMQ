# Noftification/service/utils.py
import http.client
import json
from google.oauth2 import service_account
import google.auth.transport.requests

def get_access_token():
    credentials = service_account.Credentials.from_service_account_file(
        filename='service/private_key.json',
        scopes=['https://www.googleapis.com/auth/firebase.messaging']
    )
    request = google.auth.transport.requests.Request()
    credentials.refresh(request)
    return credentials.token

def send_fcm_message(token, title, body, data={}):
    access_token = get_access_token()
    url = "fcm.googleapis.com"
    project_id = "cloud-tasks-72920"  # Replace with your actual Firebase project ID
    endpoint = f"/v1/projects/{project_id}/messages:send"

    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json; UTF-8',
    }

    message = {
        "message": {
            "token": token,
            "notification": {
                "title": title,
                "body": body
            },
            "data" : data
            

        }
    }

    conn = http.client.HTTPSConnection(url)
    conn.request("POST", endpoint, body=json.dumps(message), headers=headers)
    response = conn.getresponse()
    data = response.read()
    conn.close()
    return json.loads(data.decode("utf-8"))
