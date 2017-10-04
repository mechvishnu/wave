from django.contrib.auth.models import User
from django import forms
from demo_app.models import Ticket


class UserForm(forms.ModelForm):
    class Meta():
        model=User
        fields=['username','email','password']



class AppointForm(forms.ModelForm):
    class Meta():
        model=Ticket
        exclude=['appointment_id']
