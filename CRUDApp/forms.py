from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Comment 

class CommentForm(ModelForm):
  comment_text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))

  class Meta:
    model = Comment
    fields = ('name', 'comment_text')


class NewUserForm(UserCreationForm):
  email = forms.EmailField(required=True)


  class Meta:
    model = User
    fields = ("username", "email", "password1", "password2")

  def save(self, commit=True):
    user = super(NewUserForm, self).save(commit=False)
    user.email = self.cleaned_data['email']
    if commit:
      user.save()
    return user    