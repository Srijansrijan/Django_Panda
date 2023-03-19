from django.shortcuts import render, HttpResponse
from panda_app.models import Mymodel
# Create your views here.
def indexx(request):
    return render(request,'home.html')

def types(request):
    return render(request,'types.html')

def login(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        panda_choice = request.POST.get('choice')
        Mymodel_instance = Mymodel(name=name, email=email, panda_choice = panda_choice )
        Mymodel_instance.save()
    return render(request,'login.html')

def about(reqest):
    return render(request,'about.html')