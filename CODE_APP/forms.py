from django import forms 
from .models import Post ,Category

choices = Category.objects.all().values_list('name','name')

choices_list =[]
for item in choices:
    choices_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title","author",'category',"body")
        widgets = {
            "title":forms.TextInput(attrs={'class' : 'form-control','placeholder':'Enter title'}),
            # "author":forms.TextInput(attrs={'class' : 'form-control','id':'author_name'}),
            "author":forms.Select(attrs={'class' : 'form-control'}),
            "category":forms.Select(choices=choices_list,attrs={'class' : 'form-control'}),
            "body":forms.Textarea(attrs={'class' : 'form-control'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title",'category',"body")
        widgets = {
            "title":forms.TextInput(attrs={'class' : 'form-control','placeholder':'Enter title'}),
            "category":forms.Select(choices=choices_list,attrs={'class' : 'form-control'}),
            "body":forms.Textarea(attrs={'class' : 'form-control'}),
        }
