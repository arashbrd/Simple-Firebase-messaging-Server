
# views.py
import os
from django.shortcuts import render, redirect 
from django.conf import settings
from .models import SimpleUsers
import datetime
from django.http import JsonResponse
from utils.utils import generate_access_token,send_fcm_message,extract_project_id

json_file = settings.JSON_FILE_PATH # the address of key file downloade from Google Firebase


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
                Message={
                    'status':[]
                }
                
                access_token = generate_access_token(json_file)
                if access_token is None:
                    Message['status'].append(f"Failed connecting to server to get Access Token")
                    return JsonResponse(Message)

                # print(f"************Access Token:{access_token}")
                
                project_id=extract_project_id(json_file)
                for token in checked_values:
                    # print(f"*******************{token}")
                    print("Sending data....")
                    res=send_fcm_message(bearer_token=access_token,notification_body='salam',notification_title='hi',project_id=project_id,token=token)
                    if res:
                        Message['status'].append(f"Sucessfully send to user with this token:{token}")

                    else:
                         Message['status'].append(f"Failed to send  with this token:{token}")

                return JsonResponse(Message)
    return render(request, 'home/index.html',context)
 