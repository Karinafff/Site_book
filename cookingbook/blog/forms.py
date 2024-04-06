from django import forms
from .models import Comment, Post, PostPoint

class PostPointForm(forms.ModelForm):
    class Meta:
        model=PostPoint
        fields=('post_header','post_point_text','post_images')


class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('name','email','body')

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={
        "id":"inputLogin",
        "class":"form-control",
        "placeholder":"Логін",
    }))
    password=forms.CharField(widget=forms.PasswordInput(attrs={
        "type":"password",
        "id":"inputPassword",
        "class":"form-control",
        "placeholder":"Пароль",}))


class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title','short_description','image','tags')

