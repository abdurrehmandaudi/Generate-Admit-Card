from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from .models import UserDetail

class RegForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'regTXTbox','placeholder':'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'regTXTbox','placeholder':'Re-Password'}))
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        widgets = {
            'username':forms.TextInput(attrs={'class':'regTXTbox','placeholder':'username'}),
            'first_name':forms.TextInput(attrs={'class':'regTXTbox','placeholder':'First Name','required':'required'}),
            'last_name':forms.TextInput(attrs={'class':'regTXTbox','placeholder':'Last Name','required':'required'}),
            'email':forms.EmailInput(attrs={'class':'regTXTbox','placeholder':'Email','required':'required'}),
        }

class UserDetailForm(forms.ModelForm):
    class Meta:
        model = UserDetail
        fields = ['enroll_no','roll_no','mobile','photo']
        widgets = {

            'enroll_no':forms.TextInput(attrs={'class':'regTXTbox','placeholder':'Enroll Number','required':'required'}),
            'roll_no':forms.TextInput(attrs={'class':'regTXTbox','placeholder':'Roll Number','required':'required'}),
            'mobile':forms.TextInput(attrs={'class':'regTXTbox','placeholder':'Mobile Number','required':'required'}),
            'photo':forms.FileInput(attrs={'class':'regTXTboxFile','placeholder':'Photo','required':'required'}),          
        }

class loginform(AuthenticationForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'regTXTbox','placeholder':'Password'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'regTXTbox','placeholder':'username'}))
    class Meta:
        model = User
        fields = ('username',)
        widgets = {
            'username':forms.TextInput(attrs={'class':'regTXTbox','placeholder':'username'}),
        }

        