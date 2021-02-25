from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import widgets
from .models import RoomOwner

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2','first_name','last_name']
        # ,'location','phone_number']
        widgets = {
            "username": forms.TextInput(attrs={'class': 'form-control'}),
            "email": forms.EmailInput(attrs={'type': 'email', 'class': 'form-control'}),
            "first_name": forms.TextInput(attrs={'class': 'form-control'}),
            "last_name": forms.TextInput(attrs={'class': 'form-control'}),
            # "gender": forms.Select(attrs={'class': 'form-control'}),
            # "phone_number": forms.TextInput(attrs={'class': 'form-control'}),
            # "location": forms.TextInput(attrs={'class': 'form-control'}),
        }
    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = widgets.PasswordInput(attrs={'class': 'form-control'})
        self.fields['password2'].widget = widgets.PasswordInput(attrs={'class': 'form-control'})

class RoomOwnerForm(ModelForm):
    class Meta:
        model = RoomOwner
        fields = ['location','phone_number']
        widgets = {
            "phone_number": forms.TextInput(attrs={'class': 'form-control'}),
            "location": forms.TextInput(attrs={'class': 'form-control'}),
        }