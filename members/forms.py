from typing import Any
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django import forms 
from CODE_APP.models import Profile

class ProfilePageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'proife_pic', 'webiste_url', 'instagram_url', 
                'facebook_url', 'twitter_url', 'linkedin_url')
        widgets= {
            "bio":forms.Textarea(attrs={'class' : 'form-control'}),
            # "proife_pic":forms.TextInput(attrs={'class' : 'form-control'}),
            "webiste_url":forms.TextInput(attrs={'class' : 'form-control'}),
            "instagram_url":forms.TextInput(attrs={'class' : 'form-control'}),
            "facebook_url":forms.TextInput(attrs={'class' : 'form-control'}),
            "twitter_url":forms.TextInput(attrs={'class' : 'form-control'}),
            "linkedin_url":forms.TextInput(attrs={'class' : 'form-control'}),

        }


class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class' : 'form-control'}))
    first_name = forms.CharField(max_length=100, required=True,widget=forms.TextInput(attrs={'class' : 'form-control'}))
    last_name = forms.CharField(max_length=100, required=True,widget=forms.TextInput(attrs={'class' : 'form-control'}))

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super(SignUpForm,self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class']= 'form-control'
        self.fields['password1'].widget.attrs['class']= 'form-control'
        self.fields['password2'].widget.attrs['class']= 'form-control'

class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class' : 'form-control'}))
    first_name = forms.CharField(max_length=100, required=True,widget=forms.TextInput(attrs={'class' : 'form-control'}))
    last_name = forms.CharField(max_length=100, required=True,widget=forms.TextInput(attrs={'class' : 'form-control'}))
    username = forms.CharField(max_length=100, required=True,widget=forms.TextInput(attrs={'class' : 'form-control'}))

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password')
    