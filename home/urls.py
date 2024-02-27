from django.urls import path
from . import views
urlpatterns=[
path('',views.index_page,name='home'),
    # path('send_messages/', views.index_page, name='send_messages'),

]