__author__ = 'leif'
from django.contrib.auth.models import User
from django import forms
from models import Category, Vehicle, Chauffeur , Company


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    username = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username','email','password')


class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Please enter the category name.",required=True)
    picture = forms.ImageField(help_text="Select item image to upload.",required=False)

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Category
        fields = ('name','picture')
