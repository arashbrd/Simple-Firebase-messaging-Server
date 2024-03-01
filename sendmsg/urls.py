from django.urls import path
from . import views
urlpatterns=[
path('',views.SendMesg.as_view(),name='sendmsg'),

]