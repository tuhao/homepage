from django import forms
from django.contrib.auth.models import User

class RegistForm(forms.Form):
    email = forms.EmailField(required=False)
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    confirmPwd = forms.CharField(widget=forms.PasswordInput())

    def clean_email(self):
        email = self.cleaned_data['email']
        if len(email) ==0:
            raise forms.ValidationError("email is required.")
        try:
            exist_email = User.objects.get(email=email)
        except User.DoesNotExist:
            pass
        else:
            raise forms.ValidationError("email already exists.")
        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        user_len = len(username)
        if user_len < 2 or user_len > 8:
            raise forms.ValidationError("username should be 2-8 characters.")
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            pass
        else:
            raise forms.ValidationError("username already exists.")
        return username

    def clean_password(self):
        password = self.cleaned_data.get('password','')
        pwd_len = len(password)
        if pwd_len < 5 or pwd_len > 12:
            raise forms.ValidationError('password should be 5-12 characters or numbers')
        return password

    def clean_confirmPwd(self):
        password = self.cleaned_data.get('password','')
        confirmPwd = self.cleaned_data.get('confirmPwd','')
        if password != confirmPwd:
            raise forms.ValidationError('confirm password is not the same')
        return confirmPwd
            
