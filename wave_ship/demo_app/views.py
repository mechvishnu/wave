from django.shortcuts import render
from django.contrib.auth.models import User
from demo_app.forms import UserForm,AppointForm
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from demo_app.models import Ticket
# Create your views here.



def index_page(request):
    return render (request,'demo_app/index.html')

def others_site(request):
    return render(request,'demo_app/others.html')

@login_required
def appointment(request):
    ticket=Ticket.objects.all()
    return render(request,'demo_app/appointment.html',context={'appointments':ticket})
@login_required
def create_appointment(request):

     if request.method=='POST':
        appoint=AppointForm(data=request.POST)
        if appoint.is_valid:
            appoint.save()
            return HttpResponseRedirect(reverse('index'))

     else:

      appoint=AppointForm
      return render (request,'demo_app/create_appointment.html',context={'appointform':appoint})


def register_page(request):
    registered=False

    if request.method =='POST':
        user_form=UserForm(data=request.POST)
        if user_form.is_valid:
            user=user_form.save()
            user.set_password(user.password)
            user.save()
            registered=True
            return render (request,'demo_app/register.html',context={'registered':registered})
        else:
           print (user.form.errors)

    else:
      forms=UserForm()
      return render (request,'demo_app/register.html',context={'forms':forms,'registered':registered})

def login_page (request):
    return render (request,'demo_app/login_form.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def user_login(request):

    if request.method =='POST':
        username =request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username ,password=password)


        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))

            else:

             return HttpResponse('ACCOUNT NOT ACTIVE !')
        else:
            return HttpResponse('Invalid username and password!')

    else:
        print ('i am here')
        return render(request,'demo_app/login_form.html')
