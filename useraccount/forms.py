from django.contrib.auth import get_user_model
#from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class SignupForm(UserCreationForm):
    email = forms.EmailField(widget = forms.EmailInput(attrs={'class':'details'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'details'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'details'}))
    phone = forms.RegexField(regex="^[6-9]\d{9}$", required=False,widget= forms.TextInput(attrs= {'class':'contactformname1'}))

    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2','email','user_type')
        widgets = {
        'username':forms.TextInput(attrs= {'class':'details'}),
        'last_name':forms.TextInput(attrs= {'class':'details'}),
        'first_name':forms.TextInput(attrs= {'class':'details'}),   
        } 

class profileform(forms.ModelForm):
    email = forms.EmailField(widget = forms.EmailInput(attrs={'class':'contactformname2'}))
    fees = forms.IntegerField(widget = forms.TextInput(attrs={'class':'contactformname2'}), required=False)
    phone_number = forms.IntegerField(widget = forms.TextInput(attrs={'class':'contactformname2'}))
    #pic = forms.ImageField(widget = forms.ImageField(attrs={'class':'contactformname2'}))

    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email', 'phone_number', 'location', 'fees', 'phone_number', 'pic', 'user_type', 'bio',)
        widgets = {
        'first_name':forms.TextInput(attrs= {'class':'contactformname2'}),
        'last_name':forms.TextInput(attrs= {'class':'contactformname2'}),
        'location':forms.TextInput(attrs= {'class':'contactformname2'}),
        'bio':forms.Textarea(attrs={'class':'contactformname2'}),
        'user_type':forms.Select(attrs={'class':'contactformname2'}),

        }