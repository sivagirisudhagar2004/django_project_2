from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Datas

# Create your views here.

def home(request):        
    mydata = Datas.objects.all()
    if(mydata != ''):
        return render(request,'home_3.html',{'datas':mydata})
    else:
        return render(request,'home_3.html')

def addData(request):     # 127.0.0.1:8000/addData
    if(request.method == "POST"):
        name = request.POST['name']
        age = request.POST['age']
        address = request.POST['address']
        mail = request.POST['mail']
        contact = request.POST['contact']

        obj = Datas()
        obj.Name = name
        obj.Age = age
        obj.Address = address
        obj.Contact = contact
        obj.Mail = mail
        obj.save()
        mydata = Datas.objects.all()
        return redirect('home')
    return render(request,"home_3.html")    

def updateData(request,id): # 127.0.0.1:8000/updataData
    Mydata = Datas.objects.get(id = id)
    if(request.method == 'POST'):
        name = request.POST['name']
        age = request.POST['age']
        address = request.POST['address']
        mail = request.POST['mail']
        contact = request.POST['contact']

        Mydata.Name = name
        Mydata.Age = age
        Mydata.Address = address
        Mydata.Contact = contact
        Mydata.Mail = mail
        Mydata.save()
        return redirect('home')
    return render(request,"update.html",{'data': Mydata})

def deleteData(request,id):  #127.0.0.1:8000/daleteData/id
    mydata = Datas.objects.get(id = id)  #object(8)
    mydata.delete()
    return redirect("home")