from django.shortcuts import render

from .forms import Edit
from .forms import Edit1
import smtplib
import pyautogui as pyautogui
import pyautogui as pu
from .testing import *
from django.shortcuts import render,redirect
from .models import user_details, feedbacks
from .models import mechanics_details
from .models import descriptions
from .models import notifications
from .models import status
from .models import admin_reply
from .models import admin_table
from django.http import HttpResponse
from django.template  import loader

from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login as log,logout
from .forms import AddForm2
from django.http import JsonResponse

def register(request):
    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')
        f=Check_is_sql(username)
        s=Check_is_sql(password)        
        admin = admin_table.objects.filter(username=username, password=password)
        mechanics = mechanics_details.objects.filter(username=username, password=password)
        user= user_details.objects.raw("SELECT * FROM vehicleapp_user_details WHERE username = %s AND password = %s",[username,password])
        # user = user_details.objects.filter(username=username, password=password)
        if f==0:
            if admin:
                return render(request, 'admin_home.html')
            elif mechanics:
                for x in mechanics:
                    id = x.id
                    username = x.username
                    mydict1={
                        'id':id,
                        'username':username
                    }
                return render(request, 'mechanics_home.html',context=mydict1)
            elif user:
                for i in user:
                    id = i.id
                    username=i.username
                    mydict={
                        'id':id,
                        'username':username
                    }
                return render(request, 'users_home.html',context=mydict)
            else:
                return render(request, 'login.html')
        else:
            return JsonResponse({'error':'Your IP is blocked'})
def user_home(request):
    return render(request,'users_home.html')


def reg_user(request):
    if request.method=='POST':
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        address = request.POST.get('address')
        location = request.POST.get('location')
        mobilenumber = request.POST.get('mobilenumber')
        username = request.POST.get('username')
        password = request.POST.get('password')

        print(name)


        # if _(name)==0 and _(mobilenumber)==0 and  _(location)==0 and _(username)==0 and _(password)==0 and _(address):
        #     if user_details.objects.filter(username=username).exists():
        #         pu.alert("Username is already exist")
        #     else:
        user_details(name=name,gender=gender,address=address,location=location,mobilenumber=mobilenumber,username=username,password=password).save()
        return render(request, 'index.html')
        # else:
        #     return render(request, 'secure.html')

    return render(request,'user_regi.html')


def add(request):
    if request.method=='POST':
        name = request.POST.get('name')
        age= request.POST.get('age')
        mobilenumber = request.POST.get('mobilenumber')
        email = request.POST.get('email')
        location = request.POST.get('location')
        category = request.POST.get('category')
        assign_payment = request.POST.get('assign_payment')
        salary = request.POST.get('salary')
        username = request.POST.get('username')
        password = request.POST.get('password')
        mail = request.POST.get('mail')

        if user_details.objects.filter(username=username).exists():
            pu.alert("Username is already exist")
        else:
            mechanics_details(name=name,age=age,mobilenumber=mobilenumber,email=email,location=location,category=category,assign_payment=assign_payment,salary=salary,username=username,password=password,mail=mail).save()
        return render(request, 'admin_home.html')
    return render(request,'add_mechanics.html')

def _(name):
    return Check_is_sql1(name)

def mechanichome(request):
    return render(request,'mechanics_home.html')
def admin_home(request):
    return render(request,'admin_home.html')
def viewuser(request):
    user = user_details.objects.all()
    return render(request,"viewusers.html",{'user':user})
def viewmechanics(request):
    mechanics = mechanics_details.objects.all()
    return render(request,"viewmechanics.html",{'mechanics':mechanics})

def update(request,id):
    if request.method=='POST':
        mechanics = mechanics_details.objects.get(pk=id)
        fm=Edit(request.POST,instance=mechanics)
        if fm.is_valid():
            fm.save()
        return render(request,'viewmechanics.html')
    else:
        mechanics=mechanics_details.objects.get(pk=id)
        fm=Edit(instance=mechanics)
    return render(request,'update.html',{'form':fm})



def delete(request,id):
    pi=mechanics_details.objects.get(pk=id)
    pi.delete()
    return HttpResponseRedirect('/viewmechanics')

def search(request):
    return render(request,'search_mechanics.html')
def search_viewmechanics(request):
    if request.method == 'POST':
        location = request.POST.get('location')
        category = request.POST.get('category')

        mechanics1 = mechanics_details.objects.filter(location=location,category=category)

        return render(request,"view_search.html",{'mechanics1':mechanics1})


def request_user(request,id):
    mechanics = mechanics_details.objects.filter(id=id)
    for x in mechanics:
        username = x.username
        print(username)
        location=x.location
        print(location)
        m = {'username': username,
            'location':location}
    return render(request, 'request.html',m)


