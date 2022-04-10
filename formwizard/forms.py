from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator

from formwizard.models import BIDDING_OPTIONS


class step1(forms.Form): #Note that it is not inheriting from forms.ModelForm
    title = forms.CharField(max_length=50, widget=forms.TextInput(attrs={ 'class': 'f1-first-name form-control','placeholder': 'Enter your title'}))
    company_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={ 'class': 'f1-first-name form-control','placeholder': 'Company name'}))
    

class step2(forms.Form): #Note that it is not inheriting from forms.ModelForm
    first_name = forms.CharField(max_length=50 , widget=forms.TextInput(attrs={ 'class': 'f1-first-name form-control','placeholder': 'Enter your first name'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={ 'class': 'f1-first-name form-control','placeholder': 'Enter your last name'}))
    birth_date = forms.CharField(max_length=50 , widget=forms.TextInput(attrs={ 'class': 'f1-first-name form-control','placeholder': 'Enter your birth month'}), help_text="* For 18+ and above")

class step3(forms.Form): #Note that it is not inheriting from forms.ModelForm
    home_address = forms.EmailField(max_length=50, widget=forms.TextInput(attrs={ 'class': 'f1-first-name form-control','placeholder': 'Enter your Home Address'}))
    phone_number = forms.CharField(max_length=11, widget=forms.TextInput(attrs={ 'class': 'f1-first-name form-control','placeholder': 'Enter your phone number'}))


class step4(forms.Form): #Note that it is not inheriting from forms.ModelForm
    bidding_settings = forms.ChoiceField(choices = BIDDING_OPTIONS, widget=forms.Select(attrs={ 'class': 'f1-first-name form-control','placeholder': 'Enter your password',}))
    google_ads_account_ID = forms.CharField(max_length=50, help_text="*the value needs to be ",validators=[
            MaxValueValidator(10),
            MinValueValidator(10)
        ], widget=forms.TextInput(attrs={'class': 'f1-first-name form-control',"pattern":".{10,}", "minlength":"10", "maxlength":"10", "oninput":"numberOnly(this.id);",'placeholder': 'Enter Your Google Ads Account ID'}))

 
class step5(forms.Form): #Note that it is not inheriting from forms.ModelForm
    username = forms.CharField(max_length=50 , widget=forms.TextInput(attrs={ 'class': 'f1-first-name form-control','placeholder': 'Choose a username'}))
    email_address = forms.EmailField(max_length=50 , widget=forms.EmailInput(attrs={ 'class': 'f1-first-name form-control','placeholder': 'Enter your Email Address'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={ 'class': 'f1-first-name form-control','placeholder': 'Enter your password', "onkeypress":"test_str()"}),  help_text="*Min 8 characters, at least 1 Cap, 1 lower, 1 special characters")
    
class LoginForm(forms.Form): #Note that it is not inheriting from forms.ModelForm
    username = forms.CharField(max_length=50 , widget=forms.TextInput(attrs={ 'class': 'f1-first-name form-control','placeholder': 'Choose a username'}))

    password = forms.CharField(widget=forms.PasswordInput(attrs={ 'class': 'f1-first-name form-control','placeholder': 'Enter your password', "onkeypress":"test_str()"}),  help_text="*Min 8 characters, at least 1 Cap, 1 lower, 1 special characters")
    
