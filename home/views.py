
# views.py
import os
from django.shortcuts import render, redirect 
from django.conf import settings
from .models import SimpleUsers
import requests
import datetime
from google.oauth2 import service_account
import google.auth.transport.requests
from django.conf import settings
from django.http import JsonResponse
import json

json_file = settings.JSON_FILE_PATH # the address of key file downloade from Google Firebase

def extract_project_id(key_file_path):
    '''this function get the address of key file and return the projct_id'''
    with open(key_file_path) as f:
        key_data = json.load(f)
        project_id = key_data.get('project_id')
        return project_id


def index_page(request):
    users = SimpleUsers.objects.all()
    context={'users':users,'msg':'','fcmTokens':''}
    #==================
    global json_file
    if request.method == 'POST':
        
        if 'upload_file' in request.POST:
            print(f"action={request.POST}")
            file = request.FILES.get('file')
            if file and file.name.endswith('.json'):
                # Define the directory to save JSON files
                upload_dir = os.path.join(settings.BASE_DIR, 'uploaded_files')
                if not os.path.exists(upload_dir):
                    os.makedirs(upload_dir)
                # Save the uploaded file
                file_path = os.path.join(upload_dir, file.name)
                json_file=file_path
                with open(file_path, 'wb+') as destination:
                    for chunk in file.chunks():
                        destination.write(chunk)
                # Redirect or do further processing
                context['msg']={"upload successfully"}
                return render(request, 'home/index.html',context)
            context['msg']={"Error"}
            return render(request, 'home/index.html',context)
        elif request.method == 'POST'and  request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            # selected_users = request.POST.getlist('users')
            
            checked_values = request.POST.getlist('checkedValues[]')
            if checked_values ==[]:
                
                # print("plz select at least one user to send notif....")
              
                return render(request, 'home/index.html',context)

            else:
                print("Selected fcmToken:", checked_values)
                context['fcmTokens']=checked_values
                # print(f"***********************json file is:{json_file}")
                access_token = generate_access_token(json_file)
                # print(f"************Access Token:{access_token}")
                Message={
                    'status':[]
                }
                
                for token in checked_values:
                    # print(f"*******************{token}")
                    project_id=extract_project_id(json_file)
                    print("Sending data....")
                    res=send_fcm_message(bearer_token=access_token,notification_body='salam',notification_title='hi',project_id=project_id,token=token)
                    if res:
                        Message['status'].append(f"Sucessfully send to user with this token:{token}")

                    else:
                         Message['status'].append(f"Failed to send  with this token:{token}")

                return JsonResponse(Message)
    return render(request, 'home/index.html',context)
        
def generate_access_token(file_path):
    '''this function for generate accesss token '''
    credentials = service_account.Credentials.from_service_account_file(
        file_path,
        
        scopes=["https://www.googleapis.com/auth/firebase.messaging"],
    )

    request = google.auth.transport.requests.Request()
    credentials.refresh(request)

    return credentials.token

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

