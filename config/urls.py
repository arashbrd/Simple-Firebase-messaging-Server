
from django.contrib import admin
from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',include('home.urls')),
    path('api/sendmsg/',include('sendmsg.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/auth-token/',obtain_auth_token,name='generate_auth_token')
]
