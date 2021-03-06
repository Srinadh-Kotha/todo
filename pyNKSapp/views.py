from django.db.models.fields import NullBooleanField
from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from pyNKSapp.models import signupdetails,todo_list,trash
from django.contrib import messages
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponseRedirect

# Create your views here.


def home(request):
    return render(request,'home.html')

def login(request):
    return render(request,"login.html")

def signup(request):
    return render(request,"signup.html")

def forgotpass(request):
    return render(request,'forgotpass.html')

def passSent(request):
    return render(request,'passSent.html')

def addtodolist(request):
    return render(request,"addtodolist.html")

# def todolist(request):
#     # print()
#     return render(request,"todolist.html")

def logindata(request):
    if request.method=="POST":
        try:
            # if(request.POST['password']==""):
            #     # userPassword = signupdetails.objects.get(email=request.POST['email'])
            #     userPassword = signupdetails.objects.get(email=request.POST['email'])
            #     # for i in userPassword:
            #         # if(request.POST['email']==userPassword.email):
            #         #     passw=userPassword.password
            #     print("user details=",userPassword.password)
            #     # request.session['email']=userPassword.email
            #     return render(request,'login.html')
            userdetails=signupdetails.objects.get(email=request.POST['email'],password=request.POST['password'])
            print("Username=",userdetails)
            request.session['email']=userdetails.email
            return render(request,'home.html')
        except signupdetails.DoesNotExist as e :
            messages.success(request,'username/password invalid...!')
    return render(request,'login.html')

def forgotPassword(request):
    if request.method=="POST":
        try:
                userPassword = signupdetails.objects.get(email=request.POST['email'])
                print("user details=",userPassword.password,'email=',userPassword.email)
                # mailsender = srinadhkotha8@gmail.com

                send_mail(
                        'password',
                        "your password is "+ 
                        userPassword.password,
                        'srinadhkotha8@gmail.com',
                        [userPassword.email],
                        fail_silently=False,
                )
                return render(request,'passSent.html')

        except signupdetails.DoesNotExist as e :
            messages.success(request,'username is not registered...!')
    return render(request,'forgotpass.html')


def logout(request):
    try:
        del request.session['email']
    except:
        return render(request,'home.html')
    return render(request,'home.html')


def insertrecord(request):
    if request.method=='POST':
        if request.POST.get('firstname') and request.POST.get('lastname') and request.POST.get('phone') and request.POST.get('email') and request.POST.get('dob') and request.POST.get('gender'):
            saverecord=signupdetails()

            saverecord.firstname=request.POST.get('firstname')
            saverecord.lastname=request.POST.get('lastname')
            saverecord.phone=request.POST.get('phone')
            saverecord.email=request.POST.get('email')
            saverecord.dob=request.POST.get('dob')
            saverecord.password=request.POST.get('password')
            saverecord.reenterpassword=request.POST.get('reenterpassword')
            saverecord.gender=request.POST.get('gender')
            if saverecord.password!=saverecord.reenterpassword:
                return redirect('insertrecord')
            else:
                saverecord.save()
            #saverecord.save()
            messages.success(request,'submitted...!')
        return render(request,'signup.html')
    else:
        return render(request,'signup.html')

def todo_listadd(request):
    if request.method=='POST':
        if request.POST.get('heading') and request.POST.get('description') and request.POST.get('comments') and request.POST.get('start_date') and request.POST.get('end_date') and request.POST.get('status'):
            id_sesss=signupdetails.objects.get(email=request.session['email'])
            saverecord1=todo_list()
            # savetotrash=trash()
            print(type(id_sesss.id))
            saverecord1.user_id=id_sesss.id
            saverecord1.heading=request.POST.get('heading')
            saverecord1.description=request.POST.get('description')
            saverecord1.comments=request.POST.get('comments')
            saverecord1.start_date=request.POST.get('start_date')
            saverecord1.end_date=request.POST.get('end_date')
            saverecord1.status=request.POST.get('status')
            
            # savetotrash.heading=request.POST.get('heading')
            # savetotrash.description=request.POST.get('description')
            # savetotrash.comments=request.POST.get('comments')
            # savetotrash.start_date=request.POST.get('start_date')
            # savetotrash.end_date=request.POST.get('end_date')
            # savetotrash.status=request.POST.get('status')
            # savetotrash.user_id=id_sesss.id
            print(id_sesss.id)
            saverecord1.save()
            # savetotrash.save()
            #saverecord.save()
            messages.success(request,'submitted...!')
        return render(request,'addtodolist.html')
    else:
        print("no err")
        return render(request,'addtodolist.html')


def my_todo(request):
    todo=signupdetails.objects.get(email=request.session['email'])
    d=todo_list.objects.filter(user=todo).all()
    todos={
        "todoslist":d
    }
    return render(request,'todolist.html',todos)

def my_todotrash(request):
    todo=signupdetails.objects.get(email=request.session['email'])
    k=trash.objects.filter(user=todo).all()
    todostrash={
        "todoslisttrash":k
    }
    print(k)
    return render(request,'trash.html',todostrash)

def del_todo(request, i):
    y = todo_list.objects.filter(id=i)
    todo=signupdetails.objects.get(email=request.session['email'])
    savetotrash=trash()
    savetotrash.user_id=y[0].user_id
    savetotrash.heading=y[0].heading
    savetotrash.description=y[0].description
    savetotrash.comments=y[0].comments
    savetotrash.start_date=y[0].start_date
    savetotrash.end_date=y[0].end_date
    savetotrash.status=y[0].status
    savetotrash.save()
    
    # # z = trash.objects.filter(id=i)
    # print(y[0].user[0])
    y.delete()


    return render(request,'home.html') 
    

def del_trash(request, i):
    y = trash.objects.filter(id=i)
    y.delete()
    return render(request,'home.html') 
    