def send(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        location = request.POST.get('location')
        place = request.POST.get('place')
        description = request.POST.get('description')
        descriptions(username=username, location=location, place=place, description=description).save()
        #pu.alert("Message successfully delivered to the mechanics...pls stay after few minutes")
        return render(request, 'users_home.html')

def search1(request):
    return render(request,'mech_request.html')
def mech_request(request,username):

    rst = descriptions.objects.filter(username=username)
    print(rst)

    return render(request, "viewrequests.html", {'rst': rst})




def reply(request,id):
    rst = descriptions.objects.filter(id=id)
    for x in rst:

        id = x.id
        s = {'id': id,
             }
    return render(request, 'mech_reply.html',s)

def mechreply(request):
    if request.method=='POST':
        user_id = request.POST.get('user_id')
        msg = request.POST.get('msg')
        notifications(user_id=user_id,msg=msg).save()
        return render(request,'mechanics_home.html')

def viewrequests(request):
    rst = descriptions.objects.all()
    return render(request,"viewrequests.html",{'rst':rst})

def viewrequests1(request):
    rst1 = descriptions.objects.all()
    return render(request,"viewrequests1.html",{'rst1':rst1})

def view_status(request):
    sts = status.objects.all()
    return render(request,"status_view.html",{'sts':sts})

def reply1(request):
    return render(request,'admin_reply.html')

def adminreply(request):
    if request.method=='POST':
        msg = request.POST.get('msg')
        admin_reply(msg=msg).save()
    return render(request,'admin_home.html')


def msgs(request,pk):
    msg = notifications.objects.filter(id=pk)
    return render(request,"notification.html",{'msg':msg})


#def msgs1(request,pk):
 #   msg1 = admin_reply.objects.filter(id=pk)
  #  print(msg1)
   # return render(request,"view_reply.html",{'msg1':msg1})


def update_status(request):
    if request.method=='POST':
        mechanic_name = request.POST.get('mechanic_name')
        customer_name = request.POST.get('customer_name')
        customer_mobile = request.POST.get('customer_mobile')
        location = request.POST.get('location')
        payment_status = request.POST.get('payment_status')
        #otp = request.POST.get('otp')

        status(mechanic_name=mechanic_name,customer_name=customer_name,customer_mobile=customer_mobile,location=location,payment_status=payment_status,otp=otp).save()
        return render(request, 'mechanics_home.html')
    return render(request, 'updatestatus.html')


def index(request):
    return render(request,'index.html')


def login(request):
    return render(request,'login.html')

def user_profile(request,pk):
    user = user_details.objects.get( id = pk)
    print(user)
    return render(request,"user_profile.html",{'user':user})
def mech_profile(request,pk):
    mechanics = mechanics_details.objects.get( id = pk)
    print(mechanics)
    return render(request,"mech_profile.html",{'mechanics':mechanics})

def sendmail(request,id):
    ID=int(id)
    print(ID)
    mechanics = mechanics_details.objects.filter(pk=id)
    for i in mechanics:
        email1 = i.email
        mail1=i.mail
        m=str(mail1)

        main = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        main.ehlo()
        send = 'malavikaraj1997@gmail.com'  # sender mail address
        # password=input(str("enter password"))
        password = "6282malavika"
        rec = email1 # reciver mail address
        msg=m
        main.login(send, password)
        main.sendmail(send, rec, msg)
        main.quit()
        return HttpResponseRedirect('/viewmechanics')


"""
def change_pass(request,id):
    ID = int(id)
    print(ID)

    mechanics = mechanics_details.objects.filter(pk=id)

    for i in mechanics:
        username = i.username
        password = i.password
        print(username)
        print(password)

        mechanics_details(username=username,password=password).save()



        return render(request, 'changepass.html')
    return render(request, 'mechanics_home.html')






           

         """

           #mechanics = mechanics_details.objects.filter(username=username, password=password)
""""""""""
        fm1 = Edit(request.POST, instance=mechanics)
        if fm1.is_valid():
            fm1.save()
            return render(request, 'changepass.html')

#mechanics_details.objects.filter(pk=id).update(username=username, password=password)
"""

"""
def changepass(request,id):
   
    mechanics = mechanics_details.objects.get(pk=id)
    mechanics = Edit(request.POST)
    if mechanics.is_valid():
        mechanics.save()
        return render(request,'mechhome.html')
    else:
        mechanics = Edit()  # An unbound form

    return render(request,'changepass.html',{'form':mechanics})

    if request.method=='POST':
        mechanics = mechanics_details.objects.get(id=id)
        fm=Edit(request.POST,instance=mechanics)
        if fm.is_valid():
            fm.save()
        return render(request,'mechanics_home.html')
    else:
        mechanics=mechanics_details.objects.get(id=id)
        fm=Edit(instance=mechanics)
    return render(request,'changepass.html',{'form':fm})

   """

def feedback(request):
    if request.method=='POST':
        feedback = request.POST.get('feedback')
        feedbacks(feedback=feedback).save()
        return render(request, 'users_home.html')

    return render(request, 'feedback.html')
def viewfeedback(request):
    f = feedbacks.objects.all()
    return render(request,"view_feedback.html",{'f':f})

import io
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse


def render_to_pdf(template_src, context_dict):

    template = get_template(template_src)
    html  = template.render(context_dict)
    result = io.BytesIO()
    pdf = pisa.pisaDocument(io.BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return



def pdf(request):
    from vehicleapp import models
    #a=[]
    a=models.status.objects.all()
    print(a[0])

    print("aaaaaaaaa")
    dict={
        'mechanic_name':a[0].mechanic_name,
        'customer_name':a[0].customer_name,
        'customer_mobile':a[0].customer_mobile,
        'location':a[0].location,
        'payment_status':a[0].payment_status,

        }
    for i in dict:
        pass
    # context_dict=dict

    return render_to_pdf('pdf.html',dict)
"""
def pdf1(request):
    from lostandfoundapp import models
    a=models.founddetails.objects.all()
    print("qqqqqqqqq")
    print(a)
    dict1={
        'name':a[0].name,
        'color':a[0].color,
        'date':a[0].date,
        'place':a[0].place,
        'brand':a[0].brand,
        'emp':a[0].emp,

    }
    print(dict)
    print("ddddddddddddddd")
   # context_dict=dict

    return render_to_pdf('testreport1.html',dict1)



def t_report(request, user_name):
    ass = get_object_or_404(Assign, user_name=user_name)
    sc_list = []
    for stud in ass.class_id.student_set.all():
        a = StudentCourse.objects.get(student=stud, course=ass.course)
        sc_list.append(a)
    return render(request, 'info/t_report.html', {'sc_list': sc_list})
"""
