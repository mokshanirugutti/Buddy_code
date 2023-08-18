from typing import Any, Optional
from django.db import models
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from django.views import generic
from django.views.generic import DetailView,CreateView
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.urls import reverse_lazy
from .forms import SignUpForm,EditProfileForm,ProfilePageForm
from CODE_APP.models import Profile

class CreateProfilePageView(CreateView):
    model = Profile
    form_class = ProfilePageForm
    template_name = 'registration/create_profile_page.html'
    # fields = '  __all__'x

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
        
class EditProfilePageView(generic.UpdateView):
    model = Profile
    template_name = 'registration/edit_profile_page.html'
    fields = [ 
            'bio',  'proife_pic', 'webiste_url', 'instagram_url',
            'facebook_url', 'twitter_url', 'linkedin_url' 
            ]
    success_url =reverse_lazy('home')


class ShowProfilePageView(DetailView):
    model = Profile
    template_name ='registration/user_profile.html'

    def get_context_data(self, *args,**kwargs: Any):
        users = Profile.objects.all()
        context = super(ShowProfilePageView,self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile,id=self.kwargs['pk'])
        context["page_user"] = page_user
        return context


class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url =reverse_lazy('login')

class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url =reverse_lazy('home')

    def get_object(self) :
        return self.request.user