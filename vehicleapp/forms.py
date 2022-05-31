from django import forms
from .models import user_details
from .models import mechanics_details
from .models import descriptions
from .models import notifications
from .models import status
from .models import admin_reply
from .models import admin_table
from .models import feedbacks

class AddForm(forms.ModelForm):
    class Meta:
        model = user_details
        fields = (
        'name', 'address', 'location', 'mobilenumber','username','password')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Select(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'mobilenumber': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.TextInput(attrs={'class': 'form-control'}),
        }

class Edit(forms.ModelForm):
    class Meta:
        model=mechanics_details
        fields=('name','age','mobilenumber','email','location','category','assign_payment','salary','username','password','mail')
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'age':forms.TextInput(attrs={'class':'form-control'}),
            'mobilenumber':forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.TextInput(attrs={'class': 'form-control'}),
            'assign_payment': forms.TextInput(attrs={'class': 'form-control'}),
            'salary': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.TextInput(attrs={'class': 'form-control'}),
            'mail': forms.TextInput(attrs={'class': 'form-control'}),
        }

class AddForm2(forms.ModelForm):
    class Meta:
        model = descriptions
        fields = (
        'username','place', 'location','description')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'place': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
        }

class AddForm3(forms.ModelForm):
    class Meta:
        model = notifications
        fields = (
        'user_id','msg',)
        widgets = {
            'user_id': forms.TextInput(attrs={'class': 'form-control'}),
            'msg': forms.TextInput(attrs={'class': 'form-control'}),
        }

class AddForm4(forms.ModelForm):
    class Meta:
        model = status
        fields = (
        'mechanic_name','customer_name','customer_mobile','location','payment_status')
        widgets = {
            'mechanic_name': forms.TextInput(attrs={'class': 'form-control'}),
            'customer_name': forms.TextInput(attrs={'class': 'form-control'}),
            'customer_mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'payment_status': forms.TextInput(attrs={'class': 'form-control'}),
            #'otp': forms.TextInput(attrs={'class': 'form-control'}),

        }

class AddForm5(forms.ModelForm):
    class Meta:
        model = admin_reply
        fields = (
        'msg',)
        widgets = {
            'msg': forms.TextInput(attrs={'class': 'form-control'}),
        }

class Edit1(forms.ModelForm):
    class Meta:
        model=admin_table
        fields=('username','password')
        widgets={
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.TextInput(attrs={'class': 'form-control'}),
        }
class AddForm6(forms.ModelForm):
    class Meta:
        model=feedbacks
        fields=('feedback',)
        widgets={
            'feedback': forms.TextInput(attrs={'class': 'form-control'}),
        }
