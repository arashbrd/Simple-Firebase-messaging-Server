
from rest_framework.request import Request
from utils.utils import generate_access_token,extract_project_id,send_fcm_message
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings




class SendMesg(APIView):
    def post(self, request, format=None):
        # Access parameters sent in POST request
        fcmToken = request.data.get('fcmToken', None)
        notification_title = request.data.get('notification_title', None)
        notification_body = request.data.get('notification_body', None)

        if fcmToken is not None and notification_title is not None and notification_body is not None:
            Message={
                    'status':[]
                }
            # Do something with the parameter
            json_file = settings.JSON_FILE_PATH # the address of key file downloade from Google Firebase
            print(f"******json_file******{json_file}")
            access_token = generate_access_token(json_file)
            print(f"******access_token******{access_token}")
            if access_token is None:
                Message['status']=("Connection Time out getting Access Token")

                return Response({"message": f"{Message}"}, status=status.HTTP_504_GATEWAY_TIMEOUT)
                 
            project_id=extract_project_id(json_file)
            print(f"******project_id******{project_id}")
            
            res=send_fcm_message(bearer_token=access_token,notification_body=notification_body,notification_title=notification_title,project_id=project_id,token=fcmToken)
            if res:
                Message['status']=(f"Sucessfully send notif to user with this token:{fcmToken[:20]}")
                return Response({"message": f"{Message}"}, status=status.HTTP_200_OK)

            else:
                    Message['status']=(f"Failed to send  with this token:{fcmToken}")

                    return Response({"message": f"{Message}"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"error": "Parameters 'fcmToken,notification_title,notification_body' is required"}, status=status.HTTP_404_NOT_FOUND)
