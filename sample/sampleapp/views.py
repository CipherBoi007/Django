from django.shortcuts import render
from .models import Data

# Create your views here.

def home(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        obj = Data()
        obj.Name = name
        obj.Email = email
        obj.Message = message
        obj.save()

    return render(request,'home.html')

def response(request):
    data = Data.objects.all()
    return render(request, 'response.html',{'data' : data})
