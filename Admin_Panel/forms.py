from django import forms
from django.contrib.auth.models import User

class CreateUserFrom(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput,label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput,label="Confirm Password")

    class Meta:
        model = User
        fields = ['username','email'] #Remove Password fields from here
    def clean(self):
        cleaned_data = super().clean()
        if(cleaned_data.get('password1') != cleaned_data.get('password2')):
            raise forms.ValidationError("Passwords don't match")
        return cleaned_data
    def save(self, commit = True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if(commit):
            user.save()
        return user
