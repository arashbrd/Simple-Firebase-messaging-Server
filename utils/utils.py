       
import google.auth.transport.requests
from google.auth.exceptions import TransportError 
from google.oauth2 import service_account
import requests
import json
from requests.exceptions import Timeout




def extract_project_id(key_file_path):
    '''this function get the address of key file and return the projct_id'''
    with open(key_file_path) as f:
        key_data = json.load(f)
        project_id = key_data.get('project_id')
        return project_id


def generate_access_token(file_path):
    try:
        '''this function for generate accesss token '''
        credentials = service_account.Credentials.from_service_account_file(
            file_path,
            
            scopes=["https://www.googleapis.com/auth/firebase.messaging"],
        )

        request = google.auth.transport.requests.Request()
        credentials.refresh(request)

        return credentials.token
    except Timeout:
    
        return None
    except TransportError:
        return None

def send_fcm_message(token, notification_body, notification_title, project_id,bearer_token):
    '''function that send notification'''
    
    
    url = f"https://fcm.googleapis.com/v1/projects/{project_id}/messages:send"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {bearer_token}"
    }
    payload = {
        "message": {
            "token": token,# token comes from user input in admin panel
            "notification": {
                "body": notification_body,
                "title": notification_title
            }
        }
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code == 200:
        print("FCM message sent successfully.")
        return True
    else:
        print(f"Failed to send FCM message. Status code: {response.status_code}")
        print(response.text)
        return False

