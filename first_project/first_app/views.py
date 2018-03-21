from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    a=5+5
    my_dict={'insert_me':'inserted from view','second_key':a}
    return render(request,'first_app/index.html',my_dict)

def home(request):
    return HttpResponse ("WELCOME TO HOME PAGE")

def img(request):
    return render(request,'first_app/static_image.html')