from django.urls import path
from second_app.views import index,user,form_detail_view,relative

app_name = 'second_app'
urlpatterns=[
    path('index/',index,name='index'),
    path('users/',user,name='user'),
    path('form_details/',form_detail_view,name='form_details'),
    path('relative/',relative,name='relative')
]

